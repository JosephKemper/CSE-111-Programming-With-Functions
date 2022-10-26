# The Ultimate Choose Your Own Adventure Game
import PySimpleGUI as sg


def main ():
    sg.theme("default1")   
    # All the stuff inside your window.
    char_info = character_creation()
    char_name = char_info[0]
    char_gender = char_info[1]

    # TODO #87 Get current_scene to update based on player choice
    # Build each scene into a self sustaining window that 
    # will work similar to how the character creation window works


    # Maps the player choices to the variable current_scene
    current_scene = cabin_scene(char_name, char_gender)
    # Returns (story_text, player_choices, next_scenes)

    # Pulls display text from current scene to display to user
    display_text = current_scene [0]
    
    # Pulls returned options from current scene to be mapped to display
    current_options = current_scene [1]
    option_1 = current_options ["option_1"]
    option_2 = current_options ["option_2"]

    # Format of dictionary values
    # {"option_1":first_scene,"option_2":second_scene}
    next_scenes = current_scene [2]
    first_scene = next_scenes ["option_1"]
    second_scene = next_scenes ["option_2"]

    layout = [
        [sg.Text('Page 1/5', size=20, key='TEXT')],
        [sg.pin(sg.Button('PREV', visible=False)), sg.Push(), sg.pin(sg.Button('NEXT'))],
    ]

    
    # TODO: #77 BUG Options 1 and 2 not working. 
    # Create the Window
    window = sg.Window("The Ultimate Choose Your Own Adventure Story", layout)
    # Event Loop to process "events" and get the "values" of the inputs
    page = 1
    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event in ('PREV', 'NEXT'):
            page += 1 if event == 'NEXT' else -1
        window['TEXT'].update(f'Page {page}/5')
        window['PREV'].update(visible=(page!=1))
        window['NEXT'].update(visible=(page!=5))

    window.close()



def personalized_dialog (char_gender, key):
    """
    The dialog in this adventure commonly uses 
    gender references that are meant to be tailored 
    directly to the player. The purpose of this function
    is to allow those references to be dynamic to the character
    which the player created.
    """
    if char_gender == "Male":
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
        return male.get(key)
    elif char_gender == "Female":
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
        return female.get(key)

