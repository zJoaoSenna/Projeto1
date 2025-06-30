import json
from tasks import tasks
from timeit import default_timer as timer
from datetime import timedelta
import datetime
import pandas as pd
from re import search
from google.cloud import bigquery
from google.cloud.bigquery.schema import PolicyTagList
class orchestrator():    
    

    """
    Uma classe de osquestração dos pipeline de ingestão

    ...

    Attributes
    ----------
    url (str): String com a url da api\n
    format_file (str): String com o formato do arquivos na chamada da api\n
    bucket_raw (str): String com o bucket raw\n
    bucket_validation (str): String com o bucket de validacao\n
    UserID (str): String com a usuário da api [vem do cofre de senha do google secret manager]\n
    Password (str): String com a senha da api [vem do cofre de senha do google secret manager]\n

    Methods
    -------
    run_pipeline_livro_razao_full: roda o pipeline para extração dos dados por periodo\n
    run_pipeline_all_relatories: roda o pipeline para extração dos dados sem periodo\n
    run_program: Executa o pipeline\n
    main: Inicia o pipeline\n
    """
          
    def run_pipeline_transformation(bucket_ingestion:str,database:str,job,url_teams:str, project_id:str):

      '''
      Executa as ações de chamada da api, decodificação das respostas e gravação dos dados no GCS

               Parameters:
                     list_path (list): Lista com os caminhos dos relatórios
               Returns:
                     Não retorna nada 
      '''
      start = timer()

      today = datetime.datetime.today().strftime('%Y%m%d') # Coleta a data do dia no formato 'YYYYMMDD'      
      registry_date = datetime.datetime.today() # Coleta a data do dia no formato timestamp      
      
      for table in job:
        
         start = timer()
         filename = table + '_' + today # Nome a tabela que sera acessada no bucket raw
         path = database + '/' 
         df_table = tasks.get_data_from_directories(bucket_ingestion,path,filename) # Leitura dos dados da tabela contida no bucket raw
         column_transformation_info = pd.DataFrame(columns = ['ColunaOriginal','ColunaRenomeada','Status']) # Montagem da estrutura da tabela de info de transformacao
         column_transformation_info['ColunaOriginal'] = list(df_table.columns) # Montagem da estrutura da tabela de info de transformacao
         column_transformation_info['Status'] = 'Transformação não aplicada' # Montagem da estrutura da tabela de info de transformacao
         new_tablename = table

         for k, v in job[table].items():           

            if k == 'remove_linhas_duplicadas': # Remove todos as linhas duplicadas
               df_table,msg = tasks.drop_duplicate(df_table,table,url_teams)

            if k == 'remover_caracter_especial_colunas': # Remove os caracteres especiais de todas as colunas
               df_table,column_transformation_info,msg = tasks.apply_remove_special_caracters_columns(df_table,table,column_transformation_info,url_teams,add_table_name = 'ON')
 
            if k == 'remover_colunas': # Remove as colunas especificadas
               df_table,column_transformation_info,msg = tasks.drop_features(df_table,v,column_transformation_info,table,url_teams)
               
            if k == 'transforma_decimal': # Transforma para decimal as colunas especificadas
               df_table,column_transformation_info,msg = tasks.str_to_value(df_table,v,column_transformation_info,table,url_teams) 
             
            if search("transforma_data", k): # Transforma para datatime as colunas especificadas            
               df_table,column_transformation_info,msg = tasks.apply_datetime(df_table,v,column_transformation_info,table,url_teams)

            if k == 'renomear_tables': # Renomeia a tabela    
               new_tablename = v               

            if k == 'ingestion_models':
               ingestion_models = v

            if k == 'filtrar_colunas':
                SchemaUp = []                
                for k,v in job[table]['filtrar_colunas'].items():                                       
                    #policy_tags = PolicyTagList(names=["projects/data-plataform-prd/locations/us-central1/taxonomies/724454937206755859/policyTags/6121450378573031565"])                           
                    #parcelasafaturar_oracle = PolicyTagList(names=["projects/data-platform-327618/locations/us-central1/taxonomies/8710032562362372476/policyTags/5695854228660259497"])
                    schema = bigquery.SchemaField(k, bigquery.enums.SqlTypeNames[v[0]], description=None, policy_tags=PolicyTagList(names=[v[2]]))        
                    SchemaUp.append(schema)

         column_transformation_info.drop('ColunaOriginal',axis=1,inplace =True) # Montagem da estrutura da tabela de stats de transformacao
         df_stats = tasks.get_dataframe_stats(df_table,column_transformation_info) # Montagem da estrutura da tabela de stats de transformacao
         df_stats['Nome_Tabela'] = table # Nome da tabela
         df_stats['Registro'] = registry_date # Coluna com data do registro

         end = timer()                 
         pipeline_latency = str(timedelta(seconds=end-start).total_seconds())  
         
         df_info = tasks.get_dataframe_info(df_table,pipeline_latency,'csv',msg)
         df_info['Nome_Tabela'] = table # Nome da tabela
         df_info['Registro'] = registry_date   # Coluna com data do registro  
           
         tasks.update_data_to_bq_database(df_table,new_tablename,database,ingestion_models, SchemaUp, project_id)
         tasks.update_data_to_bq(df_info,df_stats,database,new_tablename,'data_quality') # Gravar os dados da tabela info e os dados da tabela stats no BigQuery

    def run_pipeline_view(database:str,queries,project_id:str):   
        for query in queries:
            new_tablename = query
            for k, v in queries[query].items(): 
                if k == 'renomear_tables':   
                    new_tablename = v
                if k == 'filtrar_colunas':
                    SchemaUp = []           
                    for k,v in queries[query]['filtrar_colunas'].items():                                                       
                        schema = bigquery.SchemaField(k, bigquery.enums.SqlTypeNames[v[0]], description=None, policy_tags=PolicyTagList(names=[v[2]]))        
                        SchemaUp.append(schema)
                if k == 'query':
                    sql = v
                if k == 'ingestion_models':
                    ingestion_models = v                    
            tasks.update_sql_to_bq_database(sql,new_tablename,database,ingestion_models, SchemaUp, project_id)


            




