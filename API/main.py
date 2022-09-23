from fastapi import FastAPI
from random import randrange
import requests

app = FastAPI()

@app.get('/')

def read_root():
    return("Bem vindo a API Cifra de Cesar, acesse ../getcifra para receber uma mensagem encriptada.")

@app.get('/getcifra')

def get_cifra():
    response = requests.get('http://dog-api.kinduff.com/api/facts')
    json = response.json()
    key = randrange(1,27)
    phrase = str(json['facts'])

    for ch in ["'", '[', ']']:
        if ch in phrase:
            phrase = phrase.replace(ch, '')
            
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    phrase = phrase.upper()
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
    
    return ("Frase Criptografada", newPhrase, "Chave", key, "Frase Original", phrase)

@app.post('/resolvecifra/{key}/{phrase}')

def resolve_Cifra(key, phrase):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    phrase = phrase.upper()
    key = int(key)
    newPhrase = ''
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

