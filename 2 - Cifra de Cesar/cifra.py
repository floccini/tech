def cifra(dado, chave, modo):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mensagemRecebida = ''
    for i in dado:
        index = alfabeto.find(i) #Acha a posição da letra no alfabeto, e guarda dentro de index
            
        if index == -1:
            mensagemRecebida += i  #Caso o caractere não esteja dentro da variável alfabeto, ele o mantém e pula pro próximo
        else:
            novoIndex = index + chave if modo == 1 else index - chave  #Lida com o caracter de acordo com o modo, somando ou diminuindo a posição com a chave
            print(novoIndex)
            if(novoIndex >= 26):
                novoIndex -= 26
                print(novoIndex) 
            mensagemRecebida += alfabeto[novoIndex:novoIndex+1] #procura no alfabeto a letra que corresponde as posições de novoIndex, uma por uma, e devolve pra variáv
        
    return mensagemRecebida.lower()

def verificaChave(chave):
    if chave > 26 or chave < 1:
        print('Chave inválida, o intervalo deve ser entre 1 e 26')
        exit()
    return chave

def main():
    modo = input('Digite E para encriptar, D para decriptar ou qualquer outra letra para ver um exemplo: ')
    if modo.lower() == "d":
        modo = 0
        chave = int(input('Qual o valor da chave de decriptação? Deve ser entre 1 e 26\n'))
        mensagem = input('Digite a mensagem a ser decriptada: ').upper()
        resultado = cifra(mensagem, chave, modo)
        print(f"A mensagem é: {resultado}")
    elif modo.lower() == "e":
        modo = 1
        chave = int(input('Qual o valor da chave de encriptação? Deve ser entre 1 e 26\n'))
        verificaChave(chave)
        mensagem = input('Digite a mensagem a ser encriptada: ').upper()
        resultado = cifra(mensagem, chave, modo)
        print(f"A mensagem encriptada é: {resultado}")
    else:
        mensagem = 'Nenhuma grande descoberta foi feita jamais sem um palpite ousado'
        print(f"Aqui vai um exemplo da mensagem: '{mensagem}' sendo encriptada com chave 4")
        mensagem = mensagem.upper()
        chave = 4
        modo = 1
        resultado = cifra(mensagem, chave, modo)
        print(f"A mensagem encriptada é: {resultado}")

if __name__ == "__main__":
    main()
