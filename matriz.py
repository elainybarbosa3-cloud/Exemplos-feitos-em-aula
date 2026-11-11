'''matriz = [
    [3,4,7,8],
    [1,3,6,2],
    [6,9,7,8],
    [7,5,0,8],
]
lista = matriz[0] #Retorna a primeira lista [3,4,7,8]
print(list)
print(f"O elemento da linha 1 e coluna 2 = {matriz[1][2]}")
#Primeiro índice pega a linha e o segundo a coluna
print(f"O elemento da linha 1 e coluna 2 = {matriz[2][1]}")
#modificar os valores de uma matriz
matriz[1][2] = 10
print(matriz)'''
numeros = [
    [3,4,7,8],
    [1,3,6,2],
    [6,9,7,8],
    [7,5,0,8],
]
print(numeros[1][2])
l = int(input("Qual linha você quer ver: "))
linha = numeros [l - 1]
print(linha)
print(numeros[1][2])