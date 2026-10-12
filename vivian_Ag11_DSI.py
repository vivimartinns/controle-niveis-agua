
# Agenda 11 - Controle de Níveis de Água
# Simulação de monitoramento de um reservatório

from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init()

# Lista com as situações dos cinco níveis
situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função que define a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Exibe os níveis do reservatório
print("=== CONTROLE DE NÍVEIS DE ÁGUA ===\n")

for nivel in range(1, 6):
    situacao = situacoes[nivel - 1]
    cor = definir_cor(nivel)

    print(cor + f"Nível {nivel}: {situacao}" + Style.RESET_ALL)

print("\nMonitoramento finalizado!")
