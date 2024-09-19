!pip install xmltodict

import pprint
import json
import requests
import xmltodict

def requisicao():
  api_key = "1737636254"
  api_pass = "cf334dde-eb8c-11ee-8b18-0050569ac2e1"
  tipo = "AD"
  cidade = input("Informe a cidade desejada: ")

  url = f"http://aisweb.decea.gov.br/api/?apiKey={api_key}&apiPass={api_pass}&area=rotaer&city={cidade}&type={tipo}"

  requisicao = requests.get(url)
  resposta = requisicao.content

  return resposta

def xml_to_dict(resposta):
  resposta_json = xmltodict.parse(resposta)

  return resposta_json

def resultado(resposta_json):

  total_aeroportos = int(resposta_json.get('aisweb').get('rotaer').get('@total'))

  if total_aeroportos == 1:
    cidade = resposta_json.get('aisweb').get('rotaer').get('item').get('city')

    aeroporto = resposta_json.get('aisweb').get('rotaer').get('item')

    print(f"\n\nA cidade de {cidade} tem os seguinte aeroporto:\n")

    print(f"Aerodromo 1\nNome: {aeroporto.get('name')}\nCódigo ICAO: {aeroporto.get('AeroCode')}\n")

  else:

    cidade = resposta_json.get('aisweb').get('rotaer').get('item')[0].get('city')

    lista_aeroportos = resposta_json.get('aisweb').get('rotaer').get('item')

    numero = 1

    print(f"\n\nA cidade de {cidade} tem os seguintes aeroportos:\n")

    for aeroporto in lista_aeroportos:
      print(f"Aerodromo {numero}\nNome: {aeroporto.get('name')}\nCódigo ICAO: {aeroporto.get('AeroCode')}\n")
      numero +=1

def main():
  resposta = requisicao()
  resposta_json = xml_to_dict(resposta)
  resultado(resposta_json)

#--------------------------------------------------------------------------------------------------------------
main()
