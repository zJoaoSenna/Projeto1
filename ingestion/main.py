from orchestrator import orchestrator
from datetime import timedelta
from timeit import default_timer as timer
import urllib.request
from tasks import tasks

def dataplatform_prod_cloudfunction_hub_ingestion(request):

    Formato = 'csv' ## parametro obrigatorio: formato do arquivo 
    bucket_raw = 'data-platform-prod-gcs-raw' # parametro fixo: nome do bucket raw 
    bucket_validation = 'data-platform-prod-gcs-validation' # parametro fixo: nome do bucket validacao
    database = 'hub' # parametro obrigatorio
    url_teams = 'https://exemplo1.webhook.office.com/webhookb2/a9f0dcda-88b2-49ae-bbd0-688201db6d79@0c0bcda4-1b8e-46ab-b56c-4ae3741f4340/IncomingWebhook/a5487195276845c3afa3d701aeb139f2/a5682695-ab78-42e9-be7a-3c4a85accc1f' # parametro obrigatorio
 
    ## Get credentials 
    url_get_project_id = "http://metadata.google.internal/computeMetadata/v1/project/project-id"
    req = urllib.request.Request(url_get_project_id)
    req.add_header("Metadata-Flavor", "Google")
    project_id = urllib.request.urlopen(req).read().decode()
    project_number = tasks.get_project_number(project_id)

    username = tasks.access_secret_version(project_number,'dataplatform_userid_hub_migracao', version_id="latest")
    password = tasks.access_secret_version(project_number,'dataplatform_password_hub_migracao', version_id="latest")
    db_connection_name = 'agendas'
    host = '172.16.1.100'

    ## Para chamadas sincronas
    table_name_list = ['Restricao','PreferenciaSolucaoFuncionario','PreferenciaSegmentoFuncionario','PreferenciaPaisFuncionario','PreferenciaIdiomaFuncionario','PreferenciaEstadoFuncionario',\
                       'Negocio','HobbyFuncionario','Hobby','ExperienciaAnteriorFuncionario','EmpresaExterna','CargoExterno','AreaConhecimento','AreaConhecimentoFuncionario','Certificacao','CertificacaoFuncionario',\
                       'Curso','TipoCurso','CursoFuncionario','NivelAreaConhecimento','NivelIdioma','Idioma','IdiomaFuncionario','InstituicaoCurso','Proficiencia','Passaporte','TipoVisto','Visto','Cidadania',\
                       'Agenda', 'AgendaConfirmada', 'AgendaConfirmadaVazia', 'AgendaMensal', 'AssociacaoTipoAgenda', 'Cargo',\
                       'Carteira', 'CarteiraFuncionario', 'Cidadania', 'Cidade', 'CidadeFrente', 'ClasseFrente', 'Cliente',\
                       'CustoCargo', 'Departamento', 'DesempenhoFuncionario', 'DisponibilidadeFuncionario', 'Empresa', 'Estado',\
                       'Frente', 'FrenteMovimentacao', 'Funcao', 'Funcionario', 'FuncionarioMesSemAtuacao', \
                       'FuncionarioParticipaPoolMes', 'Negocio', 'Pais', 'PreferenciaNegocioFuncionario', 'Reclassificacao',\
                       'SegmentoMercado', 'Solucao', 'SolucaoFrente', 'SolucaoMacro', 'StatusFrente', 'SugestaoFuncionario', 'TaxaOcupacao', \
                       'TaxaOcupacaoFuncionario', 'TipoAgenda', 'TipoFrente','AtuacaoFuncionario','CidadeRegiao','CustoAdicional',\
                       'ExcecaoCargaHoraria','Feriado','JustificativaRecusa','MembrosExcecaoCargaHoraria','Regiao',\
                       'StatusSugestaoFuncionario','LogStatusFrente','HistoricoMesFuncionario','DisponibilidadeTaxaOcupacaoEstatico',\
                       'TaxaOcupacaoCarteiraEstatico','Briefing','CustoHdFuncionario', 'ViewEquipeConsumidaTotal','LogFrente','BriefingSegmento','BriefingAgenda',\
                       'ViewEquipeFormada','ViewHistoricoParticipaTO','ViewAlocacaoConsultorCanalTeams', 'ViewMapaColetivo', 'StatusAgenda']

    # Se necessário pode colocar mais parametros. Ex: path, url, secrets, login

    start = timer()

    # <Chamar o orchestrator ajustado com as necessidades da ingestão>
    orch = orchestrator(Formato,bucket_raw,bucket_validation,database,url_teams) # Se necessario pode acrescentar mais parametros de entrada nessa classe
    orch.run_pipeline_ingestion(table_name_list,host,username,password,db_connection_name) # Exemplo de objeto: As entradas desse objeto podem ser personalizadas
    
    end = timer()
    print('apply_remove_special_caracters: {}' .format(timedelta(seconds=end-start))) 

    return '200'
