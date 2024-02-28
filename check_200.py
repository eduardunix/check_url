#Verificador de status de aplicação web, ele verifica se esta retornando status code 200, caso nao retorne 200 é  encaminhado uma mensagem no telegram.
import requests
import subprocess
import sqlite3

#TELEGRAM
token = ''
id_canal = ''

#CONEXAO COM SQLITE PARA URL JA PROCESSADAS
con = sqlite3.connect('sites_processados')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS sites(Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,url TEXT PRIMARY KEY)')
cur.execute('CREATE TABLE IF NOT EXISTS listasites(nome TEXT,url TEXT PRIMARY KEY)')
cur.execute('DELETE FROM sites WHERE Timestamp <= datetime(\'now\', \'-1 day\')')
con.commit()
lista_de_sites = cur.execute('SELECT * FROM listasites')
lista = lista_de_sites.fetchall()

for coluna in lista:
    nome = coluna[0]
    url = coluna[1]
    print(nome)
    consulta = cur.execute('SELECT * FROM sites where url = ?', (url,))
    resultado = cur.fetchone()
    print(resultado)
    if requests.get(url).status_code == 200:
        print(f"a aplicação {nome} está no ar")
    else:
        if not resultado:
            print(f"a aplicação {nome} está fora do ar")
            mensagem = f"a aplicação {nome} está fora do ar"
            url_bot = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id_canal}&text={mensagem}"
            print(requests.get(url_bot).json())
            cur.execute('INSERT INTO sites (url) VALUES (?)', (url,))
            con.commit()
con.close()
