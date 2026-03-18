# Calculate Average Marks

n = int(input("Enter number of subjects: "))

total = 0

for i in range(n):
    marks = float(input("Enter marks: "))
    total += marks

average = total / n

print("Total Marks =", total)
print("Average Marks =", average)