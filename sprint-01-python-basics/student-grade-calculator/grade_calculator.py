name = input("Enter student name:")
marks_Math = int(input("Enter Marks for Math:"))
marks_Science = int(input("Enter Marks for Science:"))
marks_English = int(input("Enter Marks for English:"))
marks_History = int(input("Enter Marks for History:"))
marks_Geography = int(input("Enter Marks for Geography:"))

total = marks_Math + marks_Science + marks_English + marks_History +marks_Geography

average = total / 5

grade = A
print("----------------------------------------")
print(" Student Report ")
print(" ----------------------------------------")

print("Student Name : {name}")

print(f"Math      : {marks_Math}")

print(f"Science   : {marks_Science}")

print(f"English   : {marks_English}")

print(f"History   : {marks_History}")

print(f"Geography  : {marks_Geography}")

print("----------------------------------------")

print(f"Total     : {total}")

print(f"Average   : {average}")

print(f"Grade      : {grade}")

