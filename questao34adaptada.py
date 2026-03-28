#inicio 

import os 
valor : int = 0
dir : str = ""
arq: str =""

def main(): 
    pasta = '/tmp/exercicios'
    #os.mkdir(pasta)
    os.makedirs(pasta, exist_ok= True) #afirmando que existe 
    os.chmod (pasta, 0o744) #assegurando que ela tem permissão
    global valor
    c = 0 #contador tem que começar com zero
    valor  = int (input("Digite um número de 1 até 10: "))
    while (c <= 10): #enquanto c menor ou igual que 10, vai repetir
        rslt = mult (c,valor) #chamando multi 
        grava(c,rslt)
        print (valor, "x", c, "=" , rslt)
        c = c + 1


def mult (vlr , tab):
    res = vlr * (tab)
    return res

def grava (c, rslt):
    global dir, arq
    dir = '/tmp/exercicios/'
    arq = 'ex34.txt'
    linha = str (rslt) + '\n' #quebra de linha
    if (os.path.exists(dir)) and (os.path.isdir(dir)): # verifica se existe e é uma pasta
        tipo = 'w'
        if (c==0): #se o contador for 0 (ent começa com zero) x * 0
            tipo = 'w'
        else: #caso contador seja maior que zero
            tipo = 'a'
    with open (dir + arq , tipo) as file : #agr abre o arquivo usando o tipo escolhido acima, temq somar as strings tb
        file.write (linha)

if (__name__== '__main__'):
    main()

 
