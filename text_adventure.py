# The Ultimate Choose Your Own Adventure Game
import PySimpleGUI as sg



def main ():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('This is a test')],
        [sg.Text('Enter something on Row 2'), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()


# Create window for program display

# Create buttons for exiting and user choices

# Create box for text entry for user choices
# Allow for both text entry and button selection

# Nest each scene and its alternatives in a function. 
# Function will return (not print) the appropriate version of each scene. 
# Scenes will have one argument with a default value that determines the version of the scene



if __name__ == "__main__":
    main()
    




