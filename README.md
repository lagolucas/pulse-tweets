# science-pulse-tweets
 Twitter bot for science pulse project

 Release 1.1.0

 Para ser usado com chamadas em crontab


# Instalação

## Criar uma máquina virtual EC2 na amazon (recomendo t3a.nano)

## Instalar os seguintes itens
### Com yum
`sudo yum install python3`

`sudo yum install python3-dev libpq-dev`


### Com pip3
`pip3 install peewee`

`pip3 install tweepy`

`pip3 install psycopg2-binary`

## clonar o repositório na máquina

## Configurações

### alterar o arquivo config.json.default

Colocar as credenciais corretas de banco e da api do twitter e renomear para config.json

### alterar os arquivos twitter_auth.py e database.py

No início desses arquivos está o caminho para o config.json

É necessário adaptar esse código para que a chamada da crontab carregue corretamente

Caso o projeto tenha sido clonado na raiz da pasta do usuário, é necessário adicionar `science-pulse-tweets/` antes de `config.json`

# Funcionamento do BOT

## Parâmetros

### parametros para tipo de trends

Para cada tipo de trend usada no bot, é necessário um parâmetro com o `body_text` utilizado, isso será referenciado pelo param_id na tabela de fila de tweets

### end

Na tabela de parametros são necessários parâmetros com o slug `end` para cada lingua que serão construídos os fios no twitter

## Tweets

### Fila

No horário programado o robo irá varrer a tabela de fila buscando todos os tweets para montar o fio, esses tweets serão ordenados de acordo com o parâmetro trend-type para garantir que o primeiro tweet seja o com parâmetro com slug do tipo `popular`.

Os tweets serão atualizados com `bot_flag = True` depois de ter realizado o tweet.

## A aplicação precisa de um parâmetro para funcionar corretamente

Para execução do script é necessário passar dos parâmetros a língua e o período do dia.

As opções para língua são `pt` e `en`;

As opções para período do dia são  `night` e `morning`;

### Configuração do cronjob

Os crnjobs usados atualmente são os seguintes:

`0 13 * * * nohup python3 science-pulse-tweets/tuitar.py pt morning > sci_out_pt_morn.log 2> sci_err_pt_morn.log &`

`0 14 * * * nohup python3 science-pulse-tweets/tuitar.py en morning > sci_out_en_morn.log 2> sci_err_en_morn.log &`

`0 23 * * * nohup python3 science-pulse-tweets/tuitar.py pt night > sci_out_pt_night.log 2> sci_err_pt_night.log &`

`0 0 * * * nohup python3 science-pulse-tweets/tuitar.py en night > sci_out_en_night.log 2> sci_err_pt_night.log &`
