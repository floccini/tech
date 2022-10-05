from fastapi import FastAPI
from random import randrange
import requests
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=NTT-D02XPM3;"
    "Database=DOG_FACT"
)

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()


app = FastAPI()

lista = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789, ’.'


@app.get('/')

def read_root():
    return("Bem vindo a API Cifra de Cesar, acesse ../getcifra para receber uma mensagem encriptada.")

@app.get('/getcifra')

def get_cifra():
    response = requests.get('http://dog-api.kinduff.com/api/facts')
    json = response.json()

    response2 = requests.get('https://api.thedogapi.com/v1/breeds?limit=10&page=0')
    json2 = response2.json() 
    size = len(json2) 
    nome = []
    for i in range(size):
        nome.insert(i, (str(json2[i]['name']))) 

    key = randrange(1,27)
    phrase = str(json['facts'])
    originalPhrase = str(json['facts'])

    phrase = phrase.upper()
    copia = phrase

    for ch in copia:
        if ch not in lista:
            phrase = phrase.replace(ch, '')
            
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newPhrase = ''
    for i in phrase:
        index = alphabet.find(i)
        if index == -1:
            newPhrase += i  
        else:
            newIndex = index + key  
            if(newIndex >= 26):
                newIndex -= 26
            newPhrase += alphabet[newIndex:newIndex+1]
            
        newPhrase.lower()
    fato = newPhrase

    comando = f"""INSERT INTO fatos(fato) VALUES ('{fato}')"""
    cursor.execute(comando)
    cursor.commit()

    for i in range(size):
        comando2 = f"""INSERT INTO racas(nome) VALUES ('{nome[i]}')"""
        cursor.execute(comando2)
        cursor.commit()

    comando3 = """SELECT f.fato, r.nome FROM fatos as f JOIN racas as r on f.fatoId = r.racaId"""
    cursor.execute(comando3)
    cursor.commit()
    
    return ("Frase Criptografada", newPhrase, "Chave", key, "Frase Original", originalPhrase)

@app.post('/resolvecifra/{key}/{phrase}')

def resolve_Cifra(key, phrase):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    phrase = phrase.upper()
    key = int(key)
    newPhrase = ''
    copia = phrase
    for ch in copia:
        if ch not in lista:
            phrase = phrase.replace(ch, '')
    for i in phrase:
        index = alphabet.find(i) 
        if index == -1:
            newPhrase += i  
        else:
            newIndex = index - key
            if(newIndex >= 26):
                newIndex -= 26
            newPhrase += alphabet[newIndex:newIndex+1]
        newPhrase.lower()

    return ("Frase Descriptografada", newPhrase)

