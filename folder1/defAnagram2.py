import random

class anagram:

    def anagrama(self, recebe):
        innerActive = True
        self.recebe = recebe
        self.contSTR = len(str(self.recebe))
        x = 0
        lista2STR = []
        while innerActive:
            if x == 5:
                innerActive = False
                return str(lista2STR(0))+"\n"+str(lista2STR(1))+"\n"+str(lista2STR(2))+"\n"+str(lista2STR(3))+"\n"+str(lista2STR(4))
            listaSTR = []
            strVazia = ""
            i = 0

            for i2 in str(self.recebe):
                listaSTR.append(str(i2))
            while i < len(str(self.recebe)):
                try:
                    if i == 0:
                        rand = random.randrange(0, self.contSTR)
                        strVazia = strVazia + str(listaSTR[int(rand)])
                        listaSTR.pop(rand)

                    elif i != 0:
                        self.contSTR = self.contSTR - 1
                        rand = random.randrange(0, self.contSTR)
                        strVazia = strVazia + str(listaSTR[int(rand)])
                        listaSTR.pop(rand)
                    i += 1

                except ValueError as e:
                    print("Inválido!", e)
                    break
            lista2STR.append(strVazia)
            x = x + 1

ObjAnagram = anagram()