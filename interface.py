#Interface gráfica da calculadora IRPF

import PySimpleGUI as psg

import calculadoraIRPF
from calculadoraIRPF import calcSomar

layout = [
    [psg.Text('Número 1: '), psg.InputText(key= 'num1')],
    [psg.Text('Número 2: '), psg.InputText(key= 'num1')],
    [psg.Button('calcular'), psg.Button('limpar')],
    ]

janela = psg.Window('Calculadora', layout)

while True:
    event, values = window.read()
    if event in (psg.WIN_CLOSED, 'Sair'):
        break
    elif evento == 'Calcular Soma':
        num1 = float(values['num1'])
        num2 = float(values['num2'])
        totalSoma = calcSomar(num1, num2)
    window['calcular'].update(f'A soma de {num1} e {num2} é: {totalSoma}')
window.close()