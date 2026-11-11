cavaleiros = [
[1, "Capricórnio", "Shura"],
[2, "Aquário", "Camus"],
[3, "Peixes", "Afrodite"],
[4, "Áries", "Mu"],
[5, "Touro", "Aldebaran"],
[6, "Gêmeos", "Saga / Kanon"],
[7, "Câncer", "Máscara da   Morte"],
[8, "Leão", "Aiolia"],
[9, "Virgem", "Shaka"],
[10, "Libra", "Dohko"],
[11, "Escorpião", "Milo"],
[12, "Sagitário", "Aiolos"]  
]
mes = int(input("Digite o seu més de nascimento (1 a 12):"))
if 1 <= mes <= 12:
    cavaleiro = cavaleiros[mes - 1]
    print(f"Você é o cavaleiro {cavaleiro[2]} de {cavaleiro[1]}!")
else:
    print("Mês inválido!") 

    