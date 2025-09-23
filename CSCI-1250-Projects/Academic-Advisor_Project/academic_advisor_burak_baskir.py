def score_calculator(enter_scores):
    print(enter_scores)
    quizes_score = float(input("Enter quiz score: "))
    if quizes_score < 0 or quizes_score > 100:
        print("Invalid score")
        exit(1)
    hackathons_score = float(input("Enter hackathon score: "))
    if hackathons_score < 0 or hackathons_score > 100:
        print("Invalid score")
        exit(1)
    labs_score = float(input("Enter lab score: "))
    if labs_score < 0 or labs_score > 100:
        print("Invalid score")
        exit(1)
    exams_score = float(input("Enter exam score: "))
    if exams_score < 0 or exams_score > 100:
        print("Invalid score")
        exit(1)

    total_score = quizes_score/10 + hackathons_score/10 + labs_score*2/5 + exams_score*2/5
    return total_score

def score_to_letter(total_score):
    if total_score <= 100 and total_score >= 90:
        return "A"
    elif total_score >= 80:
        return "B"
    elif total_score >= 70:
        return "C"
    elif total_score >= 60:
        return "D"
    elif total_score >= 0:
        return "F"
    else:
        print("Invalid score")
        exit(1)

print("Welcome to the academic advisor!")
total_score = score_calculator("Please enter the scores for the student:")
letter_grade = score_to_letter(total_score)
print(f"The total score is {total_score:.2f}, and the letter grade is {letter_grade}.")
if letter_grade == "A":
    print("Congrats! amazing job ")
elif letter_grade == "B":
    print("Keep up the consistent effort! ")
elif letter_grade == "C":
    print("Review quiz mistakes for patterns \n Start assignments earlier")
elif letter_grade == "D":
    print("Reviewing areas where you lost points\n Asking for help on challenging topics ")
else:
    print(""" You are currently failing. Consider:
        Focusing extra effort on upcoming assignments
        Meeting with your professor during office hours
        Forming a study group with classmates """)

