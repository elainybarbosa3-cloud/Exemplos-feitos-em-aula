'''frutas = ["maçã", "banana", "uva", "laranja"]
#Armazenado o nome da feira em uma variável
texto = " ˙ ✩°˖🫐 ⋆｡˚꩜ 𝐅𝐫𝐮𝐭𝐚𝐫𝐢𝐚 ˚˖𓍢ִ໋🌷͙֒✧˚.🎀༘⋆"
#Decorando
print('='*len(texto))
print(texto)
print('='*len(texto))
#adicionando o nome da fruta
continuar = "sim"
while continuar == "sim" or continuar == 's':
#verficando se a fruta já está na lista
    novo_item = input("𖧷₊˚˖𓍢ִ🍓✧˚.🎀༘⋆ﾟ＊ Digite o nome da fruta para adicionar a feira 𖧷₊˚˖𓍢ִ🍓✧˚.🎀༘⋆ﾟ＊: ").strip().title()
    if novo_item == '':
        print("⋆｡‧˚ʚ🍒ɞ˚‧｡⋆ Digite o nome de uma fruta para realizar o cadastro ⋆｡‧˚ʚ🍒ɞ˚‧｡⋆: ")    
    elif novo_item in frutas:
        posicao = frutas.index(novo_item) + 1
#Informar o ultimo elemento da lista
        print(f"o item informado já existe na{posicao}ª a posição da lista")
    else:
        frutas.append(novo_item)
        print(f"A fruta {frutas [-1]} foi cadastrada com sucesso ")
        print(frutas)
    continuar = input("⋆｡‧˚ʚ🍒ɞ˚‧｡⋆ deseja continuar 'sim' ou 'não' ⋆｡‧˚ʚ🍒ɞ˚‧｡⋆: ").strip().lower()
print("lista das frutas: ")
frutas_contadas = []
for fruta in frutas:
    if fruta not in frutas_contadas:
        quantidade = frutas.count(fruta)
        print(f"{fruta}: {quantidade} ocorrencia(s)")
        frutas_contadas.append(fruta)
print(f"lista das frutas: {frutas}")
print(f"quantidade de frutas {len(frutas_contadas)} frutas totalizadas")'''
while True:
    resposta = input("deseja sair:")
    if resposta == "sim":
        break
print("Programa encerrado")