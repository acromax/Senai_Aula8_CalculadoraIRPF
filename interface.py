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
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'limpar':
        janela['valores'].update('')
        janela['resultado'].update('')
        janela['valores'].set_focus()
    else:
        valores = int(valores['valores'])
        janela['resultado'].update(funcoesConversorTemperatura.celsius_para_fahrenheit(valores))

janela.close()