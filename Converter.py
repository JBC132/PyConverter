import PySimpleGUI as sg

layout = [
    [sg.Input(), sg.Spin(['km to mile', 'kg to pound', 'sec to min']), sg.Button('Convert')],
    [sg.Text('Output')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()