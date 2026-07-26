# Task 3: List Comprehensions Practice
import csv

with open('../csv/employees.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    employeeNames_list = []
    for row in reader:
        employeeNames_list.append(row)
    employeeNames = [name[1] + ' ' + name[2] for name in employeeNames_list] # Create first and last name list

print(employeeNames)

# Create list with only names that contain the letter "e"
eNames = [name for name in employeeNames if "e" in name.lower()]
print(eNames)