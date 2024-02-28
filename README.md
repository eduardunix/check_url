#Sobre

Aplicação para checar se o endpoint está retornando 200.

```
#Dependencias
pip install sqlite3

#Cadastrar Sites
sqlite3 sites_processados
CREATE TABLE IF NOT EXISTS sites(Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,url TEXT PRIMARY KEY)
CREATE TABLE IF NOT EXISTS listasites(nome TEXT,url TEXT PRIMARY KEY)
INSERT INTO listasites (nome, url) VALUES ('NOME SITE OU APP', 'URL SITE OU APP');

É necessário cadastrar a API KEY do seu bot do TELEGRAM e GROUP ID.
https://my.cytron.io/tutorial/how-to-create-a-telegram-bot-get-the-api-key-and-chat-id?gad_source=1

#Excecutar
python3 check_200.py

```
