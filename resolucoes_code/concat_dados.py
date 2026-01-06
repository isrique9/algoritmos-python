# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

print(f"Tu escreveu: {palavra1} {palavra2}. Está correto? (Y/N)")

resposta = input("Está correto? (Y/N): ")

if resposta.lower() in ['y', 'sim']:
    print("Ok, obrigado por me testar.")
else:
    print("Me desculpe pelo erro, vou melhorar na próxima vez.")
