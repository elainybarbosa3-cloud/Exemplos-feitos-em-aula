idade = int(input("informe a sua idade: "))
situacao_matricula = input("informe a situação de sua matrícula (matriculado/nao matriculado): ").upper()
if idade >= 18 and situacao_matricula == "matriculado":
    print("Acesso liberado!")
else:
    print("Acesso negado!")
    