def character_creation ():
    sg.theme("default1")   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Welcome to our story. This is where you create your character.')],
                [sg.Text("Please enter your character name, then select your character's gender.")], 
                [sg.Text('Name'), sg.InputText(key="-NAME-")],
                [sg.Radio('Male', "RADIO", key= "-MALE-", default= True),
                sg.Radio('Female', "RADIO", key= "-FEMALE-")],
                [sg.Submit() ,sg.Cancel()] ]

    window = sg.Window('The Ultimate Choose Your Own Adventure Story', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        char_name = values ["-NAME-"]
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
            window.close()
        elif len(char_name)<1:
            sg.popup ("Please enter a name and select a gender for your character to continue.")
        elif len (char_name) >=1:
            if event == "Submit":
                char_gender = ""
                if values ["-MALE-"]:
                    char_gender = "Male"
                elif values ["-FEMALE-"]:
                    char_gender = "Female"
            
                # Next line was used for testing purposes
                #sg.popup(f"You entered {character_name} and {character_gender}")
            return char_name, char_gender, window.close()
        
    window.close()


def cabin_scene(char_name, char_gender):
    """
    This function is used to stage user interaction 
    for activities that happen in the cabin scene of the story.
    """
    story_text = f""""Today is going to be great!" You think to yourself.
I got the day off.
My friends and I have an amazing weekend planned.
I might even see that really cute {personalized_dialog(char_gender,"love_interest")} again.
Who knows! Maybe I'll even ask {personalized_dialog(char_gender,"opposite_him_her")} on a date.
Nothing could possibly ruin this day!
In the middle of your preparations to get ready for your weekend, 
you hear an unfamiliar voice shouting just outside your house.
"{char_name.capitalize ()} should be inside, get {personalized_dialog(char_gender,"him_her")} now. 
The High {personalized_dialog(char_gender,"enemy_leader")} wants {personalized_dialog(char_gender,"him_her")} alive and in one piece."
As you look out the window, you see a dozen strangely dressed 
{personalized_dialog(char_gender,"men_women")} carrying large swords angrily moving towards your home.
You're at your dad's old cabin, miles out of town. 
Even if they went 80, it would take the police an hour to get out here, 
and you're not sure if you can get cell signal anyway.
"Police can't help me." You think to yourself. "I need to think of other options."
I could try to HIDE and hope they don't find me, 
or I could try to ESCAPE out the window and make a break for it. 
The forest is not far, I could run out there forever."""
        
    player_choices = {
            "option_1":"HIDE",
            "option_2":"ESCAPE"}

    next_scenes = {
            "option_1":closet_scene,
            "option_2":forest_scene}

    return story_text, player_choices, next_scenes

#TODO: #83 Build out closet scene
def closet_scene(char_name, char_gender):
    story_text = f"""You quickly duck in the closet and hide, 
but as they continue to search the house determined to find you, 
your nerves start to get the better of you.
You hear several people moving closer to the closet door.
When the door opens, you see six large {personalized_dialog(char_gender, men_women)}, 
dressed in blood red robes with masks covering their faces, 
and giant swords pointing towards you. 
Your father's old shotgun is right behind you. 
If it even works ... or is loaded, you might be able to get a shot off ...
but these robed lunatics might give professional bodybuilders a run for their money.
Or instead of FIGHTing, you could just GIVE UP and hope for the best. 
They do want you in one piece after all ... which is hopefully a good thing."""


    player_choices = {
        "option_1":"FIGHT",
        "option_2":"GIVE UP"}

    next_scenes = {
        "option_1":"filler_0",
        "option_2":"filler_1"}

    return story_text, player_choices, next_scenes

# TODO: Build out Forest Scene
def forest_scene(char_name, char_gender):
    story_text = f"""You carefully look out the back window, 
making sure not to be seen, 
waiting until all of the cultists start making their way into the front door. 
You quickly open the window and run as fast as you can into the forest.
Just as you get to the tree line you hear someone yell behind you 
{personalized_dialog(char_gender, he_she)}'s running into the forest. The yelling and loud footsteps behind you, 
tells you that the whole group is chasing after you and drives you to run faster. 
You duck behind a bush, then notice a cave in the side of the nearby mountain 
and quickly run for it.
As you sprint to the cave, a giant sword flies so close to your head that it nicks your ear. 
You almost feel as though the force of the wind from the sword flying by you might have knocked you over, 
but the force of trees exploding into little pieces of shrapnel in front of you after the sword tore through it 
and the tree in front of it certainly did knock you over, and seeing the sword fly back over your face, 
barely missing your nose as you tumble to the ground makes you grateful you only hit your head on a rock.
As you quickly struggle to your feet, feeling a little disoriented from the explosion, 
you don't stop to listen to the argument between two of the cultists not far behind you. 
You just run. You run for your life. 
You run with all the energy of two trees exploding into little pieces of shrapnel that are still covering much of your body.
As you duck into the cave, you stop in horror to find it barely goes back 6 feet. 
With the sun behind the mountain that 6 feet is certainly dark, 
but the pain from hundreds of pieces of wood embedded into your flesh testifies that what you thought you knew cannot be true. 
Hundreds of points of terrible pain and the memory of a giant sword flying back over your face, 
returning as though on command to its wielder, leaves you with a perfect conviction, 
that there is a lot you do not know about the world. There is a lot even science does not know about the world.
You stand there, back pressed firmly against the rock, 
in perfect silence for what feels like an eternity, wrapped in a gem, and gifted back to you. 
Waiting. Listening. Feeling. But there's more. So much more. 
Part of you wants to just melt into the rock and hope these freaks never find you. 
Part of you wants to grab the nearby branch, left over from one of the exploding trees, 
and see how many of them you can take out. Part of you wants to fall to your knees and cry, 
but you know there is no time for that right now.
What do you want to do:
Embrace the weird and try to MERGE into the rock,
or pick up the BRANCH and try to fight?"""

    player_choices = {
            "option_1":"MERGE",
            "option_2":"BRANCH"}

    next_scenes = {
        "option_1":"filler_0",
        "option_2":"filler_1"}


    return story_text, player_choices, next_scenes


if __name__ == "__main__":
    main()
    





