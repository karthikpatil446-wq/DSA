def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Swap for descending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# Read 6 subject marks
marks = []
print("Enter marks for 6 subjects:")
for i in range(6):
    mark = int(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

# Sort using bubble sort
sorted_marks = bubble_sort_desc(marks)

# Display report
print("\n=== Student Marks Report ===")
print("Marks from highest to lowest:")
for m in sorted_marks:
    print(m)
    #outpiut
"""    Enter marks for 6 subjects:
Enter mark for subject 1: 54
Enter mark for subject 2: 88
Enter mark for subject 3: 95
Enter mark for subject 4: 78
Enter mark for subject 5: 12 
Enter mark for subject 6: 54

=== Student Marks Report ===
Marks from highest to lowest:
95
88
78
54
54
12"""