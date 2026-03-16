first_grade = int(input("Enter with the first grade:"))
second_grade = int(input("Enter with the second grade:"))
third_grade = int(input("Enter with the third grade:"))

highest_grade = max(first_grade, second_grade, third_grade)
lowest_grade = min(first_grade, second_grade, third_grade)

print(f'Highest grade is {highest_grade}')
print(f'Lowest grade is {lowest_grade}')

