#inicio

import os 

nome : str = ""
nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0
valor_media: float = 0 
dir : str = ""
arq: str = ""

def main ():
    pasta = '/tmp/exercicios'
    os.makedirs (pasta, exist_ok= True ) #afirmando que existe
    os.chmod (pasta,0o744)#assegurando que tem permissão
    c = 0
    while c < 5:
        entrada(c)
        c= c + 1

def entrada(c):
    global nota1 , nota2 , nota3 , nota4 , valor_media
    nota1 = float (input("Digite a 1° nota: "))
    nota2 = float (input("Digite a 2° nota: "))
    nota3 = float (input("Digite a 3° nota: "))
    nota4 = float (input("Digite a 4° nota: "))
    nome = input("Digite o nome do aluno: ")
    valor_media = med(nota1,nota2,nota3,nota4)
    if(valor_media >= 6):
        print("Média: ",valor_media, ", Aprovado!")
    elif (valor_media >=3):
        print("Média: ",valor_media, ", Exame!")
    else: 
        print("Média: ",valor_media, ", Retido!")
    cadastro = (nome , nota1 , nota2 , nota3, nota4, valor_media, c)

def med(nota1 , nota2 , nota3 , nota4): 
    media : float = 0
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

def cadastro(nome , nota1 , nota2 , nota3 , nota4 , valor_media):
    global dir ,  arq
    dir = 'tmp/exercicios'
    arq = 'ex21.txt'
    linha = nome + ";" + str(nota1) + ";" + str (nota2)+ ";" + str (nota3) + ";" + str (nota4) + ";" + (valor_media) + "\n"
    #concatenação com quebra de linha e operação de cast
    escreveArq(dir, arq, linha, valor_media)


def escreveArq (caminho , nome_arq , linha_cad , c):
    if (os.path.exists(caminho)) and (os.path.isdir(caminho)):
        if (c == 0):
            tipo = 'w'
        else : 
            tipo = 'a'
    with open (caminho + nome_arq , tipo) as file: 
        file.write (linha_cad) 

if (__name__=='__main__'): 
    main()

#fim 