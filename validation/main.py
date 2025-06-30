import requests
from datetime import timedelta
from timeit import default_timer as timer
from orchestrator import orchestrator
from tasks import tasks
import datetime

def dataplatform_prod_cloudfunction_hub_validation(request):

    bucket_validation = 'data-platform-prod-gcs-validation'    
    database = 'hub'
    url_teams = 'https://falconi365.webhook.office.com/webhookb2/a9f0dcda-88b2-49ae-bbd0-688201db6d79@0c0bcda4-1b8e-46ab-b56c-4ae3741f4340/IncomingWebhook/a5487195276845c3afa3d701aeb139f2/a5682695-ab78-42e9-be7a-3c4a85accc1f'
    
    table_name_list = ['Agenda', 'AgendaConfirmada', 'AgendaConfirmadaVazia', 'AgendaMensal', 'AssociacaoTipoAgenda', 'Cargo',\
                       'Carteira', 'CarteiraFuncionario', 'Cidadania', 'Cidade', 'CidadeFrente', 'ClasseFrente', 'Cliente',\
                       'CustoCargo', 'Departamento', 'DesempenhoFuncionario', 'DisponibilidadeFuncionario', 'Empresa', 'Estado',\
                       'Frente', 'FrenteMovimentacao', 'Funcao', 'Funcionario', 'FuncionarioMesSemAtuacao', \
                       'FuncionarioParticipaPoolMes', 'Negocio', 'Pais', 'PreferenciaNegocioFuncionario', 'Reclassificacao',\
                       'SegmentoMercado', 'Solucao', 'SolucaoFrente', 'StatusFrente', 'SugestaoFuncionario', 'TaxaOcupacao', \
                       'TaxaOcupacaoFuncionario', 'TipoAgenda', 'TipoFrente','AtuacaoFuncionario','CidadeRegiao','CustoAdicional',\
                       'ExcecaoCargaHoraria','Feriado','JustificativaRecusa','MembrosExcecaoCargaHoraria','Regiao',\
                       'StatusSugestaoFuncionario','LogStatusFrente','HistoricoMesFuncionario','DisponibilidadeTaxaOcupacaoEstatico',\
                       'TaxaOcupacaoCarteiraEstatico','Briefing','CustoHdFuncionario', 'ViewEquipeConsumidaTotal','LogFrente','BriefingSegmento','BriefingAgenda',\
                       'ViewEquipeFormada','ViewHistoricoParticipaTO','ViewAlocacaoConsultorCanalTeams', 'ViewMapaColetivo', 'StatusAgenda']
    
    start = timer()
    orchestrator.run_pipeline_validation(bucket_validation,database,table_name_list,url_teams) # Rodar o pipeline de validacao   

    end = timer()
    print('apply_remove_special_caracters: {}' .format(timedelta(seconds=end-start)))

    return '200'

