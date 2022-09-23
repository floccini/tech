from fastapi import FastAPI
from random import randrange
import requests

app = FastAPI()

lista = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789, ’.'


@app.get('/')

def read_root():
    return("Bem vindo a API Cifra de Cesar, acesse ../getcifra para receber uma mensagem encriptada.")

@app.get('/getcifra')

def get_cifra():
    response = requests.get('http://dog-api.kinduff.com/api/facts')
    json = response.json()
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

