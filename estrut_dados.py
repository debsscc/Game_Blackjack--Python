exercicio = int(input( "Qual exercício de strings? "))
 
if exercicio == 1: 
    print ("SENHAS")

    #Solicita a senha pro usuário
    senha = input("Digite a senha: ")

    #Verifica se a senha tem pelo menos 8 caracteres, até 12
    if len(senha) < 8 or len(senha) > 12:
        print("Senha inválida. Deve ter entre 8 e 12 caracteres.")
    else:
        #Verifica se a senha contém letras maiúsculas, minúsculas e números	
        tem_maiuscula = False
        tem_minuscula = False
        tem_numero = False

        for caracter in senha:
            if caracter.isupper():
                tem_maiuscula = True
            elif caracter.islower():
                tem_minuscula = True
            elif caracter.isdigit():
                tem_numero = True

        #Se a senha atender a todos os critérios True, sendo válida, imprime que é válido
        if tem_minuscula and tem_maiuscula and tem_numero:
            print("Senha válida.")
        else:
            print("Senha Inválida")
    
elif exercicio == 2:
    print("Nome Compost")
    # Solicita o nome completo do aluno
    nome_completo = input("Nome Completo: ")

# Valida se o nome é composto
    if " " not in nome_completo.strip():
#O método strip() em Python é usado para remover espaços em branco do início e do final de uma string. Ele retorna uma cópia da string original sem os espaços em branco no início e no final.
        print("Ops... Por favor, digite o nome completo")
    else:
        # Extraindo o primeiro nome
        primeiro_nome = nome_completo.split()[0]
        
        # Exibindo o primeiro nome em letras maiúsculas
        print("Nome no Crachá:", primeiro_nome.upper())
    
elif exercicio == 3:
    # Solicita a palavra ao usuário
    palavra = input("Palavra: ")

    # Obtém a letra inicial da palavra
    letra_inicial = palavra[0]

    # Exibe a letra inicial
    print("Descubra:", letra_inicial, end=" ")

    # Itera sobre os caracteres da palavra, começando do segundo caractere
    for caractere in palavra[1:]:
        if caractere.lower() == letra_inicial.lower():
            # Se o caractere é igual à letra inicial (ignorando maiúsculas/minúsculas), imprime o caractere
            print(caractere, end=" ")
        else:
            # Se não, imprime "_"
            print
    
elif exercicio == 4:
    # Solicita a palavra ao usuário
    palavra = input("Palavra: ")

    # Obtém a versão invertida da palavra
    palavra_invertida = palavra[::-1]
    #[::-1] é uma forma de fatiar uma sequência (como uma string) em Python de forma a criar uma cópia invertida dela. 
    #Os dois primeiros : indicam que você está fazendo um fatiamento (slicing) da sequência.
    #O primeiro : antes do -1 indica que estamos começando do índice 0 (início da sequência).
    #O -1 indica o passo do fatiamento. Neste caso, o -1 significa que estamos indo da última posição para a primeira (ou seja, de trás para frente).

    # Verifica se a palavra é um palíndromo
    if palavra.lower() == palavra_invertida.lower():
        print(palavra, "é um Palíndromo")
    else:
        print(palavra, "não é um Palíndromo")


