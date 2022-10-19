# The Ultimate Choose Your Own Adventure Game
import PySimpleGUI as sg

def main ():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    character_info = character_creation()
    
    display_text = character_info
    option_1 = "Run"
    option_2 = "Fight"
    layout = [  [sg.Text(display_text)],
        [sg.Button(option_1),sg.Button(option_2)], 
        [sg.Text('Or try your luck with your own option'), sg.InputText()],
        [sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('The Ultimate Choose Your Own Adventure Story', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()

def character_creation ():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Welcome to our story. This is where you create your character.')],
                [sg.Text("Please enter your character name, then select your character's gender.")], 
                [sg.Text('Name'), sg.InputText()],
                [sg.Radio('Male', "RADIO1"),
                sg.Radio('Female', "RADIO1")],
                [sg.Button('Exit')] ]

# TODO: #48 Figure out how to assign text the user enters to a variable. 
# TODO: #49 Figure out how to exit a function to go to the next window in PYsimpleGUI.
# TODO: #50 Figure out how to make a user enter both a name and select a gender to continue
# Possibly enable a continue button to show up after they have selected either male or female. 
# Change the gender select buttons to a radio button. 
    
    window = sg.Window('The Ultimate Choose Your Own Adventure Story', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        character_name = values [0]
        if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
            break
        elif event == "Male":
            character_gender = "Male"
            return character_name, character_gender
        elif event == "Female":
            character_gender = "Female"
            return character_name, character_gender
    window.close()



# Create buttons for exiting and user choices

# Create box for text entry for user choices
# Allow for both text entry and button selection

# Nest each scene and its alternatives in a function. 
# Function will return (not print) the appropriate version of each scene. 
# Scenes will have one argument with a default value that determines the version of the scene



if __name__ == "__main__":
    main()
    





