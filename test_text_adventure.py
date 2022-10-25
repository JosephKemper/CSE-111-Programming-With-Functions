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


def test_cabin_scene ():
    prior_death = False
    discovered_powers = False
    char_gender = "Male"
    char_name = "John"
    test_cabin_scene = cabin_scene(char_name, char_gender, prior_death,discovered_powers) 
    # Returns (story_text, player_choices, next_scenes)

    next_scenes = test_cabin_scene [2]
    assert next_scenes ["option_1"] == closet_scene 
    assert next_scenes ["option_2"] == forest_scene

    player_choices = test_cabin_scene [1]
    assert player_choices ["option_1"] == "HIDE"
    assert player_choices ["option_2"] == "ESCAPE"
    
    assert "girl" == personalized_dialog(char_gender,"love_interest")
    assert "her" == personalized_dialog(char_gender,"opposite_him_her")
    assert "John" == char_name.capitalize ()
    assert "him" == personalized_dialog(char_gender,"him_her")
    assert "Lady" == personalized_dialog(char_gender,"enemy_leader")
    assert "him" == personalized_dialog(char_gender,"him_her")
    assert "men" == personalized_dialog(char_gender,"men_women")
    
    char_gender = "Female"
    char_name = "Jane"
    
    assert "guy" == personalized_dialog(char_gender,"love_interest")
    assert "him" == personalized_dialog(char_gender,"opposite_him_her")
    assert "Jane" == char_name.capitalize ()
    assert "her" == personalized_dialog(char_gender,"him_her")
    assert "Lord" == personalized_dialog(char_gender,"enemy_leader")
    assert "her" == personalized_dialog(char_gender,"him_her")
    assert "women" == personalized_dialog(char_gender,"men_women")
    



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
