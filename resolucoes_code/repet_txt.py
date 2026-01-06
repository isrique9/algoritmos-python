# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

import random

print("Adivinhe o número entre 1 e 10!")
segredo = random.randint(1, 10)

while True:
    palpite = int(input("Seu palpite: "))
    if palpite == segredo:
        print("🎉 Acertou!")
        break
    else:
        print("❌ Errado, tente de novo...")
