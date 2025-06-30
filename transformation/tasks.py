import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
from datetime import datetime
import unicodedata
import re
import requests
import sys
import traceback
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
        df = df.to_csv(sep=";", index=False, encoding="UTF-8",header=True,date_format='%Y-%m-%dT%H:%M:%SZ')                
        blob = bucket.blob(database+'/'+table_name+'_'+data+'.csv')
        blob.upload_from_string(data=df) 
    
    
    
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
        df = pd.read_csv('gs://'+ bucket +'/'+ path + filename + '.csv',encoding='utf8',sep=";",keep_default_na=False)
        df = df.astype(str)
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

    def get_dataframe_stats(df:pd.DataFrame,column_transformation_info:pd.DataFrame):

        '''
        Retorna os dados estatisticos das tabelas 

                Parameters:
                        df (dataframe): Dataframe que será analisado
                        
                Returns:
                        df_stats (dataframe): Retorna um dataframe
        ''' 
        
        df_stats = pd.DataFrame(df.describe(include='all',datetime_is_numeric=True)).transpose().filter(['index','count','unique','types'])  
        df_types = pd.DataFrame(columns = ['ColunaType','Tipo']) 
        df_types['Tipo'] = df.dtypes            
        df_stats = pd.concat([column_transformation_info.reset_index(drop=True),df_stats.reset_index(drop=True)], axis=1)
        df_stats = pd.concat([df_stats.reset_index(drop=True), df_types.reset_index(drop=True).astype(str)], axis=1)
        df_stats = df_stats.rename(columns={"index": "Colunas", "count": "Nao_Nulos","unique": "Qtd_Unicos"}).drop('ColunaType',axis=1)

        return df_stats    

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
                ## LINHAS COMENTADAS PARA PUBLICAÇÃO APENAS DAS INFORMAÇÕES REFERENTES A INFO
                bq_client.get_table(data_quality +'.info_transformacao_' + database + '_' + table_name)
                #bq_client.get_table(data_quality +'.estatistica_transformacao_' + database + '_' + table_name)
                tableRef_info = bq_client.dataset(data_quality).table('info_transformacao_' + database + '_' + table_name)
                #tableRef_stats = bq_client.dataset(data_quality).table('estatistica_transformacao_' + database + '_' + table_name)
                job_config = bigquery.LoadJobConfig()
                job_config.write_disposition = 'WRITE_TRUNCATE'
                bigqueryJob_info  = bq_client.load_table_from_dataframe(df1, tableRef_info)
                #bigqueryJob_stats = bq_client.load_table_from_dataframe(df2, tableRef_stats,job_config=job_config)
                bigqueryJob_info.result()
                #bigqueryJob_stats.result()
            except:
                tableRef_info = bq_client.dataset(data_quality).table('info_transformacao_' + database + '_' + table_name)
                #tableRef_stats = bq_client.dataset(data_quality).table('estatistica_transformacao_' + database + '_' + table_name)
                job_config = bigquery.LoadJobConfig()
                ## LINHAS COMENTADAS PARA PUBLICAÇÃO AEPENS DAS INFORMAÇÕES DO DIA. PARA CARGA HISTÓRICA, RETONAR O 'WRITE APPEND'
                ##job_config.write_disposition = 'WRITE_APPEND'
                job_config.write_disposition = 'WRITE_TRUNCATE'
                bigqueryJob_info  = bq_client.load_table_from_dataframe(df1, tableRef_info,job_config=job_config)
                #bigqueryJob_stats = bq_client.load_table_from_dataframe(df2, tableRef_stats,job_config=job_config) 
                bigqueryJob_info.result()
                #bigqueryJob_stats.result()  
        except:
            bq_client.create_dataset(data_quality)
            tableRef_info = bq_client.dataset(data_quality).table('info_transformacao_' + database + '_' + table_name)
            #tableRef_stats = bq_client.dataset(data_quality).table('estatistica_transformacao_' + database + '_' + table_name)
            job_config = bigquery.LoadJobConfig()
            ## LINHAS COMENTADAS PARA PUBLICAÇÃO AEPENS DAS INFORMAÇÕES DO DIA. PARA CARGA HISTÓRICA, RETONAR O 'WRITE APPEND'
            ##job_config.write_disposition = 'WRITE_APPEND'
            job_config.write_disposition = 'WRITE_TRUNCATE'
            bigqueryJob_info  = bq_client.load_table_from_dataframe(df1, tableRef_info,job_config=job_config)
            #bigqueryJob_stats = bq_client.load_table_from_dataframe(df2, tableRef_stats,job_config=job_config)   
            bigqueryJob_info.result()
            #bigqueryJob_stats.result()


    def update_data_to_bq_database(df:pd.DataFrame,table_name:str,database:str,ingestion_models:str, schemaUp, project_id:str):
                
        '''
        Escreve os dados em um bucket no google cloud storage (usado para carga full)

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        ''' 
       
        bq_client = bigquery.Client(location='us-central1')
        try:
           bq_client.get_dataset(database)
           if ingestion_models == 'full_load':                        
                job_config = bigquery.LoadJobConfig()
                job_config.write_disposition = 'WRITE_TRUNCATE'               
                tableRef_name = bq_client.dataset(database).table(table_name)            
                bigqueryJob_info = bq_client.load_table_from_dataframe(df, tableRef_name,job_config=job_config)            
                bigqueryJob_info.result()
                table = bq_client.get_table(project_id + "." + database +"."+table_name)
                table.schema= schemaUp
                bq_client.update_table(table, ["schema"])
           else:                
                job_config = bigquery.LoadJobConfig()
                job_config.write_disposition = 'WRITE_APPEND'               
                tableRef_name = bq_client.dataset(database).table(table_name)            
                bigqueryJob_info = bq_client.load_table_from_dataframe(df, tableRef_name,job_config=job_config)            
                bigqueryJob_info.result() 
                table = bq_client.get_table(project_id + "." + database +"."+table_name)
                table.schema= schemaUp
                bq_client.update_table(table, ["schema"]) 
        except:            
            bq_client.create_dataset(database)
            job_config = bigquery.LoadJobConfig()
            job_config.write_disposition = 'WRITE_TRUNCATE'               
            tableRef_name = bq_client.dataset(database).table(table_name)            
            bigqueryJob_info = bq_client.load_table_from_dataframe(df, tableRef_name,job_config=job_config)                        
            bigqueryJob_info.result()

    def update_sql_to_bq_database(sql:str,table_name:str,database:str,ingestion_models:str, schemaUp, project_id:str):
                
        '''
        Escreve os dados em um bucket no google cloud storage (usado para carga full)

                Parameters:
                        df (dataframe): Dataframe que será armazenado\n
                        ActualDate (str): Senha armazenada no cofre de senha do Secret Manager (GCP)\n
                        bucket_name (str):  Nome do bucket que os dados serão gravados\n
                        
                Returns:
                        Não retorna nada
        ''' 

        bq_client = bigquery.Client(location='us-central1')
        #try:           
        if ingestion_models == 'full_load':                       
                job_config = bigquery.QueryJobConfig()
                job_config.write_disposition = 'WRITE_TRUNCATE'               
                tableRef_name = bq_client.dataset(database).table(table_name)            
                job_config.destination = tableRef_name
                query_job = bq_client.query(sql,job_config=job_config) 
                query_job.result()
                table = bq_client.get_table(project_id + "." + database +"."+table_name)
                table.schema= schemaUp
                bq_client.update_table(table, ["schema"])
        else:                
                job_config = bigquery.QueryJobConfig()
                job_config.write_disposition = 'WRITE_APPEND'               
                tableRef_name = bq_client.dataset(database).table(table_name)            
                query_job = bq_client.query(sql,job_config=job_config)            
                query_job.result()

 
    def str_to_value(df:pd.DataFrame, list_columns:list,column_transformation_info:pd.DataFrame,table_name:str,url_teams:str):
        content_list = []
        for col in list_columns:
            try:                                        
                try:
                    df[col] = df[col].replace('','nan').str.extract(r'([0-9.-]+)').astype(float)
                except:                                         
                    df[col] = df[col].str.extract(r'([0-9,.-]+)')    
                    df[col] = df[col].apply(lambda x: x.replace('.', '').replace(',', '.') if isinstance(x, str) else x).astype(float)
            
                index = column_transformation_info.index[column_transformation_info['ColunaRenomeada'] == col]
                column_transformation_info['Status'][index] = 'Transformado para o formato de float'                                 
                msg = 'Transformada'

            except Exception as ex: 
                index = column_transformation_info.index[column_transformation_info['ColunaRenomeada'] == col]
                column_transformation_info['Status'][index] = 'ERRO : Nao transformado para o formato de float'
                msg = 'Erro: Transformada mas contém erro'
                tb = ex.__traceback__
                title_text = 'Erro na transformação da tabela' + table_name 
                content_text = {
                    'Título': 'A tranformação de string para valor não foi aplicado para a coluna: ' + '"' + col + '"',
                    'TipoErro': type(ex).__name__,
                    'MensagemErro': str(ex),
                    "NomeArquivo": tb.tb_frame.f_code.co_filename,
                    "NomeFunção": tb.tb_frame.f_code.co_name,
                    "LinhaCodigo": tb.tb_lineno
                }           
                content_list.append(content_text)
                pass
        if content_list: 
            msg_html = content_list
            msg_html = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in msg_html for key in item])  
            content = \
                'Suspende a cerveja e a piscina. Erro a vista :'\
                + '<ul>'\
                + f'{msg_html}'\
                + '</ul>'                

            tasks.send_teams(url_teams, content,title_text)      
        return df,column_transformation_info,msg

    def apply_datetime(df:pd.DataFrame, list_columns:list,column_transformation_info:pd.DataFrame,table_name:str,url_teams:str):
        content_list = []
        for col in list_columns[:-1]:
            try:                   
                df[col] = pd.to_datetime(df[col],format = list_columns[-1], errors='coerce')#,utc=True)   
                index = column_transformation_info.index[column_transformation_info['ColunaRenomeada'] == col]                              
                column_transformation_info['Status'][index] = "Transformado para o formato de data"
                msg = 'Transformada'
                
            except Exception as ex:                                                
                index = column_transformation_info.index[column_transformation_info['ColunaRenomeada'] == col]
                column_transformation_info['Status'][index] = 'ERROR : Nao transformado para o formato de data'
                msg = 'Erro: Transformada mas contém erro'

                tb = ex.__traceback__
                title_text = 'Erro na transformação da tabela' + table_name 
                content_text = {
                    'Título': 'A tranformação de string para datatime não foi aplicado para a coluna: ' + '"' + col + '"',
                    'TipoErro': type(ex).__name__,
                    'MensagemErro': str(ex),
                    "NomeArquivo": tb.tb_frame.f_code.co_filename,
                    "NomeFunção": tb.tb_frame.f_code.co_name,
                    "LinhaCodigo": tb.tb_lineno
                }   
                content_list.append(content_text) 
                pass
                
        if content_list:
            msg_html = content_list
            msg_html = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in msg_html for key in item])  
            title_text = 'Erro na transformação da tabela' + table_name 
            content = \
                'Suspende a cerveja e a piscina. Erro a vista :'\
                + '<ul>'\
                + f'{msg_html}'\
                + '</ul>'                

            tasks.send_teams(url_teams, content, title_text)         

        return df,column_transformation_info,msg 

    def drop_features(df:pd.DataFrame,list_columns:list,column_transformation_info:pd.DataFrame,table_name:str,url_teams:str):
        content_list = []

        for col in list_columns:
           try:       
          
                df.drop(col,axis=1,inplace =True)
                index = column_transformation_info.index[column_transformation_info['ColunaRenomeada'] == col]                              
                column_transformation_info.drop(index, inplace=True, axis=0) 
                column_transformation_info.dropna(how='all', inplace = True)
                msg = 'Transformada'

           except Exception as ex:
                index = column_transformation_info.index[column_transformation_info['ColunaRenomeada'] == col]
                column_transformation_info['Status'][index] = 'ERROR : Nao foi retirada da tabela'
                msg = 'Erro: Transformada mas contém erro'
                tb = ex.__traceback__ 
                title_text = 'Erro na transformação da tabela' + table_name 
                content_text = {
                        'Título': 'Os caracteres especiais não foram retirados das colunas da tabela: ' + '"' + table_name + '"',
                        'TipoErro': type(ex).__name__,
                        'MensagemErro': str(ex),
                        "NomeArquivo": tb.tb_frame.f_code.co_filename,
                        "NomeFunção": tb.tb_frame.f_code.co_name,
                        "LinhaCodigo": tb.tb_lineno
                }                  
                content_list.append(content_text)
                pass  
        if content_list:
                msg_html = content_list
                msg_html = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in msg_html for key in item])  
                content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html}'\
                        + '</ul>'                

                tasks.send_teams(url_teams, content,title_text)                 
        return df,column_transformation_info,msg
    
    def remove_special_caracters(word):
        nfkd = unicodedata.normalize('NFKD', word)
        new_word = u"".join([c for c in nfkd if not unicodedata.combining(c)])   
        return re.sub('[^a-zA-Z0-9 \\\ _]', '', new_word)
            
    def apply_remove_special_caracters_columns(df:pd.DataFrame,table_name:str,column_transformation_info:str,url_teams:str,add_table_name:str):
        aux = 0
        content_list = []

        for col in df.columns:
           try:       
                new_word = tasks.remove_special_caracters(col).lower()
                if add_table_name == 'ON':
                   df = df.rename(columns={df.columns[aux]: new_word + '_' + table_name})
                   index = column_transformation_info.index[column_transformation_info['ColunaOriginal'] == col]                                 
                   column_transformation_info["ColunaRenomeada"][index] = new_word + '_' + table_name
                else:
                   df = df.rename(columns={df.columns[aux]: new_word})
                   index = column_transformation_info.index[column_transformation_info['ColunaOriginal'] == col]                                 
                   column_transformation_info["ColunaRenomeada"][index] = new_word  
                msg = 'Transformada'
                #print('apply_remove_special_caracters_columns'+str(table_name)+str(col))
           except Exception as ex:
                column_transformation_info["ColunasRenomeadas"] = "Erro - Coluna nao renomeada:" + ex
                msg = 'Erro: Transformada mas contém erro'
                tb = ex.__traceback__ 
                title_text = 'Erro na transformacao da tabela' + table_name 
                content_text = {
                        'Título': 'Os caracteres especiais não foram retirados das colunas da tabela: ' + '"' + col + '"',
                        'TipoErro': type(ex).__name__,
                        'MensagemErro': str(ex),
                        "NomeArquivo": tb.tb_frame.f_code.co_filename,
                        "NomeFunção": tb.tb_frame.f_code.co_name,
                        "LinhaCodigo": tb.tb_lineno
                }                  
                content_list.append(content_text)
           aux += 1
        
        if content_list:
                msg_html = content_list
                msg_html = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in msg_html for key in item])  
                content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html}'\
                        + '</ul>'                

                tasks.send_teams(url_teams, content,title_text) 

        return df,column_transformation_info,msg

    def drop_duplicate(df:pd.DataFrame,table_name:str,url_teams:str):
        content_list = []
        try:
                df.drop_duplicates(keep='first', inplace=True)
                msg = 'Transformada'
        except Exception as ex:
                msg = 'Erro: Transformada mas contém erro'
                tb = ex.__traceback__ 
                title_text = 'Erro na transformação da tabela' + table_name 
                content_text = {
                        'Título': 'As linhas duplicadas no foram retiradas da tabela: ' + '"' + table_name + '"',
                        'TipoErro': type(ex).__name__,
                        'MensagemErro': str(ex),
                        "NomeArquivo": tb.tb_frame.f_code.co_filename,
                        "NomeFunção": tb.tb_frame.f_code.co_name,
                        "LinhaCodigo": tb.tb_lineno
                }           
                content_list.append(content_text)   
        if content_list:
                msg_html = content_list
                msg_html = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in msg_html for key in item])  
                content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html}'\
                        + '</ul>'                

                tasks.send_teams(url_teams, content,title_text)       
       
        return df,msg 

    def rename_coluns(df:pd.DataFrame,table_name:str,url_teams:str):
        content_list = []
        try:
                df.drop_duplicates(keep='first', inplace=True)
                msg = 'Transformada'
        except Exception as ex:
                msg = 'Erro: Coluna(s) não foram renomeadas'
                tb = ex.__traceback__ 
                title_text = 'Erro em renomear colunas da tabela' + table_name 
                content_text = {
                        'Título': 'As Coluna(s) não foram renomeadas na tabela: ' + '"' + table_name + '"',
                        'TipoErro': type(ex).__name__,
                        'MensagemErro': str(ex),
                        "NomeArquivo": tb.tb_frame.f_code.co_filename,
                        "NomeFunção": tb.tb_frame.f_code.co_name,
                        "LinhaCodigo": tb.tb_lineno
                }           
                content_list.append(content_text)   
        if content_list:
                msg_html = content_list
                msg_html = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in msg_html for key in item])  
                content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html}'\
                        + '</ul>'                

                tasks.send_teams(url_teams, content,title_text)       
       
        return df,msg 


    def extract_string(df:pd.DataFrame,table_name:str,columns_list:list,strToExtract:str,columns_fmt:str,url_teams:str):
        content_list = []
        for col in columns_list: 
                try:                                
                        df[col] = df[col].str.extract(strToExtract).astype(columns_fmt)
                except Exception as ex:
                        tb = ex.__traceback__ 
                        title_text = 'Erro no enriquecimento da tabela' + table_name 
                        content_text = {
                                'Título': 'A extração não foi aplicada na' +'"'+ col +'"'+ 'da tabela' + '"' + table_name + '"',
                                'TipoErro': type(ex).__name__,
                                'MensagemErro': str(ex),
                                "NomeArquivo": tb.tb_frame.f_code.co_filename,
                                "NomeFunção": tb.tb_frame.f_code.co_name,
                                "LinhaCodigo": tb.tb_lineno
                        }           
                        content_list.append(content_text)   
        
        if content_list:
                msg_html = content_list
                msg_html = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in msg_html for key in item])  
                content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html}'\
                        + '</ul>'                

                tasks.send_teams(url_teams, content,title_text)
        return df

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