def calculategrade(marks):
    if(marks>=75): print("A grade")
    elif(marks>55): print("B grade")
    elif(marks>35):print("C grade")
    else: print("Fail")
def main():
    student_name = input("Enter the student's name: ")
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i} (out of 100): "))
        marks.append(mark)
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    grade = calculategrade(percentage)
    print("\nStudent Grade Report")
    print(f"Name: {student_name}")
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
main()