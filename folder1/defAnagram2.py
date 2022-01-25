import random


def anagrama(recebe):
    listaSTR = []
    contSTR = len(str(recebe))
    strVazia = ""
    i = 0

    for i2 in str(recebe):
        listaSTR.append(str(i2))
    while i < len(str(recebe)):
        try:
            if i == 0:
                rand = random.randrange(0, contSTR)
                strVazia = strVazia + str(listaSTR[int(rand)])
                listaSTR.pop(rand)

            elif i != 0:
                contSTR = contSTR - 1
                rand = random.randrange(0, contSTR)
                strVazia = strVazia + str(listaSTR[int(rand)])
                listaSTR.pop(rand)
            i += 1

        except ValueError as e:
            print("Inválido!", e)
            break
    return strVazia
