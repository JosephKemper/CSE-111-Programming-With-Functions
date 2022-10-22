# The Ultimate Choose Your Own Adventure Game
import PySimpleGUI as sg
import time

def main ():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    character_info = character_creation()
    prior_death = False
    discovered_powers = False

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

def cust_dia (gender, key):
    """
    The dialog in this adventure commonly uses 
    gender references that are meant to be tailored 
    directly to the player. The purpose of this function
    is to allow those references to be dynamic to the character
    which the player created.
    """
    male = {
        "he_she" :"he", 
        "him_her" : "him",
        "his_her" : "his",
        "boy_girl" : "boy",
        "brother_sister" : "brother",
        "son_daughter" : "son",
        "male_female" : "male",
        "men_women" : "men",
        "man_woman" : "man",
        "love_interest" : "girl",
        "opposite_male_female" : "female",
        "opposite_men_women" : "women",
        "opposite_he_she" : "she",
        "opposite_his_her" : "her",
        "opposite_him_her" : "her",
        "enemy_leader" : "Lady"
        }

    female = {
        "he_she" : "she",
        "him_her" : "her",
        "his_her" : "her",
        "boy_girl" : "girl",
        "brother_sister" : "sister",
        "son_daughter" : "daughter",
        "male_female" : "female",
        "men_women" : "women",
        "man_woman" : "woman",
        "love_interest" : "guy",
        "opposite_male_female" : "male",
        "opposite_men_women" : "men",
        "opposite_he_she" : "he",
        "opposite_his_her" : "his",
        "opposite_him_her" : "him",
        "enemy_leader" : "Lord"
        }
    if gender == "male":
        return male.get(key)
    elif gender == "female":
        return female.get(key)

def cabin_scene(char_name, gender, prior_death,discovered_powers):
    

    if prior_death == False:
        display_text == f"""
        "Today is going to be great!" You think to yourself.
I got the day off.
My friends and I have an amazing weekend planned.
I might even see that really cute {cust_dia(gender,love_interest)} again.
Who knows! Maybe I'll even ask {cust_dia(gender,opposite_him_her)} on a date.
Nothing could possibly ruin this day!
In the middle of your preparations to get ready for your weekend, 
you hear an unfamiliar voice shouting just outside your house.
{char_name.capitalize ()} should be inside, get {cust_dia(gender,him_her)} now. 
The High {cust_dia(gender,enemy_leader)} wants {cust_dia(gender,him_her)} alive and in one piece."
As you look out the window, you see a dozen strangely dressed 
{cust_dia(gender,men_women)} carrying large swords angrily moving towards your home.
You're at your dad's old cabin, miles out of town. 
Even if they went 80, it would take the police 30 minutes to get out here, 
and you're not sure if you can get signal anyway.
Police can't help me." You think to yourself. "I need to think of other options."
I could try to HIDE and hope they don't find me, 
or I could try to ESCAPE out the window and make a break for it. 
The forest is not far, I could hide in there forever."""
        



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
    





