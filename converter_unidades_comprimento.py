def converter_comprimento(valor, unidade_origem, unidade_destino):
    unidades = {
        "metros": 1,
        "centímetros": 0.01,
        "milímetros": 0.001,
        "quilômetros": 1000,
        "polegadas": 0.0254,
        "pés": 0.3048,
    }
    resultado = valor * unidades[unidade_origem] / unidades[unidade_destino]
    return round(resultado, 2)  # Arredonda o resultado para 2 casas decimais


valor = float(input("Digite o valor: "))
unidade_origem = input("Digite a unidade de origem (por exemplo, 'metros'): ").lower()
unidade_destino = input(
    "Digite a unidade de destino (por exemplo, 'centímetros'): "
).lower()

resultado = converter_comprimento(valor, unidade_origem, unidade_destino)
print(f"{valor} {unidade_origem} equivalem a {resultado} {unidade_destino}")
