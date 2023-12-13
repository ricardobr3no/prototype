import PySimpleGUI as sg

# layout
sg.theme('DarkPurple6')

col_1 = [
    [sg.B('7', size=(1, 2)), sg.B('8', size=(1, 2)), sg.B('9', size=(1, 2))],
    [sg.B('4', size=(1, 2)), sg.B('5', size=(1, 2)), sg.B('6', size=(1, 2))],
    [sg.B('1', size=(1, 2)), sg.B('2', size=(1, 2)), sg.B('3', size=(1, 2))],
    [sg.B('0', size=(1, 2)), sg.B('.', size=(1, 2)), sg.B('=', size=(1, 2), key='-EQUAL-')],
]

col_2 = [
    [sg.B('CE', size=(3, 2), key='-CEVERY-')],
    [sg.B('—', size=(3, 2))],
    [sg.B('+', size=(3, 8))],
]

col_3 = [
    [sg.B('<--', size=(3, 2), key='-CLEAR-')],
    [sg.B('X', size=(3, 2))],
    [sg.B('/', size=(3, 2))],
    [sg.B('+/-', size=(3, 2), key='-SWAP-')]
]


layout = [
    [sg.Text(key='-INPUT-', size=(250, 1), font='bold 20', justification='r', text_color='black', background_color='light gray')],
    [sg.Frame('', layout=[[sg.Col(col_1)]]), sg.Frame('', layout=[[sg.Col(col_2), sg.Col(col_3)]])]
]


# Process
window = sg.Window('Calculadora GUI', layout=layout, size=(330, 270))


historico = ''
numeros = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
op = ''
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event in numeros:
        if len(historico) <= 12:
            historico += event
        window['-INPUT-'].update(historico)

    elif event in ['X', '/', '—', '+']:
        num_1 = float(historico)
        op = event
        historico = ''

    elif event == '-SWAP-':
        historico = str(float(historico) * -1)
        window['-INPUT-'].update(historico)

    elif event == '-EQUAL-':
        num_2 = float(historico)
        answer = num_2

        if op == '+':
            answer = num_1 + num_2
        elif op == '—':
            answer = num_1 - num_2
        elif op == 'X':
            answer = num_1 * num_2
        elif op == '/':
            answer = num_1 / num_2

        historico = str(answer)
        window['-INPUT-'].update(historico)

    elif event == '-CLEAR-':
        historico = historico[:-1]
        window['-INPUT-'].update(historico)

    elif event == '-CEVERY-':
        historico = ''
        num_1 = 0
        num_2 = 0
        window['-INPUT-'].update(historico)

window.close()
