'''lista = [1,2,3]
lista.append(4)
#lista agora é [1,2,3,4]

lista2 = [5, 6]
lista += lista2
print(f"{lista}")
print(lista[3])
#lista agora é [1,2,3,4,5,6]

lista = [1, 2, 3 , 4 ,5]
primeiro_elemento = lista[0]
primeiro_elemento = lista[2]
print(f"{lista}")

lista = [1, 2, 3 , 4 , 5]
lista.remove(3)
#lista gora é [1,2,4,5]

del lista[0]
#lista agora é [2, 4, 5]

lista = [1, 2, 3, 4, 5]
tamanho_da_lista = len(lista)
print(f"{tamanho_da_lista}")


frutas = ["maçã", "banana", "uva", "laranja"]
frutas[0]
print (f"{frutas[0]}")
frutas[2]
print (f"{frutas[2]}")
frutas[-1]
print (f"{frutas[-1]}")
frutas[1] = "abacaxi"
frutas.append("melancia")
frutas.insert(-1, "pera")
frutas.extend(["kiwi", "manga"])
verificar = "maçã" in frutas
print(verificar)
quantidade_de_elementos = len(frutas)
print(quantidade_de_elementos)
contador = frutas.count("pera")
print(contador)
indice = frutas.index("pera")
print(f"a fruta do índice {indice}, corresponde ao elemento {frutas[indice]}")
listas = frutas.copy()
listas.append("melancia")
print(listas)
contador = listas.count("melancia")
print(contador)
print("percorrendo a lista")
for fruta in frutas:
    print(fruta)'''

#Declarando a lista de frutas
frutas = ["maçã", "banana", "uva", "laranja"]
#Armazenado o nome da feira em uma variável
texto = " ˙ ✩°˖🫐 ⋆｡˚꩜ 𝐅𝐫𝐮𝐭𝐚𝐫𝐢𝐚 ˚˖𓍢ִ໋🌷͙֒✧˚.🎀༘⋆"
#Decorando
print('='*len(texto))
print(texto)
print('='*len(texto))
#Adicionando uma condição e 
continuar = "sim"
while continuar == "sim" or continuar == 's':
    novo_item = input("𖧷₊˚˖𓍢ִ🍓✧˚.🎀༘⋆ﾟ＊ Digite o nome da fruta para adicionar a feira 𖧷₊˚˖𓍢ִ🍓✧˚.🎀༘⋆ﾟ＊: ").strip().title()
    if novo_item == '':
        print("⋆｡‧˚ʚ🍒ɞ˚‧｡⋆ Digite o nome de uma fruta para realizar o cadastro ⋆｡‧˚ʚ🍒ɞ˚‧｡⋆: ")
    elif novo_item in frutas:
        posicao = frutas.index(novo_item) + 1
        print(f"o item informado já existe na{posicao}ª a posição da lista")
    else:
        frutas.append(novo_item)
        print(f"A fruta {frutas [-1]} foi cadastrada com sucesso ")
        print(frutas)
    continuar = input("⋆｡‧˚ʚ🍒ɞ˚‧｡⋆ deseja continuar 'sim' ou 'não' ⋆｡‧˚ʚ🍒ɞ˚‧｡⋆: ").strip().lower()
print("lista das frutas: ")
#Imprimindo a lista toda
for i, fruta in enumerate(frutas):
    print(f"{i + 1} - {fruta}")
print(f"a lista contém {len(frutas)} tipos de frutas")