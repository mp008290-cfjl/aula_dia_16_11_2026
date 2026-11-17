pessoas = []

for i in range(1, 11):
    print(f"---pessoa{i}---")
    nome = input("digite o nome: ").strip()
    idade = int(input("Digite a senha: "))

    pessoa = {
        "nome": nome,
        "idade": idade
    }
    pessoas.append(pessoa)

print("\n=== pessoas com menos de 18 anos===")
for pessoa in pessoas:
    if pessoa["idade"] < 18:
        print(f"nome: {pessoa['nome']} | idade: {pessoa['idade']}anos")

    print("\n=== pessoas com 18 anos ou mais===")
    for pessoa in pessoas:
        if pessoa["idade"] >= 18:
            print(f"nome: {pessoa['nome']}anos")