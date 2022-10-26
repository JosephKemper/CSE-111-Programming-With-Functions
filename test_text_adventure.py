from text_adventure import personalized_dialog, cabin_scene, closet_scene, forest_scene
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

    char_gender = "Male"
    for key in key_list:
        assert personalized_dialog(char_gender, key) in male_value_list
    
    char_gender = "Female"
    for key in key_list:
        assert personalized_dialog(char_gender, key) in female_value_list

# TODO: #92 New adjustments to cabin_scene has caused this test to fail. 
def test_cabin_scene ():
    prior_death = False
    discovered_powers = False
    char_gender = "Male"
    char_name = "John"
    test_cabin_scene = cabin_scene(char_name, char_gender) 
    # Returns (dialog_used, player_choices, next_scenes, window.close())

    dialog_used = test_cabin_scene [0]
    assert dialog_used ["love_interest"] == "girl"
    assert dialog_used ["opposite_him_her"] == "her"
    assert dialog_used ["char_name"] == "John"
    assert dialog_used ["him_her"] == "him"
    assert dialog_used ["enemy_leader"] == "Lady"
    assert dialog_used ["him_her"] == "him"
    assert dialog_used ["men_women"] == "men"
    


    player_choices = test_cabin_scene [1]
    assert player_choices ["option_1"] == "HIDE"
    assert player_choices ["option_2"] == "ESCAPE"
    next_scenes = test_cabin_scene [2]
    assert next_scenes ["option_1"] == closet_scene 
    assert next_scenes ["option_2"] == forest_scene
    
    char_gender = "Female"
    char_name = "Jane"
    
    assert dialog_used ["love_interest"] == "guy"
    assert dialog_used ["opposite_him_her"] == "him"
    assert dialog_used ["char_name"] == "Jane"
    assert dialog_used ["him_her"] == "her"
    assert dialog_used ["enemy_leader"] == "Lord"
    assert dialog_used ["him_her"] == "her"
    assert dialog_used ["men_women"] == "women"

    



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
