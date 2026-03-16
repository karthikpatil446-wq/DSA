n = int(input("Enter total number of subjects: "))

total_credits = 0
total_points = 0

for i in range(n):
    credit = int(input("Enter credit of subject: "))
    grade_point = int(input("Enter grade point of subject: "))

    total_credits += credit
    total_points += credit * grade_point

cgpa = total_points / total_credits

print("CGPA =", round(cgpa, 2))