




print("SELECT ANY ONE OPTION : 1. ADD SCORE AND STUDENT NAME 2. VIEW ALL STUDENT SCORES 3. UPDATE STUDENT'S SCORE 4. DELETE STUDENT'S SCORE 5. CALCULAYE STATISTICS 6.SAVE A RECORD TO A FILE 7.LOAD RECORDS WHEN PROGRAM STARTS")

choice = int(input("Enter option: "))

if choice ==1 :
    student_name = input("Enter the name of the student: ")
    student_score= int(input("Enter the scoer of the student: "))
    score = {student_name, student_score}
    print("Succesfully added")

elif choice == 2:
    with open('student_records.txt', 'r') as file:
        content = file.read()
        print(content)
elif choice == 3:
    with open('student_records.txt', 'r') as file:
        content = file.read()
        updated_score = input("Enter the score of the student you want to update")
        updated_content = content.replace(student_score, updated_score)
        with open('data.txt', 'w') as file:
            file.write(updated_content)
elif choice == 4:
    




