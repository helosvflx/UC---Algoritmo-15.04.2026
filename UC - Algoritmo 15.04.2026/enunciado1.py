def calcularMedia():
    notas = []

    for i in range[3]:
        try:
            notas = float(input(f"Digite a {i+1}ª nota: "))
            notas.append(notas)
        except ValueError:
            print("Erro: as notas devem ser numéros.")
        except ZeroDivisionError:
            print("Sem notas.")
            return
        
    media = sum(notas) / len(notas)
    print(f"A média final é: {media}")

calcularMedia()
