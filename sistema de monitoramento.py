#Gregory Debom Ferreira Rm:562346
#Kenzo de Melo Sato Rm:563648
Temperatura = [
    [49, 19, 42, 12, 33],
    [60, 11, 38, 21, 47]
]
Umidade = [
    [37, 12, 88, 5, 63],
    [91, 28, 76, 45, 19]
]
Precipitação = [
    [63, 15, 88, 32, 71],
    [49, 21, 78, 55, 12]
]
x = 0  # Inicializa um contador para o número de alertas emitidos
print("------------------------------------------------------------------")
print("***TEMPERATURA***")
dia = 1  # Inicializa o contador de dias
# Itera sobre cada lista de temperaturas (cada "linha" representa um conjunto de medições)
for linha in Temperatura:
    # Itera sobre cada temperatura dentro de uma lista
    for temp in linha:
        # Verifica se a temperatura está fora da faixa considerada normal (>= 40 ou <= 5)
        if temp >= 40 or temp <= 5:
            print(f"Alerta de temperatura crítica no Dia {dia}")
            x += 1  # Incrementa o contador de alertas
        else:
            print(f"Clima sob controle no Dia {dia}")
        dia += 1  # Incrementa o contador de dias
print("------------------------------------------------------------------")
print("***UMIDADE***")
dia = 1  # Reinicializa o contador de dias
# Itera sobre cada lista de umidades
for linha in Umidade:
    # Itera sobre cada valor de umidade dentro de uma lista
    for umid in linha:
        # Verifica se a umidade está fora da faixa considerada normal (<= 20 ou >= 95)
        if umid <= 20 or umid >= 95:
            print(f"Alerta de umidade críticano dia {dia}")
            x += 1  # Incrementa o contador de alertas
        else:
            print(f"Clima sob controle no Dia {dia}")
        dia += 1  # Incrementa o contador de dias
print("------------------------------------------------------------------")
print("***PRECIPITAÇÃO***")
dia = 1  # Reinicializa o contador de dias
# Itera sobre cada lista de precipitações
for linha in Precipitação:
    # Itera sobre cada valor de precipitação dentro de uma lista
    for prep in linha:
        # Verifica se a precipitação é alta o suficiente para gerar um alerta de enchente (>= 80)
        if prep >= 80:
            print(f"Alerta de risco de enchente dia {dia}")
            x += 1  # Incrementa o contador de alertas
        else:
            print(f"Clima sob controle no Dia {dia}")
        dia += 1  # Incrementa o contador de dias

print("------------------------------------------------------------------")
print("***RESUMO_FINAL***")
print(f"Alertas emtidos {x}")
# Avalia o número total de alertas para determinar o risco geral
if x > 5:
    print("Risco Alto de Evento Climático Extremo")
else:
    print("Clima sob controle")