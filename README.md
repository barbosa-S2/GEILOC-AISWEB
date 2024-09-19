# Consumidor da API GEILOC da AISWEB

Este projeto permite consultar aeroportos em uma determinada cidade brasileira utilizando a API da AISWEB. O código obtém informações como nome e código ICAO dos aeroportos disponíveis.

## Principais Funcionalidades

- **Requisição de Dados**: O usuário informa o nome da cidade e o programa consulta os aeroportos associados a essa localidade.
  
- **Conversão de XML para JSON**: A resposta da API, que vem em XML, é convertida para um formato JSON para facilitar a manipulação dos dados.

- **Listagem de Aeroportos**: O programa exibe os aeroportos encontrados, mostrando:
  - Nome do aeroporto
  - Código ICAO correspondente
