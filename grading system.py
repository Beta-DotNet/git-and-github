
def get_grade(grade):
    if grade >= 0 and grade <= 100:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

score = int(input("Enter Score: "))
print(get_grade(score))