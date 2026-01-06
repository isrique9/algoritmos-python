# Transforma Celsius em Fahrenheit e vice-versa.

opcao = input("Digite C para Celsius->Fahrenheit ou F para Fahrenheit->C: ")

if opcao.upper() == "C":
    c = float(input("Temperatura em °C: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f:.2f}°F")
elif opcao.upper() == "F":
    f = float(input("Temperatura em °F: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c:.2f}°C")
else:
    print("Opção inválida.")
