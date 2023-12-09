# Atividade 8 - SENAI Python Turma 21
# projeto calculadora de IRPF Mensal

#apresentação
print('\n\t\t\t -- Calculadora de de IRPF Mensal --\n')

#Entradas
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

#Funções
def calcSomar (num1, num2):
    return num1 + num2 # fórmula de soma

#Teste
totalSoma = calcSomar(num1, num2)
print(f'O valor total da soma é de: {totalSoma}')