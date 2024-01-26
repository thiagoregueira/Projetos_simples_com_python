from datetime import datetime, timedelta

print("Informe a data de Referência:")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

data_referencia = datetime(ano, mes, dia)

print()
print("**************************************************")

print("Calculadora de Datas")
print("1. Adicionar dias")
print("2. Subtrair dias")
print("3. Adicionar semanas")
print("4. Subtrair semanas")
print("5. Adicionar meses")
print("6. Subtrair meses")
print("7. Adicionar anos")
print("8. Subtrair anos")

opcao = int(input("Escolha uma opção (1-8): "))

if opcao == 1:
    dias = int(input("Quantos dias adicionar: "))
    nova_data = data_referencia + timedelta(days=dias)
elif opcao == 2:
    dias = int(input("Quantos dias subtrair: "))
    nova_data = data_referencia - timedelta(days=dias)
elif opcao == 3:
    semanas = int(input("Quantas semanas adicionar: "))
    nova_data = data_referencia + timedelta(weeks=semanas)
elif opcao == 4:
    semanas = int(input("Quantas semanas subtrair: "))
    nova_data = data_referencia - timedelta(weeks=semanas)
elif opcao == 5:
    meses = int(input("Quantos meses adicionar: "))
    nova_data = data_referencia + timedelta(days=30 * meses)
elif opcao == 6:
    meses = int(input("Quantos meses subtrair: "))
    nova_data = data_referencia - timedelta(days=30 * meses)
elif opcao == 7:
    anos = int(input("Quantos anos adicionar: "))
    nova_data = data_referencia.replace(year=data_referencia.year + anos)
elif opcao == 8:
    anos = int(input("Quantos anos subtrair: "))
    nova_data = data_referencia.replace(year=data_referencia.year - anos)
else:
    print("Opção inválida")

print(f"A nova data é: {nova_data.strftime('%d-%m-%Y')}")
