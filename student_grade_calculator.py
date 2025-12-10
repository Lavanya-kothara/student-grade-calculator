def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

name = input("Enter student name: ")
marks = []

for i in range(5):
    m = float(input(f"Enter mark {i+1}: "))
    marks.append(m)

total = sum(marks)
avg = total / 5

grade = calculate_grade(avg)

print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", avg)
print("Grade:", grade)