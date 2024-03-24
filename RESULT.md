# Resultado - Desáfio CoorLab

## Requisitos
- Backend
- Frontend
- Opcional (Banco de Dados)

## Backend
Foi utilizado o Flask, framework do python, para o backend, com o objeto principal de fazer a comunicação entre o banco de dados e o frontend. Nele, foram implementados o algoritimo responsavel pela criação do banco de dados e eventuais definições das tabelas. Tambem foram implementados 4 rotas, sendo apenas duas: 
getBestPrices, com o intuito de pegar as informações da tabela Travel, filtrando pelo menor valor encontrado de preço e horario; 
e getCities, com o intuito de pegar todas as cidades existentes na tabela Cities, e suas respectivas id's para eventualmente auxiliar na chamada da outra rota.

Dentre as bibliotecas usadas: Flask, Flask-CORS, SQLAlchemy, SQLAlchemy-utils, json, os,

## Frontend
Foi utilizado o Vue3.js, framework do JS, para o frontend, para criar o UI interativo com o usuario. Nele, foram implementados 3 componentes com uma pagina principal: 
App.vue era a pagina principal que contém todos os componentes, sendo definidos nele a estrutura geral da pagina e functionalidades a serem usadas em outros componentes;
MySidebar.vue, um componente responsavel pelo menu sidebar interativo;
TravelCalc.vue, responsavel pela funcionalidade principal da pagina, onde ocorrem a maior parte das lógicas;
TravelDestinyOptions.vue, que disponibiliza as cidades possiveis encontradas no banco de dados, para o cliente poder escolher uma delas.

Dentre as dependencias usadas: Axios, eslint, prettier e sass

## Banco de Dados
Foi utilizado o SGBD Postgresql para o armazenamento das informações contidas em data.json. Através do pacote SQLAlchemy foi criado um db no banco de dados local, com 3 schemas diferentes de tabela, ou seja, 3 tabelas. A tabela Travels contia todos os dados, a tabela Cities, as cidades, e a tabela Companies, as companias. Tanto a tabela Cities quanto a tabela Companies, se relacionavam com a tabela Travels, através de chaves estrangeiras referentes aos id's das cidades e companias comtidas na tabela Travels.

**Obs**
No banco de dados, foi necessario a criação de um novo usuario e senha, com a permissão de criar novas tabelas.