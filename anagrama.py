from folder1.defAnagram import analisando1
from folder1.defAnagram2 import ObjAnagram


active = True
resultado = ""
listaNomes = []
recebe = ""
processa = ""

while active:
    try:
        recebe = str(input("Use \'S\' para sair\nInforme uma ou mais palavras separadas por vírgula: "))
        if recebe == "S" or recebe == "s":
            print("Encerrando aplicação!")
            active = False
            break
        if recebe.find(","): 
            listaNomes = recebe.split(",")
            for x in listaNomes:
                print("item: " + str(x))
                umaPalavra = analisando1(str(x))
                print(umaPalavra)
                if umaPalavra is True:
                    resultado = ObjAnagram.anagrama(x)
        cont = 0
        for w in resultado:
            print(f"{cont + 1} item: " + str(w))
            cont = cont + 1

    except ValueError as e:
        print("Inválido!", e)
        break
