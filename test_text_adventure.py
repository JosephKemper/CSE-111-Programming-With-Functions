from text_adventure import personalized_dialog
import pytest

def test_personalized_dialog():
    """
    Test that the personalized_dialog function correctly returns 
    the proper dialog items
    Parameters: none
    Return: nothing
    """
    key_list = (
        "he_she", 
        "him_her",
        "his_her",
        "boy_girl",
        "brother_sister",
        "son_daughter",
        "male_female",
        "men_women",
        "man_woman",
        "love_interest",
        "opposite_male_female",
        "opposite_men_women",
        "opposite_he_she",
        "opposite_his_her",
        "opposite_him_her",
        "enemy_leader")

    male_value_list = (
        "he",
        "him",
        "his",
        "boy",
        "brother",
        "son",
        "male",
        "men",
        "man",
        "girl",
        "female",
        "women",
        "she",
        "her",
        "her",
        "Lady")

    female_value_list = (
        "she",
        "her",
        "her",
        "girl",
        "sister",
        "daughter",
        "female",
        "women",
        "woman",
        "guy",
        "male",
        "men",
        "male",
        "he",
        "his",
        "him",
        "Lord")

    gender = "male"
    for key in key_list:
        assert personalized_dialog(gender, key) in male_value_list
    
    gender = "female"
    for key in key_list:
        assert personalized_dialog(gender, key) in female_value_list

def test_cabin_scene ():

    display_text == f"""
        "Today is going to be great!" You think to yourself.
I got the day off.
My friends and I have an amazing weekend planned.
I might even see that really cute {personalized_dialog(gender,love_interest)} again.
Who knows! Maybe I'll even ask {personalized_dialog(gender,opposite_him_her)} on a date.
Nothing could possibly ruin this day!
In the middle of your preparations to get ready for your weekend, 
you hear an unfamiliar voice shouting just outside your house.
{char_name.capitalize ()} should be inside, get {personalized_dialog(gender,him_her)} now. 
The High {personalized_dialog(gender,enemy_leader)} wants {personalized_dialog(gender,him_her)} alive and in one piece."
As you look out the window, you see a dozen strangely dressed 
{personalized_dialog(gender,men_women)} carrying large swords angrily moving towards your home.
You're at your dad's old cabin, miles out of town. 
Even if they went 80, it would take the police 30 minutes to get out here, 
and you're not sure if you can get signal anyway.
Police can't help me." You think to yourself. "I need to think of other options."
I could try to HIDE and hope they don't find me, 
or I could try to ESCAPE out the window and make a break for it. 
The forest is not far, I could run out there forever."""


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
