from text_adventure import cust_dia
import pytest

def test_cust_dia():
    """
    Test that the cust_dia function correctly returns 
    the proper dialog items
    Parameters: none
    Return: nothing
    """
    gender = "male"
    assert cust_dia(gender, "he_she") == "he"
        # "him_her",
        # "his_her",
        # "boy_girl",
        # "brother_sister",
        # "son_daughter",
        # "male_female",
        # "men_women",
        # "man_woman",
        # "love_interest",
        # "opposite_male_female",
        # "opposite_men_women",
        # "opposite_he_she",
        # "opposite_his_her",
        # "opposite_him_her",
        # "enemy_leader"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
