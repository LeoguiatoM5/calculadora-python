def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número inteiro válido.")

def main():
    nome_completo = input("Digite o seu nome completo: ")
    ano_atual = 2022

    ano_nascimento = obter_ano_nascimento()
    
    idade = calcular_idade(ano_nascimento, ano_atual)

    print("Nome: " + nome_completo)
    print("Idade: " + str(idade) + " anos")

if __name__ == "__main__":
    main()