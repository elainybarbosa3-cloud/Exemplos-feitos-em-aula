n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print(f"soma ou total: {n1} + {n2} = {s}, produto: {n1} x {n2} = {m}, razão: {n1} / {n2} = {d:.2f}", end = ' >>> ')
print(f"Divisão inteira {di} e potência {e}")