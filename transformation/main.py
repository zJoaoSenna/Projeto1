import requests
from datetime import timedelta
from timeit import default_timer as timer
from orchestrator import orchestrator
from tasks import tasks
import datetime
import urllib.request


def dataplatform_prod_cloudfunction_hub_transformation(request):

   bucket_raw = 'data-platform-prod-gcs-raw'   
   database = 'hub'
   url_teams = 'https://falconi365.webhook.office.com/webhookb2/a9f0dcda-88b2-49ae-bbd0-688201db6d79@0c0bcda4-1b8e-46ab-b56c-4ae3741f4340/IncomingWebhook/a5487195276845c3afa3d701aeb139f2/a5682695-ab78-42e9-be7a-3c4a85accc1f' # parametro obrigatorio
   url_get_project_id = "http://metadata.google.internal/computeMetadata/v1/project/project-id"
   req = urllib.request.Request(url_get_project_id)
   req.add_header("Metadata-Flavor", "Google")
   project_id = urllib.request.urlopen(req).read().decode() 
   #remover_colunas;
   #remover_caracter_especial_colunas;
   #valor_moeda: transformar valor de moeda em valor numérico
   #transforma_data : transforma o formato string para datetime
   #extrair_aplicar_tipo : retira qualquer caracter não numérico, porém, permanece no formato de string - Não tem
   #remove_linhas_duplicadas: filtrar linhas duplicadas - Não tem

   #{"relatorio_de_notas_emitidas":
   #     {
   #     Escreva as transformações aqui
   #     },

   job = {
      "visto":
      {
           "renomear_tables": 'visto_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_visto' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'numero_visto': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_visto': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_visto' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_visto' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'validade_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'tipovistoid_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'paisid_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "tipo_visto":
      {
           "renomear_tables": 'tipo_visto_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_tipo_visto' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'codigo_tipo_visto': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_tipo_visto': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_tipo_visto' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_tipo_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_tipo_visto' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_tipo_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeingles_tipo_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeespanhol_tipo_visto' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "tipo_curso":
      {
           "renomear_tables": 'tipo_curso_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_tipo_curso' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'codigo_tipo_curso': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_tipo_curso': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_tipo_curso' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_tipo_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_tipo_curso' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_tipo_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeingles_tipo_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeespanhol_tipo_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "restricao":
      {
           "renomear_tables": 'restricao_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_restricao' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'tipo_restricao': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_restricao': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_restricao' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_restricao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_restricao' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_restricao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'observacao_restricao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainicio_restricao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datafim_restricao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "preferencia_solucao_funcionario":
      {
           "renomear_tables": 'preferencia_solucao_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_preferencia_solucao_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'preferencia_preferencia_solucao_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_preferencia_solucao_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_preferencia_solucao_funcionario' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_preferencia_solucao_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_preferencia_solucao_funcionario' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_preferencia_solucao_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'solucaomacroid_preferencia_solucao_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "preferencia_segmento_funcionario":
      {
           "renomear_tables": 'preferencia_segmento_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_preferencia_segmento_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'preferencia_preferencia_segmento_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_preferencia_segmento_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_preferencia_segmento_funcionario' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_preferencia_segmento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_preferencia_segmento_funcionario' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_preferencia_segmento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'segmentomercadoid_preferencia_segmento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "preferencia_pais_funcionario":
      {
           "renomear_tables": 'preferencia_pais_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_preferencia_pais_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'prioridade_preferencia_pais_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_preferencia_pais_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_preferencia_pais_funcionario' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_preferencia_pais_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_preferencia_pais_funcionario' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_preferencia_pais_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'paisid_preferencia_pais_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "preferencia_idioma_funcionario":
      {
           "renomear_tables": 'preferencia_idioma_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_preferencia_idioma_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_preferencia_idioma_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_preferencia_idioma_funcionario' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_preferencia_idioma_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_preferencia_idioma_funcionario' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_preferencia_idioma_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'idiomaid_preferencia_idioma_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "preferencia_estado_funcionario":
      {
           "renomear_tables": 'preferencia_estado_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_preferencia_estado_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'preferencia_preferencia_estado_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_preferencia_estado_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_preferencia_estado_funcionario' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_preferencia_estado_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_preferencia_estado_funcionario' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_preferencia_estado_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'estadoid_preferencia_estado_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "instituicao_curso":
      {
           "renomear_tables": 'instituicao_curso_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_instituicao_curso' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'codigo_instituicao_curso': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_instituicao_curso': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_instituicao_curso' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_instituicao_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_instituicao_curso' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_instituicao_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "idioma_funcionario":
      {
           "renomear_tables": 'idioma_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_idioma_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_idioma_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_idioma_funcionario' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_idioma_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_idioma_funcionario' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datateste_idioma_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'observacao_idioma_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_idioma_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'idiomaid_idioma_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'proficienciaid_idioma_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nivelidiomaid_idioma_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },      
      "idioma":
      {
           "renomear_tables": 'idioma_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_idioma' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'codigo_idioma': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_idioma': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_idioma' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_idioma' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_idioma' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_idioma' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeingles_idioma' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeespanhol_idioma' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "hobby_funcionario":
      {
           "renomear_tables": 'hobby_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_hobby_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_hobby_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_hobby_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_hobby_funcionario' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_hobby_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_hobby_funcionario' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'hobbyid_hobby_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_hobby_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                       }
      },
      "hobby":
      {
           "renomear_tables": 'hobby_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_hobby' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_hobby': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_hobby': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_hobby' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_hobby' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_hobby' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']
                       }
      },
      "cargo_externo":
      {
           "renomear_tables": 'cargo_externo_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_cargo_externo' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'codigo_cargo_externo': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_cargo_externo': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_cargo_externo' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_cargo_externo' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_cargo_externo' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_cargo_externo' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "curso":
      {
           "renomear_tables": 'curso_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_curso' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'codigo_curso': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_curso': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_curso' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_curso' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'tipocursoid_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeingles_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeespanhol_curso' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "certificacao":
      {
           "renomear_tables": 'certificacao_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_certificacao' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'codigo_certificacao': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_certificacao': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_certificacao' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_certificacao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_certificacao' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_certificacao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeingles_certificacao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeespanhol_certificacao' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      }, 
      "empresa_externa":
      {
           "renomear_tables": 'empresa_externa_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_empresa_externa' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_empresa_externa': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_empresa_externa': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_empresa_externa' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_empresa_externa' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_empresa_externa' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },
      "area_conhecimento_funcionario":
      {
           "renomear_tables": 'area_conhecimento_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_area_conhecimento_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'areaconhecimentoid_area_conhecimento_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_area_conhecimento_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_area_conhecimento_funcionario' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_area_conhecimento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_area_conhecimento_funcionario' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nivelareaconhecimentoid_area_conhecimento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_area_conhecimento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'observacao_area_conhecimento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'validadolideranca_area_conhecimento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'anexo_area_conhecimento_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      }, 
      "area_conhecimento":
      {
           "renomear_tables": 'area_conhecimento_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_area_conhecimento' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'codigo_area_conhecimento': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_area_conhecimento': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_area_conhecimento' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_area_conhecimento' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_area_conhecimento' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_area_conhecimento' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeingles_area_conhecimento' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeespanhol_area_conhecimento' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      }, 
      "passaporte":
      {
           "renomear_tables": 'passaporte_hub',
		   "remove_linhas_duplicadas": ['ALL'],	
           "transforma_data": ['DataInclusao','DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                        'id_passaporte' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'numero_passaporte': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_passaporte': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_passaporte' : ["DATETIME", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_passaporte' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_passaporte' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'validade_passaporte' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'funcionarioid_passaporte' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'paisid_passaporte' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
      },     
      "view_equipe_consumida_total": 
	  {
		   "renomear_tables": 'view_equipe_consumida_total_hub',
		   "remove_linhas_duplicadas": ['ALL'],		
           "transforma_decimal": ['EquipeConsumidaTotal'],	
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'frenteid_view_equipe_consumida_total' : ["STRING", "[INTERN] Front id.", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5636748190349793674'],
                    'equipeconsumidatotal_view_equipe_consumida_total': ["FLOAT","[INTERN] Total cost consumed by the front of the project.", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5636748190349793674']}
	  },
      "view_alocacao_consultor_canal_teams":
      {
           "renomear_tables": 'view_alocacao_consultor_canal_teams_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['DataInicioPrevista','Periodo', 'PrimeiraAgenda', 'DataUltimoHdRascunho', '%Y-%m-%d'],
           "remover_caracter_especial_colunas": ['ALL'], 
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"codigofuncionario_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "nomefuncionario_view_alocacao_consultor_canal_teams": ["STRING", '[RESTRICT] Alert! Description pending with the base manager.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "email_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "codigofrente_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "nomefrente_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "status_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "codigocliente_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "nomefantasiacliente_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "codigosocio_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "nomesocio_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "codigolidernivel2_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "nomelidernivel2_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "codigolidernivel3_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "nomelidernivel3_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "codigolidernivel4_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "nomelidernivel4_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "datainicioprevista_view_alocacao_consultor_canal_teams": ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "periodo_view_alocacao_consultor_canal_teams": ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "codigofuncao_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "nomefuncao_view_alocacao_consultor_canal_teams": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "primeiraagenda_view_alocacao_consultor_canal_teams": ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"],
                            "dataUltimohdrascunho_view_alocacao_consultor_canal_teams": ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6692949998875618211"]}
       },
      "view_historico_participa_t_o":
      {
           "renomear_tables": 'view_historico_participa_t_o_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "remover_caracter_especial_colunas": ['ALL'], 
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"colaboradorid_view_historico_participa_t_o": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"],
                            "colaboradorcodigo_view_historico_participa_t_o": ["STRING", '[RESTRICT] Alert! Description pending with the base manager.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"],
                            "colaboradornome_view_historico_participa_t_o": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"],
                            "mes_view_historico_participa_t_o": ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"],
                            "cargoid_view_historico_participa_t_o": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"],
                            "cargocodigo_view_historico_participa_t_o": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"],
                            "cargonome_view_historico_participa_t_o": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"],
                            "areaid_view_historico_participa_t_o": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"],
                            "area_view_historico_participa_t_o": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6187345652523962260"]}
       },
      "view_equipe_formada":
       {
           "renomear_tables": 'view_equipe_formada_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Data', '%Y-%m-%d %H:%M:%S.%f'],
           "remover_caracter_especial_colunas": ['ALL'], 
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"codigofrente_view_equipe_formada": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7441185532164013575"],
                            "nomefrente_view_equipe_formada": ["STRING", '[RESTRICT] Alert! Description pending with the base manager.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7441185532164013575"],
                            "justificativa_view_equipe_formada": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7441185532164013575"],
                            "usuario_view_equipe_formada": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7441185532164013575"],
                            "data_view_equipe_formada": ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7441185532164013575"],
                            "ehmobilizacao_view_equipe_formada": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7441185532164013575"]}
       },
        "briefing_agenda":
       {
           "renomear_tables": 'briefing_agenda_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'], 
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_briefing_agenda": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1307430624815938198"],
                            "briefingid_briefing_agenda": ["STRING", '[RESTRICT] Alert! Description pending with the base manager.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1307430624815938198"],
                            "funcionariosugeridoid_briefing_agenda": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1307430624815938198"],
                            "agendaid_briefing_agenda": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1307430624815938198"],
                            "cargooriginalid_briefing_agenda": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1307430624815938198"],
                            "prazomobilidade_briefing_agenda": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1307430624815938198"]}
       }, 
        "briefing_segmento":
       {
           "renomear_tables": 'briefing_segmento_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "transforma_decimal": ['Hds'],
           "remover_caracter_especial_colunas": ['ALL'], 
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_briefing_segmento": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/118662734653797623"],
                            "briefingagendaid_briefing_segmento": ["STRING", '[RESTRICT] Alert! Description pending with the base manager.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/118662734653797623"],
                            "segmentomercadoid_briefing_segmento": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/118662734653797623"],
                            "hds_briefing_segmento": ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/118662734653797623"]}
       },
        "historico_mes_funcionario":
       {           
           "renomear_tables": 'historico_mes_funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_historico_mes_funcionario": ["STRING", "[RESTRICT] line id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3725795255337936501"],
                            "mes_historico_mes_funcionario": ["DATETIME", "[RESTRICT] Reference month","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3725795255337936501"]}
       },
       "log_status_frente":
       {
           "renomear_tables": 'log_status_frente_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['DataInclusao', '%Y-%m-%d %H:%M:%S.%f'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_log_status_frente": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7206886118347010791"],
                            "frenteid_log_status_frente": ["STRING", '[RESTRICT] Alert! Description pending with the base manager',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7206886118347010791"],
                            "statusanteriorid_log_status_frente": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7206886118347010791"],
                            "statusatualid_log_status_frente": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7206886118347010791"],
                            "usuarioinclusao_log_status_frente": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7206886118347010791"],
                            "datainclusao_log_status_frente": ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7206886118347010791"]} 

       },

       "agenda":
       {
           "renomear_tables": 'agenda_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao',
                               'CustoVendido', 'AgendaVendidaOriginalId', 'DataEquipeFormada', 'DataSugestao', 'DataResposta'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_agenda": ["STRING", "[RESTRICT] schedule id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3272325289979804056"],
                            "gerareceita_agenda": ["STRING", '[RESTRICT] Returns information whether the schedule generates revenue or not',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3272325289979804056"],
                            "tipoagendaid_agenda": ["STRING", "[RESTRICT] By code, it returns the type of agenda (consulting, in training, etc.)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3272325289979804056"],
                            "cargoid_agenda": ["STRING", "[RESTRICT] By code, it returns the information of the consultant's position","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3272325289979804056"],
                            "funcaoid_agenda": ["STRING", "[RESTRICT] By code, it returns the consultant's role information","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3272325289979804056"],
                            "funcionarioid_agenda": ["STRING", "[RESTRICT] By code, it returns the name of the consultant","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3272325289979804056"],
                            "frenteid_agenda": ["STRING", "[RESTRICT] By code, it returns the name of the front","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3272325289979804056"],
                            "status_agenda": ["STRING", "[RESTRICT] Front status (whether it is in progress, completed, etc.)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3272325289979804056"]}

       },

       "agenda_confirmada":
       {      
           "renomear_tables": 'agenda_confirmada_hub',  
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Dia', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao',
                               'HoraInicial', 'FrenteTemporariaId', 'Autonoma'],
           "remover_caracter_especial_colunas": ['ALL'], 
           "ingestion_models": 'full_load',

           "filtrar_colunas": {"id_agenda_confirmada": ["STRING", "[RESTRICT] Confirmed schedule id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "dia_agenda_confirmada": ["DATETIME", '[RESTRICT] Day on which the HD was registered in the agenda',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "hds_agenda_confirmada": ["STRING", "[RESTRICT] Number of HDs","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "agendaid_agenda_confirmada": ["STRING", "[RESTRICT] By code, it returns whose agenda it is","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "cidadeid_agenda_confirmada": ["STRING", "[RESTRICT] By code, it returns the city in which the HD was registered","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "solucaoid_agenda_confirmada": ["STRING", "[RESTRICT] By code, it returns the solution related to the registered HD","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "classeagenda_agenda_confirmada": ["STRING", "[RESTRICT] Association by class_front, returns the type of agenda registered","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "tipoagendaconfirmada_agenda_confirmada": ["STRING", "[RESTRICT] Schedule type (consulting, in training, etc)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "alternativaescolhidaid_agenda_confirmada": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "excluido_agenda_confirmada": ["STRING", "[RESTRICT] Returns whether the HD was deleted or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "participataxaocupacao_agenda_confirmada": ["STRING", "[RESTRICT] Returns whether or not the schedule participates in the TO","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"],
                            "homeoffice_agenda_confirmada": ["STRING", "[RESTRICT] Returns whether the HD was registered as a home office or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9066506132672516520"]}
       },
       "agenda_confirmada_vazia":
       {         
           "renomear_tables": 'agenda_confirmada_vazia_hub',          
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Dia', '%Y-%m-%d %H:%M:%S.%f'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_agenda_confirmada_vazia": ["STRING", "[RESTRICT] Empty confirmed schedule id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041776495870733373"],
                            "dia_agenda_confirmada_vazia": ["DATETIME", '[RESTRICT] Day the HD was registered in the agenda.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041776495870733373"],
                            "hds_agenda_confirmada_vazia": ["STRING", "[RESTRICT] Number of HDs.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041776495870733373"],
                            "funcionarioid_agenda_confirmada_vazia": ["STRING", "[RESTRICT] Id of the employee who owns the confirmed empty schedule.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041776495870733373"],
                            "cargoid_agenda_confirmada_vazia": ["STRING", "[RESTRICT] Id of the role to which the empty confirmed schedule belongs.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041776495870733373"]}
       },
       "agenda_mensal":
       { 
           "renomear_tables": 'agenda_mensal_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['MesCalendario', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_agenda_mensal": ["STRING", "[RESTRICT] monthly schedule id.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/394430079715929049"],
                            "mes_agenda_mensal": ["STRING", '[RESTRICT] reference month.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/394430079715929049"],
                            "hd_agenda_mensal": ["STRING", "[RESTRICT] Number of HDs registered in the month.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/394430079715929049"],
                            "agendaid_agenda_mensal": ["STRING", "[RESTRICT] By code, it returns the agenda information.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/394430079715929049"],
                            "mescalendario_agenda_mensal": ["DATETIME", "[RESTRICT] Corresponding month and year.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/394430079715929049"],
                            "hdrascunho_agenda_mensal": ["STRING", "[RESTRICT] HD not released yet.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/394430079715929049"]}
       },
       "associacao_tipo_agenda":
       {
           "renomear_tables": 'associacao_tipo_agenda_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao',
                               'GeraReceita', 'Padrao'],
           "remover_caracter_especial_colunas": ['ALL'], 
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_associacao_tipo_agenda": ["STRING", "[RESTRICT] line id.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5651030302337547029"],
                            "tipoagendaid_associacao_tipo_agenda": ["STRING", '[RESTRICT] By code, it returns the type of agenda (consulting, in training, etc.)',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5651030302337547029"],
                            "tipofrenteid_associacao_tipo_agenda": ["STRING", "[RESTRICT] By code, it returns the front type (inner, etc)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5651030302337547029"],
                            "classefrenteid_associacao_tipo_agenda": ["STRING", "[RESTRICT] By code, it returns the front class (tower, commercial, etc)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5651030302337547029"]}
       },
       "briefing":
       {
           "renomear_tables": 'briefing_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "transforma_decimal": ['TipoRegiaoAtuacao','PesoCargo','PesoIdioma','PesoLideranca','PesoSolucao','PesoSegmento','PesoCompetencia','Categoria','PesoConhecimentoEspecifico'],
           "remover_caracter_especial_colunas": ['ALL'], 
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "frenteid_briefing": ["STRING", '[RESTRICT] Alert! Description pending with the base manager.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "observacao_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "previsaoinicio_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "tiporegiaoatuacao_briefing": ["FLOAT", '[RESTRICT] Alert! Description pending with the base manager.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "exterior_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "pesocargo_briefing": ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "pesoidioma_briefing": ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "pesolideranca_briefing": ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "pesosolucao_briefing": ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "pesosegmento_briefing": ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "pesocompetencia_briefing": ["FLOAT", '[RESTRICT] Alert! Description pending with the base manager.',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "tipologistica_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "escopo_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "caracteristicacliente_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "categoria_briefing": ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "enviadopelosocio_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "pesoconhecimentoespecifico_briefing": ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "localatuacaoid_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "informacoesrelevantesmobilidade_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "tiponacionalidadefrente_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],                            
                            "projetopublico_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"],
                            "renovacao_briefing": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/389222330701364496"]}
       },
       "cargo":
       {
           "renomear_tables": 'cargo_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_cargo": ["STRING", "[RESTRICT] Job id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "codigo_cargo": ["STRING", '[RESTRICT] Job code',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "nome_cargo": ["STRING", "[RESTRICT] Job title","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "ativo_cargo": ["STRING", "[RESTRICT] If the position is active in the base","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "hierarquia_cargo": ["STRING", "[RESTRICT] Job hierarchy","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "cargopaiid_cargo": ["STRING", "[RESTRICT] Parent job id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "cargoreclassificacao_cargo": ["STRING", "[RESTRICT] Reclassification position","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "cargoequivalenteid_cargo": ["STRING", "[RESTRICT] Equivalent job id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "participataxaocupacao_cargo": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "custohd_cargo": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "nomeingles_cargo": ["STRING", "[RESTRICT] English job title","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "nomeespanhol_cargo": ["STRING", "[RESTRICT] Name of thistle in spanish","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "gerareceita_cargo": ["STRING", "[RESTRICT] Pending.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"],
                            "altahierarquia_cargo": ["STRING", "[RESTRICT] Pending.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2984149350646757355"]}
       },
       "carteira":
       {
           "renomear_tables": 'carteira_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_carteira": ["STRING", "[RESTRICT] Wallet id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1706436497597324450"],
                            "nome_carteira": ["STRING", '[RESTRICT] Wallet name',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1706436497597324450"],
                            "icone_carteira": ["STRING", "[RESTRICT] Wallet icon (image)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1706436497597324450"],
                            "modelodenegocioid_carteira": ["STRING", "[RESTRICT] Id of the business model to which the wallet belongs","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1706436497597324450"],
                            "modelonegocioid_carteira": ["STRING", "[RESTRICT] Id of the business model to which the wallet belongs","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1706436497597324450"],
                            "codigo_carteira": ["STRING", "[RESTRICT] Wallet code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1706436497597324450"],
                            "nomeingles_carteira": ["STRING", "[RESTRICT] Wallet name in English","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1706436497597324450"],
                            "nomeespanhol_carteira": ["STRING", "[RESTRICT] Portfolio name in spanish","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1706436497597324450"]}
       },
       "carteira_funcionario":
       {
           "renomear_tables": 'carteira_funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_carteira_funcionario": ["STRING", "[RESTRICT] Line id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1456836283818071577"],
                            "carteiraid_carteira_funcionario": ["STRING", '[RESTRICT] By code, it returns the name of the wallet',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1456836283818071577"],
                            "funcionarioid_carteira_funcionario": ["STRING", "[RESTRICT] By code, it returns the name of the employee","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1456836283818071577"]}
       },
       "cidadania":
       {
           "renomear_tables": 'cidadania_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_cidadania": ["STRING", "[RESTRICT] Citizenship id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7747648771086438942"],
                            "funcionarioid_cidadania": ["STRING", '[RESTRICT] By code, it returns the name of the employee',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7747648771086438942"],
                            "paisid_cidadania": ["STRING", "[RESTRICT] By code, it returns the country of the employee","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7747648771086438942"]}
       },
       "cidade":
       {
           "renomear_tables": 'cidade_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_cidade": ["STRING", "[RESTRICT] City id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1752467592977330068"],
                            "nome_cidade": ["STRING", "[RESTRICT] City's name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1752467592977330068"],
                            "estadoid_cidade": ["STRING", "[RESTRICT] By code, it returns the name of the state","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1752467592977330068"],
                            "paisid_cidade": ["STRING", "[RESTRICT] By code, it returns the name of the country","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1752467592977330068"],
                            "ativo_cidade": ["STRING", "[RESTRICT] Whether the city is active or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1752467592977330068"],
                            "codigo_cidade": ["STRING", "[RESTRICT] City ​​code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1752467592977330068"],
                            "nomeingles_cidade": ["STRING", "[RESTRICT] City ​​name in english","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1752467592977330068"],
                            "nomeespanhol_cidade": ["STRING", "[RESTRICT] City name in spanish","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1752467592977330068"]}
       },
       "cidade_frente":
       {
           "renomear_tables": 'cidade_frente_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_cidade_frente": ["STRING", "[RESTRICT] Line id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8380920951988814202"],
                            "cidadeid_cidade_frente": ["STRING", '[RESTRICT] By code, it returns the name of the city',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8380920951988814202"],
                            "frenteid_cidade_frente": ["STRING", "[RESTRICT] By code, return forward","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8380920951988814202"],
                            "ativo_cidade_frente": ["STRING", "[RESTRICT] Whether it is active or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8380920951988814202"]}
       },
       "classe_frente":
       {
           "renomear_tables": 'classe_frente_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_classe_frente": ["STRING", "[RESTRICT] front class id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6455740708867456372"],
                            "codigo_classe_frente": ["STRING", '[RESTRICT] front class code',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6455740708867456372"],
                            "nome_classe_frente": ["STRING", "[RESTRICT] Front class name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6455740708867456372"],
                            "tipofrenteid_classe_frente": ["STRING", "[RESTRICT] By code, it returns the front type (inner, etc)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6455740708867456372"],
                            "terceiro_classe_frente": ["STRING", "[RESTRICT] Says if it's third party or not. This table shows which registration the consultant has autonomy to register (does not need to be released by FE)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6455740708867456372"],
                            "nomeingles_classe_frente": ["STRING", "[RESTRICT] English front class name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6455740708867456372"],
                            "nomeespanhol_classe_frente": ["STRING", "[RESTRICT] Front class name in spanish","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6455740708867456372"]}
       },
       "cliente":
       {
           "renomear_tables": 'cliente_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_cliente": ["STRING", "[RESTRICT] Front class id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "codigo_cliente": ["STRING", '[RESTRICT] Front class code',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "nomefantasia_cliente": ["STRING", "[RESTRICT] Front class name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "razaosocial_cliente": ["STRING", "[RESTRICT] By code, it returns the front type (inner, etc)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "cnpj_cliente": ["STRING", "[RESTRICT] Says if it's third party or not. This table shows which registration the consultant has autonomy to register (does not need to be released by FE)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "porte_cliente": ["STRING", "[RESTRICT] Customer size","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "segmentoprimario_cliente": ["STRING", "[RESTRICT] Primary customer segment","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "segmentosecundario_cliente": ["STRING", "[RESTRICT] Front class id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "segmentoterciario_cliente": ["STRING", '[RESTRICT] front class code',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "cidadeid_cliente": ["STRING", "[RESTRICT] Front class name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "ativo_cliente": ["STRING", "[RESTRICT] By code, it returns the front type (inner, etc)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "logo_cliente": ["STRING", "[RESTRICT] Says if it's third party or not. This table shows which registration the consultant has autonomy to register (does not need to be released by FE)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "grupoeconomicoid_cliente": ["STRING", "[RESTRICT] By code, it returns the customer's economic group","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "segmentoprimarioid_cliente": ["STRING", "[RESTRICT] Defines the client's primary thread code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "segmentosecundarioid_cliente": ["STRING", "[RESTRICT] Defines the client's secondary thread code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "segmentoterciarioid_cliente": ["STRING", "[RESTRICT] Defines the customer's tertiary segment code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "hashlogo_cliente": ["STRING", "[RESTRICT] Customer logo","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "falconi_cliente": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"],
                            "hashimagem_cliente": ["STRING", "[RESTRICT] Customer picture","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7872451594470612947"]}
       },
       "custo_hd_funcionario":
       {
           "renomear_tables": 'custo_hd_funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['DataVigencia', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_custo_hd_funcionario": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1284623701960302872"],
                            "custo_custo_hd_funcionario": ["STRING", '[RESTRICT] Alert! Description pending with the base manager',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1284623701960302872"],
                            "datavigencia_custo_hd_funcionario": ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1284623701960302872"],
                            "funcionarioid_custo_hd_funcionario": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1284623701960302872"],
                            "frenteid_custo_hd_funcionario": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1284623701960302872"]}
       },
       "custo_cargo":
       {
           "renomear_tables": 'custo_cargo_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['InicioVigencia', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_custo_cargo": ["STRING", "[RESTRICT] Job cost id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7435194408242914819"],
                            "iniciovigencia_custo_cargo": ["DATETIME", '[RESTRICT] Beginning of the term of the cost of the position',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7435194408242914819"],
                            "custo_custo_cargo": ["STRING", "[CONFIDENTIAL] Cost of the post","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7435194408242914819"],
                            "cargoid_custo_cargo": ["STRING", "[RESTRICT] Job title","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7435194408242914819"],
                            "tipocusto_custo_cargo": ["STRING", "[RESTRICT] Cost type","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7435194408242914819"]}
       },
       "disponibilidade_taxa_ocupacao_estatico":
       {
           "renomear_tables": 'disponibilidade_taxa_ocupacao_estatico_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "transforma_decimal": ['HdsDisponiveis'],           
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_disponibilidade_taxa_ocupacao_estatico": ["STRING", "[RESTRICT] Job cost id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8323904584991410127"],
                            "mes_disponibilidade_taxa_ocupacao_estatico": ["DATETIME", '[RESTRICT] Beginning of the term of the cost of the position',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8323904584991410127"],
                            "carteiraid_disponibilidade_taxa_ocupacao_estatico": ["STRING", "[RESTRICT] Cost of the post","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8323904584991410127"],
                            "hdsdisponiveis_disponibilidade_taxa_ocupacao_estatico": ["FLOAT", "[RESTRICT] Job title","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8323904584991410127"],
                            "cargoid_disponibilidade_taxa_ocupacao_estatico": ["STRING", "[RESTRICT] Cargo ID","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8323904584991410127"]}
       },
       "departamento":
       {
           "renomear_tables": 'departamento_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_departamento": ["STRING", "[RESTRICT] Department id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041830718995089383"],
                            "codigo_departamento": ["STRING", '[RESTRICT] Department code',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041830718995089383"],
                            "nome_departamento": ["STRING", "[RESTRICT] Department name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041830718995089383"],
                            "nomeingles_departamento": ["STRING", "[RESTRICT] English name of the department","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041830718995089383"],
                            "nomeespanhol_departamento": ["STRING", "[RESTRICT] Department name in Spanish","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5041830718995089383"]}
       },
       "desempenho_funcionario":
       {
           "renomear_tables": 'desempenho_funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['DataAplicacao', '%Y-%m-%d %H:%M:%S.%f'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "filtrar_colunas": {"id_desempenho_funcionario": ["STRING", "[INTERN] Line id", "projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2291969039681453929" ],
                            "funcionarioid_desempenho_funcionario": ["STRING", '[RESTRICT] By code, returns the employee', "projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2291969039681453929" ],
                            "dataaplicacao_desempenho_funcionario": ["DATETIME", "[CONFIDENTIAL] Box application date", "projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2291969039681453929" ],
                            "box_desempenho_funcionario": ["STRING", "[CONFIDENTIAL] Box where the employee is located", "projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2291969039681453929" ]}
       },
       "disponibilidade_funcionario":
       {           
           "renomear_tables": 'disponibilidade_funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_disponibilidade_funcionario": ["STRING", "[RESTRICT] line id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/613315136896521472"],
                            "funcionarioid_disponibilidade_funcionario": ["STRING", '[RESTRICT] By code, returns employee information',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/613315136896521472"],
                            "hdsdisponiveis_disponibilidade_funcionario": ["STRING", "[RESTRICT] Available HDs of the month","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/613315136896521472"],
                            "mes_disponibilidade_funcionario": ["DATETIME", "[RESTRICT] Reference month","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/613315136896521472"]}
       },
       "empresa":
       {
           "renomear_tables": 'empresa_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_empresa": ["STRING", "[RESTRICT] Company id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8289439411960221617"],
                            "codigo_empresa": ["STRING", '[RESTRICT] Company code',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8289439411960221617"],
                            "nome_empresa": ["STRING", "[RESTRICT] Falconi group company name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8289439411960221617"],
                            "codigoticket_empresa": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8289439411960221617"],
                            "codigolabore_empresa": ["STRING", "[RESTRICT] Alert! Description pending with the base manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8289439411960221617"],
                            "pool_empresa": ["STRING", "[RESTRICT] Says whether the company participates in the pool or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8289439411960221617"],
                            "codigoempresaresumido_empresa": ["STRING", "[RESTRICT] Company code and name together","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8289439411960221617"],
                            "nomelegaloracle_empresa": ["STRING", "[RESTRICT] Legal company name in oracle","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/8289439411960221617"]}
       },
       "estado":
       { 
           "renomear_tables": 'estado_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_estado": ["STRING", "[RESTRICT] State id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5171632329584886581"],
                            "nome_estado": ["STRING", '[RESTRICT] State name',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5171632329584886581"],
                            "paisid_estado": ["STRING", "[RESTRICT] By code, it returns the name of the country","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5171632329584886581"],
                            "codigo_estado": ["STRING", "[RESTRICT] State code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5171632329584886581"],
                            "nomeingles_estado": ["STRING", "[RESTRICT] State name in English","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5171632329584886581"],
                            "nomeespanhol_estado": ["STRING", "[RESTRICT] State name in spanish","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5171632329584886581"]}
       },
       "frente":
       {
           "renomear_tables": 'frente_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_frente": ["STRING", "[RESTRICT] Front id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "codigo_frente": ["STRING", "[RESTRICT] front code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nome_frente": ["STRING", "[CONFIDENTIAL] front name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "codigoprojeto_frente": ["STRING", "[RESTRICT] project code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nomeprojeto_frente": ["STRING", "[CONFIDENTIAL] Project name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "codigoproposta_frente": ["STRING", "[RESTRICT] Commercial proposal code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nomeproposta_frente": ["STRING", "[CONFIDENTIAL] Business proposal name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "codigotipofrente_frente": ["STRING", "[RESTRICT] Front type code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nometipofrente_frente": ["STRING", "[RESTRICT] Front type name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "codigoclassefrente_frente": ["STRING", "[RESTRICT] front class code","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nomeclassefrente_frente": ["STRING", "[RESTRICT] Front class name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "sociodiretor_frente": ["STRING", "[CONFIDENTIAL] portfolio head partner","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "lidernivel2_frente": ["STRING", "[CONFIDENTIAL] Level 2 Leader (Partner)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "datainicio_frente": ["STRING", "[RESTRICT] Project start date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "duracao_frente": ["STRING", "[RESTRICT] Project duration","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "dataassinaturacontrato_frente": ["STRING", "[RESTRICT] Contract signing date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "datatermoaceite_frente": ["STRING", "[RESTRICT] Acceptance term date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "valorequipevendida_frente": ["STRING", "[CONFIDENTIAL] Value of team sold","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "dataautorizacaodiretoria_frente": ["STRING", "[RESTRICT] Board authorization date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "statusid_frente": ["STRING", "[RESTRICT] Front status (in progress, completed, etc)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "solucaoid_frente": ["STRING", "[RESTRICT] Project related solution","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "empresaid_frente": ["STRING", "[RESTRICT] Group company to which the project belongs","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "lidernivel3_frente": ["STRING", "[CONFIDENTIAL] Level 3 leader (GP)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "lidernivel4_frente": ["STRING", "[CONFIDENTIAL] Level 4 Leader (Leader)","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nomefrenteoriginal_frente": ["STRING", "[CONFIDENTIAL] Original front name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "valorpropostacomercial_frente": ["STRING", "[CONFIDENTIAL] Value of the commercial proposal","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "clienteid_frente": ["STRING", "[RESTRICT] By code, it returns the name of the customer","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "cidadebaseid_frente": ["STRING", "[RESTRICT] By code, it returns the base city of the project","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "valorequipeformada_frente": ["STRING", "[CONFIDENTIAL] Value of formed team","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "ativo_frente": ["STRING", "[RESTRICT] Returns whether the front is active or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "tipofrenteid_frente": ["STRING", "[RESTRICT] front type","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "classefrenteid_frente": ["STRING", "[RESTRICT] front class","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "temporario_frente": ["STRING", "[RESTRICT] Returns whether it is a temporary front or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "dataassociacaovenda_frente": ["STRING", "[RESTRICT] Sale association date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "frenteassociada_frente": ["STRING", "[RESTRICT] The name of the associated front","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nomeclientevenda_frente": ["STRING", "[CONFIDENTIAL] Sales customer name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "dataequipeformada_frente": ["STRING", "[RESTRICT] Formed team date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "dataequipevendida_frente": ["STRING", "[RESTRICT] Team sold date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "valorequipeativagolive_frente": ["STRING", "[CONFIDENTIAL] Active team value","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "valorequipeatual_frente": ["STRING", "[CONFIDENTIAL] Current team value","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "dataliberacaoequipe_frente": ["STRING", "[RESTRICT] Date the team was released","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "responsavelformacaoequipe_frente": ["STRING", "[RESTRICT] Team Building Manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "equipeformada_frente": ["STRING", "[RESTRICT] Returns whether the team is formed or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "notificacaobriefingenviada_frente": ["STRING", "[RESTRICT] Returns whether the briefing completion notification was sent","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "porte_frente": ["STRING", "[RESTRICT] Project size","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "rankingfrenteid_frente": ["STRING", "[RESTRICT] front ranking","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "carteiraid_frente": ["STRING", "[RESTRICT] Portfolio in which the project is included","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "criticidade_frente": ["STRING", "[RESTRICT] Project criticality","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "novadatainicio_frente": ["STRING", "[RESTRICT] New project start date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "keyaccount_frente": ["STRING", "[RESTRICT] Returns if the project is keyaccount","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "renovacao_frente": ["STRING", "[RESTRICT] Returns if it is a renovation project","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "categoria_frente": ["STRING", "[RESTRICT] project category","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "tipoprojetoid_frente": ["STRING", "[RESTRICT] By code, it returns the type of the project","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "frenterenovacaoid_frente": ["STRING", "[RESTRICT] By code, it returns the renewed front","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nometipofrenteingles_frente": ["STRING", "[RESTRICT] English front type name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nometipofrenteespanhol_frente": ["STRING", "[RESTRICT] Front type name in spanish","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nomeclassefrenteingles_frente": ["STRING", "[RESTRICT] English front class name","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "nomeclassefrenteespanhol_frente": ["STRING", "[RESTRICT] Front class name in spanish","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "datafim_frente": ["STRING", "[RESTRICT] front end date","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "equipeformadaconcluida_frente": ["STRING", "[RESTRICT] Alert! Description pending with the base manager.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "datainiciofinanceiro_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "datafimfinanceiro_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "intercompany_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "intercompanynumero_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"],
                        "sucessfee_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5263153116545307653"]}
        },
       "frente_movimentacao":
       {
           "renomear_tables": 'frente_movimentacao_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao',
                               'JustificativaId'],
           "transforma_decimal": ['Valor'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {"id_frente_movimentacao": ["STRING", "[RESTRICT] Front drive id","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1813771020619086267"],
                            "frenteid_frente_movimentacao": ["STRING", '[RESTRICT] By code, return forward',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1813771020619086267"],
                            "valor_frente_movimentacao": ["FLOAT", "[RESTRICT] Busy front value","projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1813771020619086267"],
                            "observacao_frente_movimentacao": ["STRING", '[RESTRICT] Alert! Description pending with the base manager',"projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1813771020619086267"]}
       },

       "funcao":
       {
           "renomear_tables": 'funcao_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_funcao' : ["STRING", "[RESTRICT] role id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5562400351786652203'],
                    'codigo_funcao': ["STRING","[RESTRICT] function code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5562400351786652203'],
                    'nome_funcao': ["STRING","[RESTRICT] role name", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5562400351786652203'],
                    'ativo_funcao' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5562400351786652203'],
                    'hierarquia_funcao': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5562400351786652203'],
                    'adicional_funcao': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5562400351786652203'],
                    'nomeingles_funcao' : ["STRING", "[RESTRICT] Function name in English", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5562400351786652203'],
                    'nomeespanhol_funcao': ["STRING","[RESTRICT] Function name in spanish", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5562400351786652203']}
       },

       "funcionario":
       { 
           "renomear_tables": 'funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['DataAdmissao', 'DataDesligamento', 'DataNascimento','DataPrevisaoReclassificacao', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao',
                               'Nome', 'Login', 'CPF', 'RG', 'EmissorRG', 'TelefoneComercial', 'Celular',
                               'CodigoPostal', 'Imagem', 'MeioPeriodo', 'EmailPessoal', 'DataCasamento', 'ValeRefeicao',
                               'ValeAlimentacao', 'Mae', 'Pai', 'Conjuge', 'EnderecoBase', 'TelefoneResidencial', 'CelularPessoal',
                               'TipoDesligamento', 'DataUltimaIntegracao', 'SaldoFerias',
                               'DataLimiteFerias', 'HashImagem','DepartamentoHcm', 'DataInicioHcm', 'EmpresaHcm',
                               'TerceiroHcm', 'EmpresaIdHcm', 'Linkedin'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_funcionario' : ["STRING", "[RESTRICT] employee id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'codigo_funcionario': ["STRING","[RESTRICT] consultant code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'nomecompleto_funcionario': ["STRING","[CONFIDENTIAL] Consultant's full name", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'email_funcionario' : ["STRING", "[RESTRICT] The employee's email", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'perfil_funcionario': ["STRING","[RESTRICT] If the consultant is from the consultancy, third party, etc.", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'departamento_funcionario': ["STRING","[RESTRICT] Consultant's department (if he is part of the board, is a partner, etc.)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'dataadmissao_funcionario' : ["DATETIME", "[RESTRICT] Employee hire date", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'status_funcionario': ["STRING","[RESTRICT] Status on the employee in the system (active or inactive)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'datadesligamento_funcionario' : ["DATETIME", "[RESTRICT] Employee termination date", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'datanascimento_funcionario': ["DATETIME","[CONFIDENTIAL] Consultant's date of birth", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'sexo_funcionario': ["STRING","[RESTRICT] consultant's gender", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'estadocivil_funcionario' : ["STRING", "[RESTRICT] What is the civil status of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'nacionalidade_funcionario': ["STRING","[RESTRICT] Consultant's nationality", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'dataprevisaoreclassificacao_funcionario': ["DATETIME","[CONFIDENTIAL] Reclassification forecast date", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'cargoid_funcionario' : ["STRING", "[RESTRICT] Consultant's position", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'empresaid_funcionario': ["STRING","[RESTRICT] Company of the group of which the consultant is part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'cidadeid_funcionario' : ["STRING", "[RESTRICT] consultant's city", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'participataxaocupacao_funcionario': ["STRING","[RESTRICT] Whether the consultant participates in the T.O or not", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'codigochapa_funcionario' : ["STRING", "[RESTRICT] Consultant plate code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'interesseatuacaoforabase_funcionario': ["STRING","[RESTRICT] Interest in working outside the base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'interesseatuacaoexterior_funcionario': ["STRING","[RESTRICT] Interest in working abroad", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'box_funcionario' : ["STRING", "[CONFIDENTIAL] consultant's box", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'naturalidadeid_funcionario': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'nacionalidadeid_funcionario': ["STRING","[RESTRICT] Consultant's nationality", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'falconigente_funcionario' : ["STRING", "[RESTRICT] Whether the consultant is part of Falconi Gente or not", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'empresataxaocupacaoid_funcionario': ["STRING","[RESTRICT] Company id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'uniqueid_funcionario': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'instagram_funcionario': ["STRING","[RESTRICT] Employee instagram address", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'carteiraid_funcionario': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901'],
                    'superadmin_funcionario': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1749641489518224901']}
       },
       "funcionario_mes_sem_atuacao":
       {
           "renomear_tables": 'funcionario_mes_sem_atuacao_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['DataInicio', 'DataFim', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_funcionario_mes_sem_atuacao' : ["STRING", "[RESTRICT] line id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2107295898765752121'],
                    'funcionarioid_funcionario_mes_sem_atuacao': ["STRING","[RESTRICT] By code, it returns the name of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2107295898765752121'],
                    'hd_funcionario_mes_sem_atuacao': ["STRING","[RESTRICT] Number of non-working HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2107295898765752121'],
                    'datainicio_funcionario_mes_sem_atuacao' : ["DATETIME", "[RESTRICT] Registration start date", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2107295898765752121'],
                    'datafim_funcionario_mes_sem_atuacao': ["DATETIME","[RESTRICT] Registration end date", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2107295898765752121']}
       },

       "funcionario_participa_pool_mes":
       {
           "renomear_tables": 'funcionario_participa_pool_mes_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_funcionario_participa_pool_mes' : ["STRING", "[RESTRICT] Line ID", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1055275497839509166'],
                    'mes_funcionario_participa_pool_mes': ["DATETIME","[RESTRICT] Reference month, returns the name of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1055275497839509166'],
                    'participataxaocupacao_funcionario_participa_pool_mes': ["STRING","[RESTRICT] Returns whether or not the employee participates in the T.O", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1055275497839509166'],
                    'funcionarioid_funcionario_participa_pool_mes' : ["STRING", "[RESTRICT] By code, it returns the name of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1055275497839509166']}
       },
       "negocio":
       {
           "renomear_tables": 'negocio_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_negocio' : ["STRING", "[RESTRICT] business id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5965721494767496533'],
                    'codigo_negocio': ["STRING","[RESTRICT] business code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5965721494767496533'],
                    'nome_negocio': ["STRING","[RESTRICT] business name", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5965721494767496533'],
                    'nomeingles_negocio' : ["STRING", "[RESTRICT] Business name in english", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5965721494767496533'],
                    'nomeespanhol_negocio' : ["STRING", "[RESTRICT] Business name in spanish", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5965721494767496533']}
       },
       "pais":
       {
           "renomear_tables": 'pais_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_pais' : ["STRING", "[RESTRICT] country id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4590067281143094467'],
                    'nome_pais': ["STRING","[RESTRICT] Name of the country", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4590067281143094467'],
                    'codigo_pais': ["STRING","[RESTRICT] country code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4590067281143094467'],
                    'nomeingles_pais' : ["STRING", "[RESTRICT] Country name in English", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4590067281143094467'],
                    'nomeespanhol_pais' : ["STRING", "[RESTRICT] Country name in spanish", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4590067281143094467']}
       },
       "preferencia_negocio_funcionario":
       {
           "renomear_tables": 'preferencia_negocio_funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_preferencia_negocio_funcionario' : ["STRING", "[RESTRICT] business id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2266130543831482294'],
                    'preferencia_preferencia_negocio_funcionario': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2266130543831482294'],
                    'negocioid_preferencia_negocio_funcionario': ["STRING","[RESTRICT] business code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2266130543831482294'],
                    'funcionarioid_preferencia_negocio_funcionario' : ["STRING", "[RESTRICT] By code, it returns employee information", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2266130543831482294']}
       },
       "reclassificacao":
       {
           "renomear_tables": 'reclassificacao_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_reclassificacao' : ["STRING", "[RESTRICT] line id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5664841467550470210'],
                    'mes_reclassificacao': ["DATETIME","[RESTRICT] reference month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5664841467550470210'],
                    'quantidade_reclassificacao': ["STRING","[CONFIDENTIAL] Number of reclassifications", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5664841467550470210'],
                    'baseid_reclassificacao' : ["STRING", "[RESTRICT] By code, it returns the base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5664841467550470210'],
                    'cargoid_reclassificacao' : ["STRING", "[RESTRICT] By code, returns the charge", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5664841467550470210'],
                    'empresaid_reclassificacao' : ["STRING", "[RESTRICT] By code, it returns the company of the group (MID, People)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5664841467550470210']}
       },
       "segmento_mercado":
       {
           "renomear_tables": 'segmento_mercado_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_segmento_mercado' : ["STRING", "[RESTRICT] segment id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3024716787939391516'],
                    'codigo_segmento_mercado': ["STRING","[RESTRICT] Market segment code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3024716787939391516'],
                    'nome_segmento_mercado': ["STRING","[RESTRICT] Market segment name", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3024716787939391516'],
                    'hdminimo_segmento_mercado' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3024716787939391516'],
                    'nomeingles_segmento_mercado' : ["STRING", "[RESTRICT] Industry name in English", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3024716787939391516'],
                    'nomeespanhol_segmento_mercado' : ["STRING", "[RESTRICT] Market segment name in Spanish", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3024716787939391516']}
       },
       "solucao":
       {
           "renomear_tables": 'solucao_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_solucao' : ["STRING", "[RESTRICT] solution id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6073590438537013029'],
                    'codigo_solucao': ["STRING","[RESTRICT] solution code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6073590438537013029'],
                    'nome_solucao': ["STRING","[RESTRICT] solution name", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6073590438537013029'],
                    'venda_solucao' : ["STRING", "[RESTRICT] Says if the solution is for sale or not", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6073590438537013029'],
                    'hdminimo_solucao' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6073590438537013029'],
                    'ativo_solucao' : ["STRING", "[RESTRICT] Returns whether the solution is active or not", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6073590438537013029'],
                    'nomeingles_solucao' : ["STRING", "[RESTRICT] English solution name", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6073590438537013029'],
                    'nomeespanhol_solucao' : ["STRING", "[RESTRICT] Spanish solution name", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6073590438537013029']}
       },
       "solucao_frente":
       {
           "renomear_tables": 'solucao_frente_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_solucao_frente' : ["STRING", "[RESTRICT] line id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2941574552074077420'],
                    'frenteid_solucao_frente': ["STRING","[RESTRICT] By code, return forward", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2941574552074077420'],
                    'solucaoid_solucao_frente': ["STRING","[RESTRICT] By code, it returns the type of solution", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2941574552074077420'],
                    'ativo_solucao_frente' : ["STRING", "[RESTRICT] Returns whether it is active or not", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2941574552074077420']}
       },
       "status_frente":
       {
           "renomear_tables": 'status_frente_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_status_frente' : ["STRING", "[RESTRICT] front status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4912174961926312213'],
                    'codigo_status_frente': ["STRING","[RESTRICT] front status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4912174961926312213'],
                    'nome_status_frente': ["STRING","[RESTRICT] Front status (completed, in progress, etc)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4912174961926312213'],
                    'nomeingles_status_frente' : ["STRING", "[RESTRICT] front status in english", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4912174961926312213'],
                    'nomeespanhol_status_frente' : ["STRING", "[RESTRICT] front status in spanish", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4912174961926312213']}
       },
       "sugestao_funcionario":
       {
           "renomear_tables": 'sugestao_funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['DataVencimento', 'DataAnaliseLideranca', '%Y-%m-%d %H:%M:%S.%f'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao',
                               'ObservacaoFormacao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_sugestao_funcionario' : ["STRING", "[INTERN] Employee suggestion id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'agendaid_sugestao_funcionario': ["STRING","[INTERN] Employee Schedule ID", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'funcionariosugeridoid_sugestao_funcionario': ["STRING","[RESTRICT] Suggested Employee ID", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'responsavelformacaoid_sugestao_funcionario' : ["STRING", "[INTERN] Team Building Responsible ID", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'responsavelliderancaid_sugestao_funcionario' : ["STRING", "[INTERN] ID of the leader responsible for the approval", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'statussugestaofuncionarioid_sugestao_funcionario' : ["STRING", "[RESTRICT] Submitted suggestion status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'justificativarecusaid_sugestao_funcionario': ["STRING","[CONFIDENTIAL] By ID, it returns the reason for refusal", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'datavencimento_sugestao_funcionario': ["DATETIME","[INTERN] Suggestion expiration date", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'posicaoranking_sugestao_funcionario' : ["STRING", "[RESTRICT] Employee position in the suggestion ranking", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'notaranking_sugestao_funcionario' : ["STRING", "[RESTRICT] Employee score in suggestion ranking", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'dataanaliselideranca_sugestao_funcionario' : ["DATETIME", "[INTERN] Date leadership reviewed the suggestion", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'observacaolideranca_sugestao_funcionario': ["STRING","[CONFIDENTIAL] Note left by the leadership", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770'],
                    'dataenvioformacao_sugestao_funcionario': ["STRING","[CONFIDENTIAL] Note left by team building", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1520071093139517770']}
       },
       "taxa_ocupacao":
       {
           "renomear_tables": 'taxa_ocupacao_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_taxa_ocupacao' : ["STRING", "[RESTRICT] line id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'mes_taxa_ocupacao': ["DATETIME","[RESTRICT] reference month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdsdisponiveis_taxa_ocupacao': ["STRING","[RESTRICT] HDs available in the month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdsutilizados_taxa_ocupacao' : ["STRING", "[RESTRICT] HDs registered in the month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'baseid_taxa_ocupacao' : ["STRING", "[RESTRICT] Possibly returns the name of the base city", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'cargoid_taxa_ocupacao' : ["STRING", "[RESTRICT] By code, returns the charge", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'empresaid_taxa_ocupacao': ["STRING","[RESTRICT] By code, it returns the company of the group (MID, People)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdsexcessao_taxa_ocupacao': ["STRING","[RESTRICT] HDs of absences, notice or main function", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdstorre_taxa_ocupacao' : ["STRING", "[RESTRICT] HDs of intern projects", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdsvp_taxa_ocupacao' : ["STRING", "[RESTRICT] promotional visit HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdsprobono_taxa_ocupacao' : ["STRING", "[RESTRICT] HD's of pro bono projects", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdstreinamentointerno_taxa_ocupacao': ["STRING","[RESTRICT] internal training HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdstreinamentoexterno_taxa_ocupacao': ["STRING","[RESTRICT] external training hard drives", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdsprincipal_taxa_ocupacao' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdsprojetoexternaonaoprobono_taxa_ocupacao' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdssematuacao_taxa_ocupacao': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948'],
                    'hdscolabora_taxa_ocupacao': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2622964305584004948']}
       },
       "taxa_ocupacao_funcionario":
       {
           "renomear_tables": 'taxa_ocupacao_funcionario_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] line id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'mes_taxa_ocupacao_funcionario': ["DATETIME","[RESTRICT] reference month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdsdisponiveis_taxa_ocupacao_funcionario': ["STRING","[RESTRICT] HDs available in the month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdsutilizados_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] HDs registered in the agenda in the month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'funcionarioid_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] By code, it returns the name of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'baseid_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] By code, it returns the base of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'cargoid_taxa_ocupacao_funcionario': ["STRING","[RESTRICT] By code, returns the position of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'empresaid_taxa_ocupacao_funcionario': ["STRING","[RESTRICT] By code, it returns the company of the employee's group (MID, People, etc.)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdsexcessao_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] HDs of absences, notice or main function", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdstorre_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] HDs of internal projects", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdsvp_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] promotional visit HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdsprobono_taxa_ocupacao_funcionario': ["STRING","[RESTRICT] promotional visit HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdstreinamentointerno_taxa_ocupacao_funcionario': ["STRING","[RESTRICT] internal training HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdstreinamentoexterno_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] external training hard drives", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdsprincipal_taxa_ocupacao_funcionario' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdsprojetoexternaonaoprobono_taxa_ocupacao_funcionario': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdssematuacao_taxa_ocupacao_funcionario': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850'],
                    'hdscolabora_taxa_ocupacao_funcionario': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7425165406402587850']}
       },
       "taxa_ocupacao_carteira_estatico":
       {
           "renomear_tables": 'taxa_ocupacao_carteira_estatico_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "transforma_data": ['Mes', '%Y-%m-%d'],
           "transforma_decimal": ['HdsDisponiveis','HdsAprovados','HdsPrevistos','HdsEmAndamento','HdsExcessao','HdsTorre','HdsVp','HdsProBono','HdsTreinamentoInterno','HdsTreinamentoExterno','HdsPrincipal','HdsProjetoExternaoNaoProBono','HdsSemAtuacao',\
                                  'HdsColabora','HdsShortFridayNaoGeraReceita','HdsShortFridayGeraReceita'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_taxa_ocupacao_carteira_estatico' : ["STRING", "[RESTRICT] line id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'mes_taxa_ocupacao_carteira_estatico': ["DATETIME","[RESTRICT] reference month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'funcionarioid_taxa_ocupacao_carteira_estatico': ["STRING","[RESTRICT] HDs available in the month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'cargoid_taxa_ocupacao_carteira_estatico' : ["STRING", "[RESTRICT] HDs registered in the agenda in the month", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'carteiraid_taxa_ocupacao_carteira_estatico' : ["STRING", "[RESTRICT] By code, it returns the name of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsdisponiveis_taxa_ocupacao_carteira_estatico' : ["FLOAT", "[RESTRICT] By code, it returns the base of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsaprovados_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] By code, returns the position of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsprevistos_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] By code, it returns the company of the employee's group (MID, People, etc.)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsemandamento_taxa_ocupacao_carteira_estatico' : ["FLOAT", "[RESTRICT] HDs of absences, notice or main function", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsexcessao_taxa_ocupacao_carteira_estatico' : ["FLOAT", "[RESTRICT] HDs of internal projects", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdstorre_taxa_ocupacao_carteira_estatico' : ["FLOAT", "[RESTRICT] promotional visit HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsvp_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] promotional visit HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsprobono_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] internal training HDs", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdstreinamentointerno_taxa_ocupacao_carteira_estatico' : ["FLOAT", "[RESTRICT] external training hard drives", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdstreinamentoexterno_taxa_ocupacao_carteira_estatico' : ["FLOAT", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsprincipal_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsprojetoexternaonaoprobono_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdssematuacao_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdscolabora_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsshortfridaynaogerareceita_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216'],
                    'hdsshortfridaygerareceita_taxa_ocupacao_carteira_estatico': ["FLOAT","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/4076610119567698216']}
       },
       "tipo_agenda":
       {
           "renomear_tables": 'tipo_agenda_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_tipo_agenda' : ["STRING", "[RESTRICT] Calendar type id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1547020610453365662'],
                    'nome_tipo_agenda': ["STRING","[RESTRICT] Schedule type (consulting, in training, etc)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1547020610453365662'],
                    'codigo_tipo_agenda': ["STRING","[RESTRICT] Schedule type code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1547020610453365662'],
                    'nomeingles_tipo_agenda' : ["STRING", "[RESTRICT] English agenda type", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1547020610453365662'],
                    'nomeespanhol_tipo_agenda' : ["STRING", "[RESTRICT] Calendar Type in Spanish", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1547020610453365662']}
       },
       "tipo_frente":
       {
           "renomear_tables": 'tipo_frente_hub',
           "remove_linhas_duplicadas": ['ALL'],
           "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
           "remover_caracter_especial_colunas": ['ALL'],
           "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_tipo_frente' : ["STRING", "[RESTRICT] front type id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1708297495391517531'],
                    'codigo_tipo_frente': ["STRING","[RESTRICT] front type code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1708297495391517531'],
                    'nome_tipo_frente': ["STRING","[RESTRICT] Type of front (internal, consulting, etc.)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1708297495391517531'],
                    'nomeingles_tipo_frente' : ["STRING", "[RESTRICT] English front type", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1708297495391517531'],
                    'nomeespanhol_tipo_frente' : ["STRING", "[RESTRICT] front type in spanish", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/1708297495391517531']}
        },
       "atuacao_funcionario": 
	   {
		   "renomear_tables": 'atuacao_funcionario_hub',
		   "remove_linhas_duplicadas": ['ALL'],
		   "transforma_data": ['Mes', '%Y-%m-%d %H:%M:%S.%f'],
		   "transforma_decimal": ['HD'],
		   "remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
		   "remover_caracter_especial_colunas": ['ALL'],
		   "ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_atuacao_funcionario' : ["STRING", "[RESTRICT] Employee performance table id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522'],
                    'funcionarioid_atuacao_funcionario': ["STRING","[RESTRICT] By code, it returns the base of the employee", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522'],
                    'funcaoid_atuacao_funcionario': ["STRING","[RESTRICT] By code, returns the function base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522'],
                    'cidadeid_atuacao_funcionario' : ["STRING", "[RESTRICT] By code, it returns the city base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522'],
                    'segmentomercadoid_atuacao_funcionario' : ["STRING", "[RESTRICT] By code, returns market segment base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522'],
                    'solucaoid_atuacao_funcionario' : ["STRING", "[RESTRICT] By code, returns the base of solutions", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522'],
                    'clienteid_atuacao_funcionario': ["STRING","[RESTRICT] By code, it returns the customer base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522'],
                    'hd_atuacao_funcionario': ["FLOAT","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522'],
                    'mes_atuacao_funcionario' : ["DATETIME", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9202605387623801522']}
	   },
			
	   "cidade_regiao": 
	   {			
			"renomear_tables": 'cidade_regiao_hub',
			"remove_linhas_duplicadas": ['ALL'],
			"remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_cidade_regiao' : ["STRING", "[RESTRICT] Id for city and region", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9034142702620037429'],
                    'regiaoid_cidade_regiao': ["STRING","[RESTRICT] By code, it returns the region base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9034142702620037429'],
                    'cidadeid_cidade_regiao': ["STRING","[RESTRICT] By code, it returns the city base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9034142702620037429']}
	   },

	   "custo_adicional": 
		{	
			"renomear_tables": 'custo_adicional_hub',
			"remove_linhas_duplicadas": ['ALL'],
			"transforma_data": ['InicioVigencia', '%Y-%m-%d %H:%M:%S.%f'],
			"transforma_decimal": ['Custo', 'CustoRh'],
			"remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_custo_adicional' : ["STRING", "[RESTRICT] Table id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6091150745190133989'],
                    'funcaoid_custo_adicional': ["STRING","[RESTRICT] By code, returns the function base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6091150745190133989'],
                    'custo_custo_adicional': ["FLOAT","[RESTRICT] Additional cost of the function", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6091150745190133989'],
                    'iniciovigencia_custo_adicional' : ["DATETIME", "[RESTRICT] Beginning of cost effectiveness", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6091150745190133989'],
                    'cargoid_custo_adicional' : ["STRING", "[RESTRICT] By code, it returns the role base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6091150745190133989'],
                    'custorh_custo_adicional' : ["FLOAT", "[RESTRICT] HR cost", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6091150745190133989']}
	    },
			
	   "excecao_carga_horaria": 
			{
			"renomear_tables": 'excecao_carga_horaria_hub',
			"remove_linhas_duplicadas": ['ALL'],
			"transforma_data": ['Data', '%Y-%m-%d %H:%M:%S.%f'],
			"remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_excecao_carga_horaria' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9128730432282162739'],
                    'motivo_excecao_carga_horaria': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9128730432282162739'],
                    'data_excecao_carga_horaria': ["DATETIME","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/9128730432282162739']}
			},

	   "feriado": 
			{
			"renomear_tables": 'feriado_hub',
			"remove_linhas_duplicadas": ['ALL'],
			"transforma_data": ['Data', '%Y-%m-%d %H:%M:%S.%f'],
			"remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_feriado' : ["STRING", "[RESTRICT] Id for the holiday", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2558585418130211865'],
                    'nome_feriado': ["STRING","[RESTRICT] holiday name", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2558585418130211865'],
                    'tipo_feriado': ["STRING","[RESTRICT] Holiday type (city, state, national)", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2558585418130211865'],
                    'data_feriado' : ["DATETIME", "[RESTRICT] holiday date", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2558585418130211865'],
                    'cidadeid_feriado' : ["STRING", "[RESTRICT] By code, it returns the city base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2558585418130211865'],
                    'estadoid_feriado' : ["STRING", "[RESTRICT] By code, returns the state base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2558585418130211865'],
                    'paisid_feriado' : ["STRING", "[RESTRICT] By code, it returns the parent base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2558585418130211865'],
                    'recursivo_feriado' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/2558585418130211865']}
			},
			
	   "justificativa_recusa": 
			{
			"renomear_tables": 'justificativa_recusa_hub',
			"remove_linhas_duplicadas": ['ALL'],
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_justificativa_recusa' : ["STRING", "[INTERN] Refusal justification id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7405215861796204277'],
                    'codigo_justificativa_recusa': ["STRING","[INTERN] Justification type code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7405215861796204277'],
                    'tipojustificativa_justificativa_recusa': ["STRING","[INTERN] Profile refusal justification type", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7405215861796204277'],
                    'nomeingles_justificativa_recusa' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7405215861796204277'],
                    'nomeespanhol_justificativa_recusa' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7405215861796204277']}
			},
			
	   "membros_excecao_carga_horaria": 
			{
			"renomear_tables": 'membros_excecao_carga_horaria_hub',
			"remove_linhas_duplicadas": ['ALL'],
			"remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_membros_excecao_carga_horaria' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3336742499318059967'],
                    'excecaocargahorariaid_membros_excecao_carga_horaria': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3336742499318059967'],
                    'funcionarioid_membros_excecao_carga_horaria': ["STRING","[RESTRICT] By code, returns the employee base", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3336742499318059967'],
                    'departamento_membros_excecao_carga_horaria' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/3336742499318059967']}
			},

	   "regiao": 
			{
			"renomear_tables": 'regiao_hub',
			"remove_linhas_duplicadas": ['ALL'],
			"remover_colunas": ['UsuarioInclusao', 'DataInclusao', 'UsuarioAlteracao', 'DataAlteracao'],
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_regiao' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7292336331374302819'],
                    'nome_regiao': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7292336331374302819'],
                    'tipo_regiao': ["STRING","[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7292336331374302819'],
                    'nomeingles_regiao' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7292336331374302819'],
                    'nomeespanhol_regiao' : ["STRING", "[RESTRICT] Alert! Description pending with the base manager", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7292336331374302819']}
			},

	   "status_sugestao_funcionario": 
			{
			"renomear_tables": 'status_sugestao_funcionario_hub',
			"remove_linhas_duplicadas": ['ALL'],			
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
           "filtrar_colunas": {
                    'id_status_sugestao_funcionario' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5152174366587830337'],
                    'codigo_status_sugestao_funcionario': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5152174366587830337'],
                    'statusformacao_status_sugestao_funcionario': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5152174366587830337'],
                    'statuslideranca_status_sugestao_funcionario' : ["STRING", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5152174366587830337'],
                    'statusformacaoingles_status_sugestao_funcionario' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5152174366587830337'],
                    'statusformacaoespanhol_status_sugestao_funcionario': ["STRING","[INTERN] Spanish team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5152174366587830337'],
                    'statusliderancaingles_status_sugestao_funcionario' : ["STRING", "[INTERN] English leadership part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5152174366587830337'],
                    'statusliderancaespanhol_status_sugestao_funcionario' : ["STRING", "[INTERN] Status of the leadership part in Spanish", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/5152174366587830337']}
			},
         "solucao_macro":
            {
			"renomear_tables": 'solucao_macro_hub',
			"remove_linhas_duplicadas": ['ALL'],	
            "transforma_data": ['DataAlteracao', '%Y-%m-%d %H:%M:%S.%f'],		
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
            "filtrar_colunas": {
                        'id_solucao_macro' : ["STRING", "[INTERN] Employee suggestion status id", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nome_solucao_macro': ["STRING","[INTERN] Employee suggestion status code", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioinclusao_solucao_macro': ["STRING","[INTERN] Status of the team-building part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'datainclusao_solucao_macro' : ["STRING", "[INTERN] Status of the leadership part", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'usuarioalteracao_solucao_macro' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'dataalteracao_solucao_macro' : ["DATETIME", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeingles_solucao_macro' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271'],
                        'nomeespanhol_solucao_macro' : ["STRING", "[INTERN] English team building part status", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/6130648996792955271']}
                       },
	   "view_mapa_coletivo": 
			{
			"renomear_tables": 'view_mapa_coletivo_hub',
			"remove_linhas_duplicadas": ['ALL'],			
			"remover_caracter_especial_colunas": ['ALL'],
			"ingestion_models": 'full_load',
            "filtrar_colunas": {
                    'frente_id_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_codigo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_datainicio_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_equipeformada_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_duracao_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_status_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_cidadebase_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_estadobase_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_paisbase_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'frente_valorpropostacomercial_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'projeto_id_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'projeto_codigo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'projeto_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'cliente_id_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'cliente_codigo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'cliente_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'cliente_porte_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcao_id_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcao_codigo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcao_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcao_hierarquia_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_id_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_codigo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_carteira_id_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_carteira_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_ativo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_participataxaocupacao_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_cidadebase_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_estadobase_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_paisbase_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'cargo_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'cargo_hierarquia_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'funcionario_departamento_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'solucao_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'sociodiretor_codigo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'sociodiretor_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'lidernivel2_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'lidernivel2_codigo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'lidernivel3_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'lidernivel3_codigo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'lidernivel4_nome_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'gerareceita_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'agendaid_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'statusagenda_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'tipo_agenda_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'mescalendario_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'hd_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327'],
                    'custo_view_mapa_coletivo': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/7085272429091304327']}
            },
    "status_agenda":
        {
        "renomear_tables": 'status_agenda_hub',
        "remove_linhas_duplicadas": ['ALL'],
        "remover_colunas": ['UsuarioInclusao', 'DataInclusao'],
        "remover_caracter_especial_colunas": ['ALL'],
        "ingestion_models": 'full_load',
        "filtrar_colunas": {
                    'id_status_agenda': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/108654032428470081'],
                    'codigo_status_agenda': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/108654032428470081'],
                    'nome_status_agenda': ["STRING", "[INTERN] Pending", 'projects/data-plataform-prd/locations/us-central1/taxonomies/5848359484124665340/policyTags/108654032428470081']}
        }
   }

#    queries = {
#           "frente_hub": 
#           {
#            "renomear_tables": 'frente_hub_gp',
#            "query": """
#                     SELECT *
#                     FROM
#                     `data-plataform-prd.hub.frente_hub` as fh
#                     WHERE (NOT regexp_contains(fh.codigo_frente, '[a-zA-Z.]'))
#            """,          
#            "filtrar_colunas": {
#                         "id_frente": ["STRING", "[RESTRICT] front id","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "codigo_frente": ["STRING", "[RESTRICT] front code","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nome_frente": ["STRING", "[CONFIDENTIAL] front name","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "codigoprojeto_frente": ["STRING", "[RESTRICT] project code","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nomeprojeto_frente": ["STRING", "[CONFIDENTIAL] Project name","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "codigoproposta_frente": ["STRING", "[RESTRICT] commercial proposal code","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nomeproposta_frente": ["STRING", "[CONFIDENTIAL] Business proposal name","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "codigotipofrente_frente": ["STRING", "[RESTRICT] front type code","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nometipofrente_frente": ["STRING", "[RESTRICT] Front type name","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "codigoclassefrente_frente": ["STRING", "[RESTRICT] front class code","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nomeclassefrente_frente": ["STRING", "[RESTRICT] Front class name","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "sociodiretor_frente": ["STRING", "[CONFIDENTIAL] portfolio head partner","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "lidernivel2_frente": ["STRING", "[CONFIDENTIAL] Level 2 Leader (Partner)","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "datainicio_frente": ["STRING", "[RESTRICT] Project start date","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "duracao_frente": ["STRING", "[RESTRICT] Project duration","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "dataassinaturacontrato_frente": ["STRING", "[RESTRICT] Contract signature date","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "datatermoaceite_frente": ["STRING", "[RESTRICT] Acceptance term date","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "valorequipevendida_frente": ["STRING", "[CONFIDENTIAL] Value of team sold","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "dataautorizacaodiretoria_frente": ["STRING", "[RESTRICT] Board authorization date","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "statusid_frente": ["STRING", "[RESTRICT] Front status (in progress, completed, etc)","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "solucaoid_frente": ["STRING", "[RESTRICT] Project related solution","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "empresaid_frente": ["STRING", "[RESTRICT] Group company to which the project belongs","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "lidernivel3_frente": ["STRING", "[CONFIDENTIAL] Level 3 leader (GP)","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "lidernivel4_frente": ["STRING", "[CONFIDENTIAL] Level 4 Leader (Leader)","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nomefrenteoriginal_frente": ["STRING", "[CONFIDENTIAL] Original front name","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "valorpropostacomercial_frente": ["STRING", "[CONFIDENTIAL] Value of the commercial proposal","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "clienteid_frente": ["STRING", "[RESTRICT] By code, it returns the name of the customer","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "cidadebaseid_frente": ["STRING", "[RESTRICT] By code, it returns the base city of the project","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "valorequipeformada_frente": ["STRING", "[CONFIDENTIAL] Value of formed team","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "ativo_frente": ["STRING", "[RESTRICT] Returns whether the front is active or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "tipofrenteid_frente": ["STRING", "[RESTRICT] front type","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "classefrenteid_frente": ["STRING", "[RESTRICT] front class","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "temporario_frente": ["STRING", "[RESTRICT] Returns whether it is a temporary front or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "dataassociacaovenda_frente": ["STRING", "[RESTRICT] Sale association date","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "frenteassociada_frente": ["STRING", "[RESTRICT]","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nomeclientevenda_frente": ["STRING", "[CONFIDENTIAL] Sales customer name","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "dataequipeformada_frente": ["STRING", "[RESTRICT] Formed team date","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "dataequipevendida_frente": ["STRING", "[RESTRICT] Team sold date","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "valorequipeativagolive_frente": ["STRING", "[CONFIDENTIAL] Active team value","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "valorequipeatual_frente": ["STRING", "[CONFIDENTIAL] Current team value","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "dataliberacaoequipe_frente": ["STRING", "[RESTRICT] Date the team was released","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "responsavelformacaoequipe_frente": ["STRING", "[RESTRICT] Team Building Manager","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "equipeformada_frente": ["STRING", "[RESTRICT] Returns whether the team is formed or not","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "notificacaobriefingenviada_frente": ["STRING", "[RESTRICT] Returns whether the briefing completion notification was sent","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "porte_frente": ["STRING", "[RESTRICT] Project size","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "rankingfrenteid_frente": ["STRING", "[RESTRICT] front ranking","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "carteiraid_frente": ["STRING", "[RESTRICT] Portfolio in which the project is included","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "criticidade_frente": ["STRING", "[RESTRICT] Project criticality","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "novadatainicio_frente": ["STRING", "[RESTRICT] New project start date","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "keyaccount_frente": ["STRING", "[RESTRICT] Returns if the project is keyaccount","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "renovacao_frente": ["STRING", "[RESTRICT] Returns if it is a renovation project","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "categoria_frente": ["STRING", "[RESTRICT] project category","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "tipoprojetoid_frente": ["STRING", "[RESTRICT] By code, it returns the type of the project","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "frenterenovacaoid_frente": ["STRING", "[RESTRICT]","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nometipofrenteingles_frente": ["STRING", "[RESTRICT]","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nometipofrenteespanhol_frente": ["STRING", "[RESTRICT]","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nomeclassefrenteingles_frente": ["STRING", "[RESTRICT]","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "nomeclassefrenteespanhol_frente": ["STRING", "[RESTRICT]","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "datafim_frente": ["STRING", "[RESTRICT]","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "equipeformadaconcluida_frente": ["STRING", "[RESTRICT]","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/3960992071982626921"],
#                         "datainiciofinanceiro_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/4368623044624356178"],
#                         "datafimfinanceiro_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/4368623044624356178"],
#                         "intercompany_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/4368623044624356178"],
#                         "intercompanynumero_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/4368623044624356178"],
#                         "sucessfee_frente": ["STRING", "[RESTRICT] Financial start date.","projects/data-plataform-prd/locations/us-central1/taxonomies/5078221751262386073/policyTags/4368623044624356178"]}, 

#            "ingestion_models": 'full_load'           
#           }
#     }

   start = timer()
   orchestrator.run_pipeline_transformation(bucket_raw,database,job,url_teams, project_id)
   if 'queries' in locals():
      orchestrator.run_pipeline_view(database,project_id)    

   end = timer()
   print('apply_remove_special_caracters: {}' .format(timedelta(seconds=end-start)))

   return '200'
