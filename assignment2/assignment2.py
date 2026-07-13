# Task 2: Read a CSV file
import csv
try: 
    def read_employees():
        employee_dict = {}
        rows = []
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    employee_dict["fields"] = row
                else:
                    rows.append(row)
        employee_dict["rows"] = rows
        return employee_dict
except Exception as e:
   print(f"An error occurred: {e}")
   
employees = read_employees()
print(employees)

# Task 3: Find the Column Index
def column_index(employee_id):
    try:
        index = employees["fields"].index(employee_id)
        return index
    except Exception as e:
        print(f"An error occurred: {e}")
 
employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    try:
        first_names_index = column_index("first_name")
        first_names = employees["rows"][row_number][first_names_index]
        return first_names
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 5: Find the Employee Function
def employee_find(employee_id):
   try:
       def employee_match(row):
           return int(row[employee_id_column]) == employee_id 
       matches=list(filter(employee_match, employees["rows"]))
       return matches
   except Exception as e:
       print(f"An error occurred: {e}")

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   try:
       matches = list(filter(lambda row : 
            int(row[employee_id_column]) 
            == employee_id, 
            employees["rows"]))
       return matches
   except Exception as e:
       print(f"An error occurred: {e}")

# Task 7: Sort the Rows by last_name Using a Lamba
def sort_by_last_name():
    try:
        employees["rows"].sort(key = 
            lambda row: row[column_index("last_name")])
        return employees["rows"]
    except Exception as e:
       print(f"An error occurred: {e}")

# Task 8: Create a dict for an Employee
def employee_dict(row): 
    try:
        dict_result = {}
        headers = employees["fields"]
        for key, value in zip(headers, row):
            if key != "employee_id":
                dict_result[key] = value
        return dict_result
    except Exception as e:
       print(f"An error occurred: {e}")

# Task 9: A dict of dicts, for All Employees
def all_employees_dict(): 
    try:
        all_employees_dict = {}
        for row in employees["rows"]:
            employee_id = row[employee_id_column]
            all_employees_dict[employee_id] = employee_dict(row)
        return all_employees_dict
    except Exception as e:
       print(f"An error occurred: {e}")

# Task 10: Use of the os Module 
import os 

def get_this_value():
    try:
        return os.environ["THISVALUE"]
    except Exception as e:
       print(f"An error occurred: {e}")

# Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    try:
        custom_module.secret = str(new_secret)
        return new_secret
    except Exception as e:
       print(f"An error occurred: {e}")

print(set_that_secret("new secret"))
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    try:
        minutes1_dict = {}
        minutes1 = []
        minutes2_dict = {}
        minutes2 = []
        with open("../csv/minutes1.csv", "r") as file1:
            reader = csv.reader(file1)
            for i, row in enumerate(reader):
                if i == 0:
                    minutes1_dict["fields"] = row
                else:
                    minutes1.append(tuple(row))
                    minutes1_dict["rows"] = minutes1
        with open("../csv/minutes2.csv", "r") as file2:
            reader = csv.reader(file2)
            for i, row in enumerate(reader):
                if i == 0:
                    minutes2_dict["fields"] = row
                else:
                    minutes2.append(tuple(row))
                    minutes2_dict["rows"] = minutes2
        return minutes1_dict, minutes2_dict
    except Exception as e:
       print(f"An error occurred: {e}")

minutes1, minutes2 = read_minutes()

# Task 13: Create minutes_set
def create_minutes_set():
    try:
        minutes1_set = set(minutes1["rows"])
        minutes2_set = set(minutes2["rows"])
        minutes = minutes1_set.union(minutes2_set)
        return minutes
    except Exception as e:
       print(f"An error occurred: {e}")

minutes_set = create_minutes_set()

# Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    try:
        minutes_list = list(minutes_set)
        new_date = tuple(map(lambda minutes_list: (minutes_list[0], 
            datetime.strptime(minutes_list[1], "%B %d, %Y")), minutes_list))
        return list(new_date)
    except Exception as e:
       print(f"An error occurred: {e}")

minutes_list = create_minutes_list()

# Task 15: Write Out Sorted List
def write_sorted_list():
    try:
        minutes_sorted_list = sorted(minutes_list, key=lambda x:x[1])
        new_date = list(map(lambda minutes_sorted_list: (minutes_sorted_list[0], 
            datetime.strftime(minutes_sorted_list[1], "%B %d, %Y")), minutes_sorted_list))
        with open("./minutes.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(new_date)
        return new_date 
    except Exception as e:
       print(f"An error occurred: {e}")

write_sorted_list()