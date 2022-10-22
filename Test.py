# The Ultimate Choose Your Own Adventure Game


# Setting up variables as lists to allow for dynamic scene mapping
current_options = []
current_scene = []
display_text_list = []
next_scenes = []

def main ():
    # All the stuff inside your window.
    char_info = character_creation()
    print("char_info = ",type(char_info))
    prior_death = False
    discovered_powers = False
    char_name = char_info[0]
    print("char_name = ",type(char_name))
    char_gender = char_info[1]
    print("char_gender = ",type(char_gender))


    # Maps the player choices to the variable current_scene
    current_scene = cabin_scene(char_name, char_gender, prior_death, discovered_powers)
    # Returns display_text, player_choices, next_scenes
    print("current_scene = ",type(current_scene))

    # Pulls display text from current scene to display to user
    display_text_list = current_scene [0]
    print("display_text_list = ",type(display_text_list))
    display_text = display_text_list [0]
    print("display_text = ",type(display_text))
    
    # Pulls returned options from current scene to be mapped to display
    current_options = current_scene [1]
    print("current_options = ",type(current_options))
    option_1 = current_options ["option_1"]
    print("option_1 = ",type(option_1))
    option_2 = current_options ["option_2"]
    print("option_2 = ",type(option_2))

    
    
    # Create the Window

def personalized_dialog (gender, key):
    """
    The dialog in this adventure commonly uses 
    gender references that are meant to be tailored 
    directly to the player. The purpose of this function
    is to allow those references to be dynamic to the character
    which the player created.
    """
    if gender == "male":
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
    elif gender == "female":
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
    return "test", "Male"


def cabin_scene(char_name, gender, prior_death,discovered_powers):
    """
    This function is used to stage user interaction 
    for activities that happen in the cabin scene of the story.
    """

    if prior_death == False:
        cabin_text = f"""
        "Today is going to be great!" You think to yourself.
I got the day off.
My friends and I have an amazing weekend planned.
I might even see that really cute {personalized_dialog(gender,"love_interest")} again.
Who knows! Maybe I'll even ask {personalized_dialog(gender,"opposite_him_her")} on a date.
Nothing could possibly ruin this day!
In the middle of your preparations to get ready for your weekend, 
you hear an unfamiliar voice shouting just outside your house.
{char_name.capitalize ()} should be inside, get {personalized_dialog(gender,"him_her")} now. 
The High {personalized_dialog(gender,"enemy_leader")} wants {personalized_dialog(gender,"him_her")} alive and in one piece."
As you look out the window, you see a dozen strangely dressed 
{personalized_dialog(gender,"men_women")} carrying large swords angrily moving towards your home.
You're at your dad's old cabin, miles out of town. 
Even if they went 80, it would take the police 30 minutes to get out here, 
and you're not sure if you can get signal anyway.
Police can't help me." You think to yourself. "I need to think of other options."
I could try to HIDE and hope they don't find me, 
or I could try to ESCAPE out the window and make a break for it. 
The forest is not far, I could run out there forever."""
        player_choices = {
            "option_1":"hide",
            "option_2":"escape"}

        next_scenes = {
            "option_1":closet_scene,
            "option_2":forest_scene}

        return cabin_text, player_choices, next_scenes

def closet_scene():
    pass

def forest_scene():
    pass


if __name__ == "__main__":
    main()
    





