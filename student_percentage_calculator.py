# Student Percentage Calculator
# Takes a student's name, marks obtained and total marks,
# then prints the percentage scored.

student = input("Enter Student Name: ")
marks_obtained = float(input("Marks Obtained: "))
total_marks = float(input("Total Marks: "))

percentage = (marks_obtained / total_marks) * 100

print(student, "scored", percentage, "%")
