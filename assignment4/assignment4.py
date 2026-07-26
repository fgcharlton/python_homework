# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
import pandas as pd

# Create a DataFrame from a dictionary:
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# Add a new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print(task1_with_salary)

# Modify an existing column:
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print(task1_older)

# Save the DataFrame as a CSV file:
task1_older.to_csv("employees.csv", index=False)

# Task 2: Loading Data from CSV and JSON
# Read data from a CSV file:
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

# Read data from a JSON file:
task2data = {
    "Name": ["Eve", "Frank"],
    "Age": [28, 40],
    "City": ["Miami", "Seattle"],
    "Salary": [60000, 95000]
}

task2_data_frame = pd.DataFrame(task2data)
task2_data_frame.to_json('additional_employees.json')
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# Combine DataFrames:
more_employees = pd.concat([task1_older, task2_data_frame], ignore_index=True)
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# Use the head() method:
first_three = more_employees.head(3)
print(first_three)

# Use the tail() method:
last_two = more_employees.tail(2)
print(last_two)

# Get the shape of a DataFrame
employee_shape = more_employees.shape
print(employee_shape)

# Use the info() method:
more_employees.info()

# Task 4: Data Cleaning
# Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)

clean_data = dirty_data.copy()

# Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()
print(clean_data)

# Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
clean_data["Age_missing"] = clean_data["Age"].isnull()
print(clean_data)

# Convert Salary to numeric and replace known place holders with (unknown, n/a) with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
clean_data["Salary_missing"] = clean_data["Salary"].isnull()
print(clean_data)

# Fill missing numeric values (use fillna). Fill Age with the mean and Salary with the median
mean_age = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)

median_salary = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)

print(clean_data)

# Convert Hire Data to datetime 
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print(clean_data)

median_date = clean_data["Hire Date"].median() # Handle missing dates with median date
clean_data["Hire Date"] = clean_data["Hire Date"].fillna(median_date)

# Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()

clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()

print(clean_data)
