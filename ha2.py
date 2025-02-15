import pandas as pd
import numpy as np

# 1. Types of Data That Can Be Used to Create a Series in Pandas
# (No code needed; just theory)

# 2. Create a Series Having the Month's Number as Data and Assign Names as Index
months = pd.Series(
    data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    index=["January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December"]
)
print("Series of Months:")
print(months)
print("\n" + "-"*40 + "\n")

# 3. Create a Series Using a Dictionary for Fresh Batch Groups
students_data = {
    "MatMIE": 30,
    "Mat DAIS": 25,
    "COMIE": 28,
    "COMEC": 32
}

students_series = pd.Series(students_data)
print("Series of Fresh Batch Groups:")
print(students_series)
print("\n" + "-"*40 + "\n")

# 4. Create and Display a DataFrame from a Dictionary
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print("Exam DataFrame:")
print(df)
print("\n" + "-"*40 + "\n")

# 5. Select Rows Where the Number of Attempts is Greater Than 2
filtered_df = df[df['attempts'] > 2]
print("Number of attempts in the examination is greater than 2:")
print(filtered_df)
