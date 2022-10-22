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
        [sg.Text("Or make a 3rd option"), 
        sg.InputText(key="text_input"),sg.Button("Option 3")],
        [sg.Button("Cancel")] ]

    
    
    # Create the Window
    window = sg.Window("The Ultimate Choose Your Own Adventure Story", layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel": # if user closes window or clicks cancel
            break
        

    window.close()

def character_creation ():
    sg.theme("default1")   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Welcome to our story. This is where you create your character.')],
                [sg.Text("Please enter your character name, then select your character's gender.")], 
                [sg.Text('Name'), sg.InputText(key="-NAME-")],
                [sg.Radio('Male', "RADIO", key= "-MALE-", default= True),
                sg.Radio('Female', "RADIO", key= "-FEMALE-")],
                [sg.Submit() ,sg.Cancel()] ]

# TODO: #61 Build functionality for Option 3 to be used. 

# TODO: #56 Get the Character Creation window to close when I am done with it. 
# TODO: #57 Build first scene and figure out how I will build and print more scenes
# TODO: #58 Figure out how I am going to organize my app. 

# Possibly enable a continue button to show up after they have selected either male or female. 
# Change the gender select buttons to a radio button. 
    
    window = sg.Window('The Ultimate Choose Your Own Adventure Story', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        character_name = values ["-NAME-"]
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
            window.close()
        elif len(character_name)<1:
            sg.popup ("Please enter a name and select a gender for your character to continue.")
        elif len (character_name) >=1:
            if event == "Submit":
                character_gender = ""
                if values ["-MALE-"]:
                    character_gender = "Male"
                elif values ["-FEMALE-"]:
                    character_gender = "Female"
            
                # Next line was used for testing purposes
                #sg.popup(f"You entered {character_name} and {character_gender}")
            return character_name, character_gender, window.close()
        
    window.close()



# Create buttons for exiting and user choices

# Create box for text entry for user choices
# Allow for both text entry and button selection

# Nest each scene and its alternatives in a function. 
# Function will return (not print) the appropriate version of each scene. 
# Scenes will have one argument with a default value that determines the version of the scene



if __name__ == "__main__":
    main()
    





