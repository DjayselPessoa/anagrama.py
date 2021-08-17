# Anagramas são palavras formadas com as mesmas letras de alguma palavra específica em ordem diferente.

O programa simplesmente verifica na primeira def se há espaços o que indicaria a presença de uma segunda palavra, portanto não coloque espaço vazio no final da palavra escolhida ou o programa não aceitará 

na segunda def ele guarda todos os caracteres da palavra numa lista por meio do .append() num for onde o range é o len da palavra recebida

passando a lista adiante ele gera aleatóriamente um index "rand()" e com ele escolho um dos elementos da lista. em seguida retiro o elemento da lista por meio do método .pop(), utiliza o index do elemento para remover

uma variável recebe os caracteres recebidos aleatoriamente da lista e concatena até o último gerando um anagrama
