try:
    m, p, c = [float(x) for x in input("ENTER THE MARKS OBTINED IN MATHS,PHYSICS AND CHEMISTRY RESPECTIVELY(separated by spaces): ").split()]
    assert m >= 0, "Please enter the valid marks obtained in maths"
    assert p >= 0, "Please enter the valid marks obtained in physics"
    assert c >= 0, "Please enter the valid marks obtained in chemistry"


except AssertionError as e:
    print(e)
else:
    if m < 35 or p < 35 or c < 35:
        if m < 35:
            print(f"You have failed in Maths by {100 - m} marks")
        if p < 35:
            print(f"You have failed in Physics by {100 - p} marks")
        if c < 35:
            print(f"You have failed in Chemistry by {100 - c} marks")
        print("You have failed the Examination.Better luck next time")
    else:
        average = round((m + p + c) / 3, 3)
        if average <= 59 and average >= 35:
            print("C GRADE")
        elif average <= 69 and average > 59:
            print("B GRADE")
        else:
            print("A GRADE")
