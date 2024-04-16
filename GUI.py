import PySimpleGUI as sg
from Api_calculator import add, substraction, multiplication, division, absolute, remainder, pow, root, log, ln, sin, cos, tan

# Define the layout of the calculator
layout = [
    [sg.Input(size=(30, 1), key='-DISPLAY-')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/'), sg.Button('sin'), sg.Button('cos'), sg.Button('tan')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*'), sg.Button('asin'), sg.Button('acos'), sg.Button('atan')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-'), sg.Button('1/x'), sg.Button('root'), sg.Button('pow')],
    [sg.Button('0'), sg.Button('.'), sg.Button('+'), sg.Button('abs'), sg.Button('%'), sg.Button('log'), sg.Button('ln')],
    [sg.Button('Clear'), sg.Button('='), sg.Button('Exit')]
]

# Create the PySimpleGUI window
window = sg.Window('Calculator', layout)

# Function to clear the display
def clear_display():
    window['-DISPLAY-'].update('')

# Function to update the display
def update_display(value):
    current_value = window['-DISPLAY-'].get()
    window['-DISPLAY-'].update(current_value + value)

# Event loop to handle user interactions
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Clear':
        clear_display()
    elif event == '=':
        try:
            result = eval(values['-DISPLAY-'])
            window['-DISPLAY-'].update(result)
        except Exception as e:
            window['-DISPLAY-'].update('Error')
    else:
        try:
            # If the event corresponds to a function name, call the function from the imported module
            if event in ('sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'root', 'log', 'ln', '1/x', 'abs'):
                func = globals()[event]  # Get the function from the global namespace
                display_value = float(values['-DISPLAY-'])
                result = func(display_value)
                window['-DISPLAY-'].update(result)
            else:
                update_display(event)
        except Exception as e:
            window['-DISPLAY-'].update('Error')

# Close the window
window.close()
