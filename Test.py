from text_adventure import cust_dia
def main ():
    gender = "male"
    keys = ("he_she",
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
            "enemy_leader"
            )

    for key in keys:
        print(cust_dia(gender, key))

main()