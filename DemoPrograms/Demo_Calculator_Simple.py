import PySimpleGUI as sg

# 界面布局
layout = [
    [sg.Input(key='input', size=(20,1)), sg.Button('C')],
    [sg.Button('1'),sg.Button('2'),sg.Button('3'),sg.Button('+')],
    [sg.Button('4'),sg.Button('5'),sg.Button('6'),sg.Button('-')],
    [sg.Button('7'),sg.Button('8'),sg.Button('9'),sg.Button('*')],
    [sg.Button('0'),sg.Button('.'),sg.Button('/'),sg.Button('=')]
]
window = sg.Window('简易计算器', layout)
expr = ''
while True:
    event, val = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'C':
        expr = ''
        window['input'].update('')
    elif event == '=':
        try:
            res = eval(expr)
            window['input'].update(str(res))
        except:
            window['input'].update('Error')
    else:
        expr += event
        window['input'].update(expr)
window.close()