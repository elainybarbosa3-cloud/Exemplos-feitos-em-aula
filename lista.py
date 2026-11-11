cavaleiros = ["Aiolia","Shaka","Mu", "Milo", "Camus"]
quantidade_de_elementos = len(cavaleiros)
print(quantidade_de_elementos)
cavaleiros.append("Aiolos")
print(cavaleiros)
cavaleiros.insert(0, "Dohko")
print(cavaleiros)
cavaleiros.remove("Milo")
print(cavaleiros)
print(f"o cavaleiro {cavaleiros.pop()} foi removido.")
primeiro = cavaleiros[0]
print(primeiro)
cavaleiros.sort()
print(cavaleiros)
for cavaleiro in cavaleiros:
    print(cavaleiro)