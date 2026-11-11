frutas = ["maçã", "banana", "uva", "laranja"]
while True:
    print("========================================")
    print("==========MENU DA FEIRA==========")
    print("1 - cadastrar frutas")
    print("2 - consultar frutas")
    print("3 - remover frutas")
    print("4 - sair")
    print("========================================")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print("cadastro de frutas")
        novo_item = input("informe o nome da fruta para cadastrar: ")
        if novo_item == "":
            print("informe um nome para realizar o cadastro")
        else:
            frutas.append(novo_item)
            print(f"A fruta {novo_item} foi cadastrada com sucesso")
    elif opcao == 2:
        print("======consultando Frutas======")
    elif opcao == 3:
        print("======Removendo Frutas=======")
    elif opcao == 4:
        print("======Encerrando o programa======")
        break
    else:
        print(f"Opção {opcao} não existe")