from folder1.defAnagram import analisando1
from folder1.defAnagram2 import anagrama
active = True
resultado = ""

while active:
    try:
        recebe = str(input("Informe uma palavra: "))
        umaPalavra = analisando1(recebe)
        print(umaPalavra)
        if umaPalavra == True:
            resultado = anagrama(recebe)
            print(resultado)
            break
        else:
            print("INFORME SOMENTE UMA PALAVRA - REINICIANDO!")

    except ValueError as e:
        print("Inválido!", e)
        break
