

def main():

    answers = questions()
    positive_questions = answers[1]
    print(positive_questions)


# Collect user data and store in separate lists
def questions () -> tuple[list[str], list[str]]:
    q1 = input("I feel that I am a person of worth, at least on an equal plane with others. ")
    q2 = input("I feel that I have a number of good qualities. ")
    q3 = input("All in all, I am inclined to feel that I am a failure. ")
    q4 = input("I am able to do things as well as most other people. ")
    q5 = input("I feel I do not have much to be proud of. ")
    q6 = input("I take a positive attitude toward myself. ")
    q7 = input("On the whole, I am satisfied with myself. ")
    q8 = input("I wish I could have more respect for myself. ")
    q9 = input("I certainly feel useless at times. ")
    q10 = input("At times I think I am no good at all. ")

# Assigning questions to lists to iteratate through them. 
    positive_list = [q1, q2, q4, q6, q7]
    negative_list = [q3, q5, q8, q9, q10]
    return positive_list, negative_list
# Variable to track the score
    

# TODO: #13 Program computes score for each response and sums scores and displays total. 
# Positive statement grading
def positive_q_grading ():
    
    score = 0
    for q in positive_list:
        if q == "A":
            score += 3
        elif q == "a":
            score += 2
        elif q == "d":
            score += 1
        else:
            score += 0
    return score

    for q in negative_list:
        if q == "A":
            score += 0
        elif q == "a":
            score += 1
        elif q == "d":
            score += 2
        else:
            score += 3

# Display results
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

if __name__ == "__main__":
    main()