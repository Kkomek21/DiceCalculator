import PySimpleGUI as sg
import Chances

# For this to work, you need to have the second file (Chances) imported. This is merely a GUI.
sg.theme('DarkTeal9')


def intro():
    layout = [[sg.Text('Welcome to DiceCalculator!', size=(40, 1))],
              [sg.Text('Choose probability to calculate:', size=(40, 1))],
              [sg.Button('At least 1 success', size=(40, 1))],  [sg.Button('Exactly X successes', size=(40, 1))],
              [sg.Button('Every side equal to X', size=(40, 1))], [sg.Button('Every side equal to or greater than X', size=(40, 1))],
              [sg.Button('Every side equal to or lower than X', size=(40, 1))],
              [sg.Button('Exit')]]
    return sg.Window('DiceCalculator', layout, location=(600, 300), finalize=True)


def chancep1():
    layout = [[sg.Text('Calculating the probability of at least 1 success:', size=(35, 1))],
              [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
              [sg.Text('Dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
              [sg.Text('Success barrier (value+):', size=(35, 1)), sg.Input(key='success_barrier', enable_events=True)],
              [sg.Text(size=(100, 1), k='-OUTPUT-')],
              [sg.Button('Calculate the probability of at least 1 success!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('chancep1', layout, finalize=True)


def chancexs():
    layout = [[sg.Text('Calculating the probability of X successes:', size=(35, 1))],
              [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
              [sg.Text('Dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
              [sg.Text('Success barrier (value+):', size=(35, 1)),
               sg.Input(key='success_barrier', enable_events=True)],
              [sg.Text('X:', size=(35, 1)),
               sg.Input(key='success_amount', enable_events=True)],
              [sg.Text(size=(100, 1), k='-OUTPUT-')],
              [sg.Button('Calculate the probability of X successes!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('chancexs', layout, finalize=True)


def chancewr():
    layout = [[sg.Text('Calculating the probability of every side being equal to X:', size=(50, 1))],
              [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
              [sg.Text('Dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
              [sg.Text('X:', size=(35, 1)),
               sg.Input(key='value', enable_events=True)],
              [sg.Text(size=(100, 1), k='-OUTPUT-')],
              [sg.Button('Calculate the probability of every side equal to X!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('chancewr', layout, finalize=True)


def chancerw():
    layout = [[sg.Text('Calculating the probability every side equal to or greater than X:', size=(50, 1))],
                  [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
                  [sg.Text('Dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
                  [sg.Text('X:', size=(35, 1)), sg.Input(key='value', enable_events=True)],
                  [sg.Text(size=(100, 1), k='-OUTPUT-')],
                  [sg.Button('Calculate the probability of every side equal to or greater than X!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('chancerw', layout, finalize=True)


def chancemw():
    layout = [[sg.Text('Calculating the probability every side equal to or lower than X:', size=(50, 1))],
              [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
              [sg.Text('Dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
              [sg.Text('X:', size=(35, 1)), sg.Input(key='value', enable_events=True)],
              [sg.Text(size=(100, 1), k='-OUTPUT-')],
              [sg.Button('Calculate the probability of every side equal to or lower than X!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('chancemw', layout, finalize=True)


window1, window2 = intro(), None
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'At least 1 success' and not window2:
        window2 = chancep1()
    elif event == 'Exactly X successes' and not window2:
        window2 = chancexs()
    elif event == 'Every side equal to X' and not window2:
        window2 = chancewr()
    elif event == 'Every side equal to or greater than X' and not window2:
        window2 = chancerw()
    elif event == 'Every side equal to or lower than X' and not window2:
        window2 = chancemw()
    if event == 'Calculate the probability of at least 1 success!':
        result = Chances.chance_for_1(int(values['success_barrier']), int(values['dice_thrown_amount']), int(values['amount_of_sides']), 1)
        window['-OUTPUT-'].update(result)
    if event == 'Calculate the probability of X successes!':
        result = Chances.chance_for_x_successes(int(values['success_amount']), int(values['success_barrier']), int(values['dice_thrown_amount']), int(values['amount_of_sides']))
        window['-OUTPUT-'].update(result)
    if event == 'Calculate the probability of every side equal to X!':
        result = Chances.chance_every_side_equal_x(int(values['dice_thrown_amount']), int(values['amount_of_sides']), int(values['value']))
        window['-OUTPUT-'].update(result)
    if event == 'Calculate the probability of every side equal to or greater than X!':
        result = Chances.chance_equal_greater(int(values['dice_thrown_amount']), int(values['amount_of_sides']), int(values['value']))
        window['-OUTPUT-'].update(result)
    if event == 'Calculate the probability of every side equal to or lower than X!':
        result = Chances.chance_equal_lower(int(values['dice_thrown_amount']), int(values['amount_of_sides']), int(values['value']))
        window['-OUTPUT-'].update(result)

window.close()
