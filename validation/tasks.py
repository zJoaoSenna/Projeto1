import pandas as pd
from pyparsing import And
import requests
from google.cloud import storage
from google.cloud import bigquery
import re
#import numpy as np
#import dask.dataframe as dd

class tasks():

    """
    Uma classe com as ferramentas de ingestão

    ...

    Attributes
    ----------
    Sem atributos

    Methods
    -------
    extract_fields_from_response: Extração das informações das chamadas\n
    get_data_from_api_async: Chamadas da api\n
    get_or_create_eventloop: Criação de loop assíncrono de execução\n
    access_secret_version: Acessando as credenciais de acesso\n
    upload_to_gcs: Carregando dados no google cloud storage
    """

    def list_gcs_directories(bucket:str, database:str): 
        
        '''
        Escreve os dados em um bucket no google cloud storage 

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        '''    
        prefix = database + '/'
        storage_client = storage.Client()
        iterator = storage_client.list_blobs(bucket, prefix=prefix, delimiter='/')
        prefixes = set()
        for page in iterator.pages:                
                prefixes.update(page.prefixes)
        prefixes = list(prefixes)
        return prefixes
     
    def get_data_from_directories(bucket:str,path:str,filename:str): 
        
        '''
        Escreve os dados em um bucket no google cloud storage 

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        '''    
        try:
            df = pd.read_csv('gs://'+ bucket +'/'+ path + filename + '.csv',encoding='utf8',sep=";")
        except:
            df = pd.read_csv('gs://'+ bucket +'/'+ path + filename + '.txt',encoding='utf8',sep=";")
        return df

    def delete_gcs_obj(table_name:str,bucket_name:str,data:str):
                
        '''
        Deleta os dados em um bucket no google cloud storage 

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        ''' 
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)                        
        blob = bucket.blob('oracle/'+table_name+'_'+data+'.csv')
        blob.delete()

    def validation_data(df_1:pd.DataFrame,df_2:pd.DataFrame,df_3:pd.DataFrame,df_4:pd.DataFrame,registry_date,table_name:str,url:str):
                
        '''
        Deleta os dados em um bucket no google cloud storage 

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        ''' 
        if df_1.iloc[0, -1] == 200:
            if df_1.iloc[0, 1] == df_2.iloc[0, 1]:
                if df_3['Colunas'].isin(df_4['Colunas']).all(axis=None):
                    df_1['Nome_Tabela'] = table_name
                    df_1['Estrutura'] = "Ok"
                    df_1['Registro'] = registry_date
                    df_3['Nome_Tabela'] = table_name
                    df_3['Registro'] = registry_date
                else:
                    add_columns_name = df_4['Colunas'][~df_4['Colunas'].isin(df_3['Colunas'])].tolist()
                    print(add_columns_name)                    
                    df_1['Nome_Tabela'] = table_name
                    df_1['Estrutura'] = f"Alerta: Mesmo nº colunas mas {add_columns_name} podem ter sido alteradas"
                    df_1['Registro'] = registry_date 
                    df_3['Nome_Tabela'] = table_name
                    df_3['Registro'] = registry_date

                    title_text = 'Alteração de estrutura da tabela: ' + table_name 
                    content_text = {
                        'Título': f"Alerta: Mesmo nº colunas mas {add_columns_name} podem ter sido alteradas"
                    }

                    content_list = []
                    content_list.append(content_text)
                    msg_html_title = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in content_list for key in item])
                                             
                    content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html_title}'\
                        + '</ul>'

                    tasks.send_teams(url, content,title_text)                   
            else:
                if df_1.iloc[0, 1] > df_2.iloc[0, 1]:
                    add_columns_name = df_3['Colunas'][~df_3['Colunas'].isin(df_4['Colunas'])].tolist()
                    print(add_columns_name)   
                    df_1['Nome_Tabela'] = table_name
                    df_1['Estrutura'] = f"Alerta: Coluna(s) {add_columns_name} foram adicionadas"
                    df_1['Registro'] = registry_date
                    df_3['Nome_Tabela'] = table_name
                    df_3['Registro'] = registry_date

                    title_text = 'Alteração de estrutura da tabela: ' + table_name 
                    content_text = {
                        'Título': f"Alerta: Coluna(s) {add_columns_name} foram adicionadas"
                     }

                    content_list = []
                    content_list.append(content_text)
                    msg_html_title = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in content_list for key in item])
                                             
                    content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html_title}'\
                        + '</ul>'

                    tasks.send_teams(url, content,title_text) 

                if df_1.iloc[0, 1] < df_2.iloc[0, 1]:
                   remove_columns_name = df_4['Colunas'][~df_4['Colunas'].isin(df_3['Colunas'])].tolist()
                   print(remove_columns_name)   
                   df_1['Nome_Tabela'] = table_name
                   df_1['Estrutura'] = f"Alerta: Coluna(s) {remove_columns_name} foram removidas"
                   df_1['Registro'] = registry_date
                   df_3['Nome_Tabela'] = table_name
                   df_3['Registro'] = registry_date

                   title_text = 'Alteração de estrutura da tabela: ' + table_name 
                   content_text = {
                        'Título': f"Alerta: Coluna(s) {remove_columns_name} foram removidas"
                   }

                   content_list = []
                   content_list.append(content_text)
                   msg_html_title = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in content_list for key in item])
                                             
                   content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html_title}'\
                        + '</ul>'
                                         
                   tasks.send_teams(url, content,title_text)                    
        else:
            df_1['Nome_Tabela'] = table_name
            df_1['Estrutura'] = "Erro: Chamada da API"
            df_1['Registro'] = registry_date
            df_3 = pd.DataFrame()    
            print('Passou por aqui')        
        return df_1, df_3

    def update_data_to_bq(df1:pd.DataFrame,df2:pd.DataFrame,database:str,table_name:str,data_quality:str):
                
        '''
        Escreve os dados em um bucket no google cloud storage 

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        ''' 
        bq_client = bigquery.Client(location='us-central1')
        
        try:
            bq_client.get_dataset(data_quality)
            try:
                bq_client.get_table(data_quality +'.info_validacao_' + database + '_' + table_name)
                bq_client.get_table(data_quality +'.estatistica_validacao_' + database + '_' + table_name)
                tableRef_info = bq_client.dataset(data_quality).table('info_validacao_' + database + '_' + table_name)
                tableRef_stats = bq_client.dataset(data_quality).table('estatistica_validacao_' + database + '_' + table_name)
                job_config = bigquery.LoadJobConfig()
                job_config.write_disposition = 'WRITE_TRUNCATE'
                bigqueryJob_info  = bq_client.load_table_from_dataframe(df1, tableRef_info)
                bigqueryJob_stats = bq_client.load_table_from_dataframe(df2, tableRef_stats,job_config=job_config)
                bigqueryJob_info.result()
                bigqueryJob_stats.result()
            except:
                tableRef_info = bq_client.dataset(data_quality).table('info_validacao_' + database + '_' + table_name)
                tableRef_stats = bq_client.dataset(data_quality).table('estatistica_validacao_' + database + '_' + table_name)
                job_config = bigquery.LoadJobConfig()
                job_config.write_disposition = 'WRITE_APPEND'
                bigqueryJob_info  = bq_client.load_table_from_dataframe(df1, tableRef_info,job_config=job_config)
                bigqueryJob_stats = bq_client.load_table_from_dataframe(df2, tableRef_stats,job_config=job_config) 
                bigqueryJob_info.result()
                bigqueryJob_stats.result()  
        except:            
            bq_client.create_dataset(data_quality)
            tableRef_info = bq_client.dataset(data_quality).table('info_validacao_' + database + '_' + table_name)
            tableRef_stats = bq_client.dataset(data_quality).table('estatistica_validacao_' + database + '_' + table_name)
            job_config = bigquery.LoadJobConfig()
            job_config.write_disposition = 'WRITE_APPEND'
            bigqueryJob_info  = bq_client.load_table_from_dataframe(df1, tableRef_info,job_config=job_config)
            bigqueryJob_stats = bq_client.load_table_from_dataframe(df2, tableRef_stats,job_config=job_config)     
            bigqueryJob_info.result()
            bigqueryJob_stats.result()

    def update_test_to_bq(df1:pd.DataFrame,df2:pd.DataFrame,database:str,data_quality:str):
                
        '''
        Escreve os dados em um bucket no google cloud storage 

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        ''' 
        bq_client = bigquery.Client(location='us-central1')
        job_config = bigquery.QueryJobConfig()
        job_config.write_disposition = 'WRITE_TRUNCATE'
        tableRef_info = bq_client.dataset(data_quality).table('info_teste_' + database)
        tableRef_stats = bq_client.dataset(data_quality).table('estatistica_teste_' + database)
        bigqueryJob_info = bq_client.load_table_from_dataframe(df1, tableRef_info,job_config=job_config)
        bigqueryJob_stats = bq_client.load_table_from_dataframe(df2, tableRef_stats,job_config=job_config)
        bigqueryJob_info.result()
        bigqueryJob_stats.result()
     
    def send_teams(webhook_url:str, content:str, title:str, color:str="000000") -> int:
        """
        - Send a teams notification to the desired webhook_url
        - Returns the status code of the HTTP request
                - webhook_url : the url you got from the teams webhook configuration
                - content : your formatted notification content
                - title : the message that'll be displayed as title, and on phone notifications
                - color (optional) : hexadecimal code of the notification's top line color, default corresponds to black
        """
        response = requests.post(
                url=webhook_url,
                headers={"Content-Type": "application/json"},
                json={
                "themeColor": color,
                "summary": title,
                "sections": [{
                        "activityTitle": title,
                        "activitySubtitle": content
                }],
                },
        )
        return response.status_code 

    def camel_snack(word:str,conversion_type:str):
       if conversion_type == 'camel_to_snack':
              word = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
       else:
           if conversion_type == 'snack_to_camel':
              word =  ''.join(word.title() for word in word.split('_')) 
       return word