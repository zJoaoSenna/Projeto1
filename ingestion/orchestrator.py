from tasks import tasks
from aiohttp import ClientSession
import asyncio
from timeit import default_timer as timer
from datetime import timedelta
import datetime
import pandas as pd

class orchestrator():

    def __init__(self,format_file:str,bucket_raw:str,bucket_validation:str,database:str,url_teams:str):

        """
        Uma classe "EXEMPLO" para a osquestração dos pipeline de ingestão 

        ...

        Attributes
        ----------
        url (str): String com a url da api\n
        format_file (str): String com o formato do arquivos na chamada da api\n
        bucket_raw (str): String com o bucket raw\n
        bucket_validation (str): String com o bucket de validacao\n
        UserID (str): String com a usuário da api [vem do cofre de senha do google secret manager]\n
        Password (str): String com a senha da api [vem do cofre de senha do google secret manager]\n
        Database (str): String com o nome do banco de dados

        Methods
        -------
        run_pipeline_livro_razao_full: roda o pipeline para extração dos dados por periodo\n
        run_pipeline_all_relatories: roda o pipeline para extração dos dados sem periodo\n
        run_program: Executa o pipeline\n
        main: Inicia o pipeline\n
        """

        self.format_file = format_file
        self.bucket_raw = bucket_raw
        self.bucket_validation = bucket_validation
        self.database = database 
        self.url_teams = url_teams

    def run_pipeline_ingestion (self,table_name_list,host,username,password,db_connection_name):

        '''
        Uma objetp  "EXEMPLO": Executa as ações de chamada da api, decodificação das respostas e gravação dos dados no GCS

                Parameters:
                        list_path (list): Lista com os caminhos dos relatórios
                Returns:
                        Não retorna nada 
        '''        
        
        # Esse modelo funciona para chamadas sincronas. Para chamadas assincronas uma nova logica deve ser escrita
        
        for table_name in  table_name_list: 
            try:
                start = timer()
                con = tasks.database_connection(host,username,password,db_connection_name)
                cursor = con.cursor(as_dict=True)
                select =f'SELECT * FROM {table_name}'
                cursor.execute(select)
                result = cursor.fetchall()
                df = pd.DataFrame(result)
                
                # Elimina o espaçamento ou quebra de linha na estruturação do dataframe          
                df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r",'"',"'"], value=["","","",""], regex=True, inplace=True)            
                
                end = timer()

                pipeline_latency = str(timedelta(seconds=end-start).total_seconds()) # Computa o tempo de ingestão
                df_info = tasks.get_dataframe_info(df,pipeline_latency,self.format_file,'200') # Estrutura um dataframe com informacoes da resposta da chamada 
                df_stats = tasks.get_dataframe_stats(df) # Estrutura um dataframe com informacoes do conteudo do dataframe
                
                data = datetime.datetime.today().strftime('%Y%m%d') # Coleta a data do dia no formato 'YYYYMMDD'

                table_name = tasks.camel_snack(table_name,'camel_to_snack') # Pode transforma para 'camel_to_snack' ou 'snack_to_camel'
                table_name_info = table_name+'/'+ table_name + '_info_ingestion' # Nome padrao para armazenar no Cloud Storage
                table_name_stats = table_name+'/'+ table_name + '_stats_ingestion' # Nome padrao para armazenar no Cloud Storage            
                tasks.upload_to_gcs(df,table_name,self.bucket_raw,data,self.database) # Armazenando os dados da tabela no Cloud Storage
                tasks.upload_to_gcs(df_info,table_name_info,self.bucket_validation,data,self.database) # Armazenando os metadados da tabela info no Cloud Storage
                tasks.upload_to_gcs(df_stats,table_name_stats,self.bucket_validation,data,self.database) # Armazenando os metadados da tabela stats no Cloud Storage
            except Exception as err:
                df = pd.DataFrame()                
                df_info = tasks.get_dataframe_info(df,'0',self.format_file,err) # Estrutura um dataframe com informacoes da resposta da chamada 
                data = datetime.datetime.today().strftime('%Y%m%d') # Coleta a data do dia no formato 'YYYYMMDD'        
                table_name_info = table_name+'/'+ table_name + '_info_ingestion' # Nome padrao para armazenar no Cloud Storage
                tasks.upload_to_gcs(df_info,table_name_info,self.bucket_validation,data,self.database) # Armazenando os metadados da tabela info no Cloud Storage
                
                
                tb = err.__traceback__                
                title_text = 'Erro na resposta da api' 
                # Texto que contendo os detalhes de eventuais erros na chamada da api
                content_text = {
                    'Título': 'Erro na resposta da api: ' + '"' + table_name + '"',
                    'TipoErro': type(err).__name__,
                    'MensagemErro': str(err),
                    "NomeArquivo": tb.tb_frame.f_code.co_filename,
                    "NomeFunção": tb.tb_frame.f_code.co_name,
                    "LinhaCodigo": tb.tb_lineno
                }  

                # Montando a mensagem (HTML) que sera exibida no teams
                content_list = []
                content_list.append(content_text)
                msg_html_title = " ".join([f"<li>{key}: {item[key]}</li>" if key !='Título' else f"<br><p><u><b>{key}: {item[key]}</b></u></p><br>" for item in content_list for key in item])
                
                # Estrutura da mensagem para envio no teams               
                content = \
                        'Suspende a cerveja e a piscina. Erro a vista :'\
                        + '<ul>'\
                        + f'{msg_html_title}'\
                        + '</ul>'
                        
                tasks.send_teams(self.url_teams, content,title_text) #  Enviando para o teams 
                pass
