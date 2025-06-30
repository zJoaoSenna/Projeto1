from tasks import tasks
from timeit import default_timer as timer
from datetime import timedelta
import datetime
import pandas as pd

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
     

    def run_pipeline_validation(bucket:str,database:str,table_name_list:list,url:str):

        '''
        Executa as ações de chamada da api, decodificação das respostas e gravação dos dados no GCS

                Parameters:
                        list_path (list): Lista com os caminhos dos relatórios
                Returns:
                        Não retorna nada 
        '''
        #list_gcs_directories = tasks.list_gcs_directories(bucket, database) # Lista a primeira camada de pasta no bucket de validacao 

        today = datetime.datetime.today().strftime('%Y%m%d') # Coleta a data do dia no formato 'YYYYMMDD'
        yesterday = (datetime.datetime.today() - timedelta(days=1)).strftime('%Y%m%d') #  Coleta a data do dia anterior no formato 'YYYYMMDD'

        for table_name in table_name_list:
            table_name = tasks.camel_snack(table_name,'camel_to_snack')
            filename_info_today = table_name + '_info_ingestion_' + today # Nome padrao para acessar no Cloud Storage dados de informacoes gerais de hoje
            filename_info_yesterday = table_name + '_info_ingestion_' + yesterday # Nome padrao para acessar no Cloud Storage dados de informacoes gerais do dia anterior
            filename_stats_today = table_name + '_stats_ingestion_' + today # Nome padrao para acessar no Cloud Storage dados de informacoes das colunas de hoje
            filename_stats_yesterday = table_name + '_stats_ingestion_' + yesterday # Nome padrao para acessar no Cloud Storage dados de informacoes das colunas do dia anterior
            #table_name = path.split('/')[-2] # Nome da tabela contido no diretorio
            path = database +'/'+ table_name +'/'
            df_info_today = tasks.get_data_from_directories(bucket,path,filename_info_today) # Coletando os dados da tabela info no arquivo dentro de Cloud Storage dia atual
            df_stats_today = tasks.get_data_from_directories(bucket,path,filename_stats_today) # Coletando os dados da tabela stats no Cloud Storage dia atual

            try:
                df_info_yesterday = tasks.get_data_from_directories(bucket,path,filename_info_yesterday) # Coletando os dados da tabela info no arquivo dentro de Cloud Storage dia anterior
                df_stats_yesterday = tasks.get_data_from_directories(bucket,path,filename_stats_yesterday) # Coletando os dados da tabela stats no Cloud Storage dia anterior
            except:
                df_info_yesterday = df_info_today
                df_stats_yesterday = df_stats_today
            
            registry_date = datetime.datetime.today() # Coleta a data do dia no formato timestamp  

            # Estrutura um dataframe com informacoes da resposta da chamada
            # Estrutura um dataframe com informacoes do conteudo do dataframe
            df_info,df_stats = tasks.validation_data(df_info_today,df_info_yesterday,df_stats_today,df_stats_yesterday,registry_date,table_name,url)
            #tasks.update_data_to_bq(df_info,df_stats,database,table_name,'data_quality') # Gravar os dados da tabela info e os dados da tabela stats no BigQuery

    def test_pipeline_validation(bucket:str,database:str,url:str,database_test:str):

        '''
        Executa as ações de chamada da api, decodificação das respostas e gravação dos dados no GCS

                Parameters:
                        list_path (list): Lista com os caminhos dos relatórios
                Returns:
                        Não retorna nada 
        '''
        list_gcs_directories = tasks.list_gcs_directories(bucket, database_test) 

        df_info_concat = pd.DataFrame()
        df_stats_concat = pd.DataFrame()

        for path in list_gcs_directories:
            filename_info_today = 'info_20220614' # Nome padrao para acessar no Cloud Storage dados de informacoes gerais com data generica
            filename_info_yesterday = 'info_20220613' # Nome padrao para acessar no Cloud Storage dados de informacoes gerais da data generica anterior
            filename_stats_today = 'stats_20220614' # Nome padrao para acessar no Cloud Storage dados de informacoes das colunas com data generica
            filename_stats_yesterday = 'stats_20220613' # Nome padrao para acessar no Cloud Storage dados de informacoes das colunas da data generica anterior
            table_name = path.split('/')[-2]

            df_info_today = tasks.get_data_from_directories(bucket,path,filename_info_today) # Coletando os dados da tabela info no arquivo dentro de Cloud Storage com data generica
            df_stats_today = tasks.get_data_from_directories(bucket,path,filename_stats_today) # Coletando os dados da tabela stats no Cloud Storage com data generica
            df_info_yesterday = tasks.get_data_from_directories(bucket,path,filename_info_yesterday) # Coletando os dados da tabela info no arquivo dentro de Cloud Storage da data generica anterior
            df_stats_yesterday = tasks.get_data_from_directories(bucket,path,filename_stats_yesterday) # Coletando os dados da tabela stats no Cloud Storage da data generica anterior
            
            registry_date = datetime.datetime.today() # Coleta a data do dia no formato timestamp  

            # Estrutura um dataframe com informacoes da resposta da chamada
            # Estrutura um dataframe com informacoes do conteudo do dataframe
            df_info,df_stats = tasks.validation_data(df_info_today,df_info_yesterday,df_stats_today,df_stats_yesterday,registry_date,table_name,url)
            df_info_concat = pd.concat([df_info_concat, df_info], axis=0)
            df_stats_concat = pd.concat([df_stats_concat, df_stats], axis=0)
        tasks.update_test_to_bq(df_info,df_stats,database,'data_quality') # Gravar os dados da tabela info e os dados da tabela stats no BigQuery