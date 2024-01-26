from datetime import date


def calcular_idade(data_nascimento):
    hoje = date.today()
    ano_nascimento = data_nascimento.year
    idade = hoje.year - ano_nascimento
    if hoje.month < data_nascimento.month or (
        hoje.month == data_nascimento.month and hoje.day < data_nascimento.day
    ):
        idade -= 1
    return idade


dia = int(input("Dia de nascimento: "))
mes = int(input("Mês de nascimento: "))
ano = int(input("Ano de nascimento: "))
data_nascimento = date(ano, mes, dia)


idade = calcular_idade(data_nascimento)
print(f"Sua idade é: {idade} anos")
