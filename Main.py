import PySimpleGUI as sg
import Chances

sg.theme('DarkTeal9')


# First window
def Intro():
    layout = [[sg.Text('Welcome to DiceCalculator!', size=(40, 1))],
              [sg.Text('Choose probability to calculate:', size=(40, 1))],
              [sg.Button('At least 1 success on dice', size=(40, 1))],  [sg.Button('Exactly X successes', size=(40, 1))],
              [sg.Button('Every side equal to X', size=(40, 1))], [sg.Button('Every side equal to or greater than X', size=(40, 1))],
              [sg.Button('Every side equal to or lower than X', size=(40, 1))],
              [sg.Button('Exit')]]
    return sg.Window('DiceCalculator', layout, location=(600, 300), finalize=True)


def Chancep1():
    layout = [[sg.Text('Calculating the probability of at least 1 success:', size=(35, 1))],
              [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
              [sg.Text('Amount of Amount of dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
              [sg.Text('Success barrier (value+):', size=(35, 1)), sg.Input(key='success_barrier', enable_events=True)],
              [sg.Text(size=(100, 1), k='-OUTPUT-')],
              [sg.Button('Calculate the probability of at least 1 success!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('Chancep1', layout, finalize=True)


def Chancexs():
    layout = [[sg.Text('Calculating the probability of X successes:', size=(35, 1))],
              [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
              [sg.Text('Amount of dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
              [sg.Text('Success barrier (value+):', size=(35, 1)),
               sg.Input(key='success_barrier', enable_events=True)],
              [sg.Text('X:', size=(35, 1)),
               sg.Input(key='success_amount', enable_events=True)],
              [sg.Text(size=(100, 1), k='-OUTPUT-')],
              [sg.Button('Calculate the probability of X successes!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('Chancexs', layout, finalize=True)


def Chancewr():
    layout = [[sg.Text('Calculating the probability of every side being equal to X:', size=(50, 1))],
              [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
              [sg.Text('Amount of dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
              [sg.Text('X:', size=(35, 1)),
               sg.Input(key='value', enable_events=True)],
              [sg.Text(size=(100, 1), k='-OUTPUT-')],
              [sg.Button('Calculate the probability of every side equal to X!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('Chancewr', layout, finalize=True)


def Chancerw():
    layout = [[sg.Text('Calculating the probability of every side equal to or greater than X:', size=(50, 1))],
                  [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
                  [sg.Text('Amount of dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
                  [sg.Text('X:', size=(35, 1)), sg.Input(key='value', enable_events=True)],
                  [sg.Text(size=(100, 1), k='-OUTPUT-')],
                  [sg.Button('Calculate the probability of every side equal to or greater than X!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('Chancerw', layout, finalize=True)


def Chancemw():
    layout = [[sg.Text('Calculating the probability of every side equal to or lower than X:', size=(50, 1))],
              [sg.Text('Sides on a die:', size=(35, 1)), sg.Input(key='amount_of_sides', enable_events=True)],
              [sg.Text('Amount of dice thrown:', size=(35, 1)), sg.Input(key='dice_thrown_amount', enable_events=True)],
              [sg.Text('X:', size=(35, 1)), sg.Input(key='value', enable_events=True)],
              [sg.Text(size=(100, 1), k='-OUTPUT-')],
              [sg.Button('Calculate the probability of every side equal to or lower than X!', size=(35, 2)), sg.Button('Exit')]]
    return sg.Window('Chancemw', layout, finalize=True)


# GUI Loop
def Main():
    window1, window2 = Intro(), None
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            elif window == window1:     # if closing win 1, exit program
                break
        elif event == 'At least 1 success' and not window2:
            window2 = Chancep1()
        elif event == 'Exactly X successes' and not window2:
            window2 = Chancexs()
        elif event == 'Every side equal to X' and not window2:
            window2 = Chancewr()
        elif event == 'Every side equal to or greater than X' and not window2:
            window2 = Chancerw()
        elif event == 'Every side equal to or lower than X' and not window2:
            window2 = Chancemw()
        if event == 'Calculate the probability of at least 1 success!':
            result = Chances.Chance_for_1(int(values['success_barrier']), int(values['dice_thrown_amount']), int(values['amount_of_sides']), 1)
            window['-OUTPUT-'].update(result)
        if event == 'Calculate the probability of X successes!':
            result = Chances.Chance_for_x_successes(int(values['success_amount']), int(values['success_barrier']), int(values['dice_thrown_amount']), int(values['amount_of_sides']))
            window['-OUTPUT-'].update(result)
        if event == 'Calculate the probability of every side equal to X!':
            result = Chances.Chance_every_side_equal_x(int(values['dice_thrown_amount']), int(values['amount_of_sides']), int(values['value']))
            window['-OUTPUT-'].update(result)
        if event == 'Calculate the probability of every side equal to or greater than X!':
            result = Chances.Chance_equal_greater(int(values['dice_thrown_amount']), int(values['amount_of_sides']), int(values['value']))
            window['-OUTPUT-'].update(result)
        if event == 'Calculate the probability of every side equal to or lower than X!':
            result = Chances.Chance_equal_lower(int(values['dice_thrown_amount']), int(values['amount_of_sides']), int(values['value']))
            window['-OUTPUT-'].update(result)

    window.close()


if __name__ == '__main__':
    Main()
