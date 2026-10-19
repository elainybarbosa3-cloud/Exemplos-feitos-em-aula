frutas = ["maçã", "banana", "uva", "laranja"]
continuar = "sim"
while continuar == "sim":
    novo_item = input("informe o nome da fruta para adicionar na lista: ").strip().title()
    if novo_item == "":
        print("informe o nome da fruta. nenhum item foi adicionado. ")
    elif novo_item in frutas:
        posicao = frutas.index(novo_item)
        print(f"A {[posicao]}, já está cadastrado")
    else:
     frutas.append(novo_item)
     print(f"A fruta {frutas[-1]}, foi adicionada com sucesso")
     continuar = input("Deseja continuar: [sim ou não]").lower()