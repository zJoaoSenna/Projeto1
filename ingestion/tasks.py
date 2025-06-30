import pandas as pd
import requests
import pymssql
from google.cloud import storage
from google.cloud import resourcemanager_v3
from google.cloud import secretmanager
import re

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

    def upload_to_gcs(df:pd.DataFrame,table_name:str,bucket_name:str,data:str,database:str):
                
        '''
        Escreve os dados em um bucket no google cloud storage 
                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        database (str): Nome do banco de dados
                Returns:
                        Não retorna nada
        ''' 
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)        
        df = df.to_csv(sep=";", index=False, encoding="UTF-8",header=True)                
        blob = bucket.blob(database+'/'+table_name+'_'+data+'.csv')
        blob.upload_from_string(data=df)    
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
        df = pd.read_csv('gs://'+ bucket +'/'+ path + filename + '.csv',encoding='utf8')
        print('gs://'+ bucket +'/'+ path + filename + '.csv')
        return df

    def get_dataframe_info(df:pd.DataFrame,latency:str,format:str,status:str):

        '''
        Retorna as informações gerais das tabelas 
                Parameters:
                        df (dataframe): Dataframe que será analisado\n
                        latency (str): Tempo de execução das chamadas na api\n
                        format (str):  Formato do arquivo de leitura\n
                        status (str): Status de resposta da api
                        
                Returns:
                        df_info (dataframe): Retorna um dataframe
        ''' 
        if df.empty:       
                data = [{'N_Linhas': 'Nulo',\
                        'N_Colunas': 'Nulo',\
                        'Volume_MB':'Nulo',\
                        'Velocidade_s':'Nulo',\
                        'Formato': 'Nulo',\
                        'Status': status}]
                df_info = pd.DataFrame(data)
        else:
                data = [{'N_Linhas': df.shape[0],\
                        'N_Colunas': df.shape[1],\
                        'Volume_MB':(df.memory_usage(deep=True)/1024/1024).sum(),\
                        'Velocidade_s':latency,\
                        'Formato': format,\
                        'Status': status}]
                df_info = pd.DataFrame(data)

        return df_info

    def get_dataframe_stats(df:pd.DataFrame):

        '''
        Retorna os dados estatisticos das tabelas 
                Parameters:
                        df (dataframe): Dataframe que será analisado
                        
                Returns:
                        df_stats (dataframe): Retorna um dataframe
        ''' 
        #df_stats = pd.DataFrame(df.describe(include='all')).transpose()
        df_stats = pd.DataFrame(df.describe(include='all',datetime_is_numeric=True)).transpose().filter(['index','count','unique'])         
        df_types = pd.DataFrame(df.dtypes)
        df_types_columns = ["types"]
        df_types.columns = df_types_columns     
        df_stats = pd.concat([df_stats, df_types[["types"]]], axis=1) 
        df_stats = df_stats.reset_index()
        df_stats = df_stats.rename(columns={"index": "Colunas", "count": "Nao_Nulos","unique": "Qtd_Unicos","types": "Tipo"})
                
        return df_stats

    def send_teams(webhook_url:str, content:str, title:str, color:str="000000") -> int:
        """
        - Send a teams notification to the desired webhook_url
        - Returns the status code of the HTTP request
                - webhook_url : the url you got from the teams webhook configuration
                - content : your formatted notification content
                - title : the message that'll be displayed as title, and on phone notifications
                - color (optional) : hexadecimal code of the notification's top line color, default corresponds to black
        """
        print(content)
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

    def database_connection(host:str,username:str,password:str,db_connection_name:str): 
        
        '''
        Escreve os dados em um bucket no google cloud storage 

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        '''  
        connection = {
                        'host': host,
                        'username': username,
                        'password': password,
                        'db': db_connection_name
                        }

        con=pymssql.connect(connection['host'],connection['username'],connection['password'],connection['db'])  
        return con

    def get_project_number(project_id):
        """Given a project id, return the project number"""
        # Create a client
        client = resourcemanager_v3.ProjectsClient()
        # Initialize request argument(s)
        request = resourcemanager_v3.SearchProjectsRequest()
        # Make the request
        page_result = client.search_projects(request=request)
        # Handle the response
        for response in page_result:
                if response.project_id == project_id:
                        project = response.name
                        return project.replace('projects/', '') 

    def camel_snack(word:str,conversion_type:str):
       if conversion_type == 'camel_to_snack':
              word = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
       else:
           if conversion_type == 'snack_to_camel':
              word =  ''.join(word.title() for word in word.split('_')) 
       return word

    def access_secret_version(project_number:str,secret_id:str, version_id="latest"): 

        '''
        Retorna os dados dos relatórios decodificados 

                Parameters:
                        project_number (str): Número do projeto na GCP\n
                        secret_id (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        version_id (str):  Sempre a última versão da biblioteca do Secret Manager\n
                        
                Returns:
                        response_txt (str): Retorna o texto extraido da chamada da api
        '''   
        client = secretmanager.SecretManagerServiceClient()    
        name = f"projects/{project_number}/secrets/{secret_id}/versions/{version_id}"   
        response = client.access_secret_version(name=name)    
        return response.payload.data.decode('UTF-8')