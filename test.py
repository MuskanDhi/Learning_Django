import numpy as np
# print(np.array([1,2,3]))
# print(np.zeros((2,2)))
# print(np.ones((2,2)))
# print(np.full((2,2),7))
# print(np.eye(3))
# print(np.arange(0,11,2))
# print(np.linspace(0,1,5))
# print(np.random.rand(3,3))
# print(np.random.randn(3,3))
# print(np.random.randint(0,10,size=5))
# print(np.empty((2,2)))

# a = np.array([[1,2,3],[4,5,6]])
# print(a.shape)
# print(a.ndim)
# print(a.size)
# print(a.dtype)

# a = np.array([1, 2, 3], dtype=np.float32)
# print(a.dtype)
# b = a.astype(np.int64)
# print(b.dtype)
# print(a.dtype)

# 1D array question

# a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# # Q1. Print the element at index 4.
# print(a[4])

# # Q2. Print the last element of the array.
# print(a[-1])

# # Q3. Print the first 5 elements.
# print(a[:5])

# # Q4. Print the last 3 elements.
# print(a[7:])

# # Q5. Print all elements from index 2 to index 6 (exclusive of 6).
# print(a[2:6])

# # Q6. Print every alternate element (i.e., 0th, 2nd, 4th, ...).
# print(a[::2])

# # Q7. Print the array in reverse order.
# print(a[::-1])

# # Q8. Print all elements except the first and last.
# print(a[1:9])

# # Q9. Replace the value at index 3 with 999, then print the whole array.
# # a[3] = 999
# # print(a)

# # Q10. Print all elements greater than 50 (using boolean indexing).
# print(a[a>50])

# # Q11. Print elements at index 1, 3, and 5 using fancy indexing.
# print(a[[1,3,5]])

# # Q12. Print the sum of all elements from index 5 to the end.
# print(a[5:].sum())

# # Q13. Create a copy of the sub-array from index 0 to 3, modify the copy's first element to 0, and print both the original array and the copy to prove they're independent.
# b = a[:4].copy()
# b[0] = 0
# print(b)
# print(a)

# # Q14. Print the array with all values greater than 70 replaced by 0 (in-place, using conditional assignment).
# a[a>70] = 0
# print(a)

# # Q15. Print the middle element of the array (without hardcoding the index number — use len(a)).
# print(a[len(a)//2])


# 2d array
# b = np.array([[1,2,3],[4,5,6]])
# print(b[0, 1])
# print(b[:, 1])
# print(b[1, :])

# 2d array question
# a = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])

# Q1. Print the shape of the array.
# print(a.shape)

# Q2. Print the element at row 1, column 2.
# print(a[1,2])

# Q3. Print the entire first row.
# print(a[0,:])

# Q4. Print the entire last column.
# print(a[:,3])

# Q5. Print the entire second column (index 1).
# print(a[:,1])

# Q6. Print the sub-array containing rows 0 and 1, and columns 1 to 3.
# print(a[:2, 1:4])

# Q7. Print the last row using negative indexing.
# print(a[-1,:])

# Q8. Print the transpose of the array.
# print(a.T)
# print(a.transpose())

# Q9. Replace the element at row 2, column 0 with 999, then print the whole array.
# a[2,0] = 999
# print(a)

# Q10. Print all elements greater than 50 (using boolean indexing — note the result will be flattened to 1D).
# print(a[a>50])

# Q11. Print only the diagonal elements of the array (hint: look up np.diagonal() or use indexing).
# print(np.diagonal(a))

# Q12. Print the sum of each column (i.e., sum down each row — think about which axis).
# print(a.sum(axis=0))

# Q13. Print the sum of each row (i.e., sum across each column — think about which axis).
# print(a.sum(axis=1))

# Q14. Print the maximum value in the entire array, and separately, the maximum value in each column.
# print(a.max())
# print(a.max(axis=0))

# Q15. Create a copy of row 0, change the first element of the copy to 0, then print both the original array and the copy to confirm they're independent.
# b = a[0,:].copy()
# b[0] = 0
# print(b)
# print(a)

# Q16. Reshape the array into a shape of (2, 6), and print the result.
# print(a.reshape(2,6))

# Q17. Flatten the 2D array into a 1D array and print it.
# print(a.reshape(-1))
# print(a.flatten())

# Q18. Print every row except the last one.
# print(a[:-1,:])

# Q19. Print the second and third rows only (rows at index 1 and 2), using fancy indexing with a list of row indices.
# print(a[[1,2]])

# Q20. Replace all values greater than 100 with 0 (in-place, using conditional assignment), then print the array.
# a[a>100] = 0
# print(a)

# a = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print(a[0,0])
# print(a[1,1])
# print(a[2,2])
# print(a[1,0])
# print(a[0,:])
# print(a[2,:])
# print(a[:,0])
# print(a[:,1])
# print(a[:,-1])
# print(a[[0,1],:-1])
# print(a[[0,1],1:])
# print(a[[1,2],:-1])
# print(a[[1,2],1:])
# print(a[[1,2]])

# a = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130, 140, 150, 160]
# ])

# print(a[[1,2],1:-1])
# print(a[:-1,2:])

# A DataFrame - a full table
import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35]
# }
# df = pd.DataFrame(data)
# print(df)
# df = pd.read_csv('results.csv')
# print(df.head())
# print(df.tail())
# print(df.shape)    
# print(df.info())   
# print(df.describe())

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 28],
#     'City': ['Delhi', 'Mumbai', 'Chennai', 'Pune']
# }
# df = pd.DataFrame(data)

# Select and print just the 'City' column as a Series.
# print(df['City'])

# Select and print 'Name' and 'City' together as a DataFrame.
# print(df[['Name', 'City']])

# Use .loc to print the row where Name == 'Charlie' (hint: set index to Name first, or filter).
# print(df.loc[df['Name'] == 'Charlie'])

# Use .iloc to print the last row of the DataFrame.
# print(df.iloc[-1:])

# Use .iloc to print rows 1 and 2 only (slicing).
# print(df.iloc[1:3])



# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 28],
#     'City': ['Delhi', 'Mumbai', 'Chennai', 'Pune']
# }
# df = pd.DataFrame(data)

# Filter and print rows where Age is greater than 27.
# print(df[df['Age'] > 27])

# Filter and print rows where City is exactly 'Delhi'.
# print(df[df['City'] == 'Delhi'])

# Filter and print rows where Age > 25 AND City == 'Pune'.
# print(df[(df['Age'] > 25) & (df['City'] == 'Pune')])

# Filter and print rows where City is either 'Delhi' OR 'Chennai', using .isin().
# print(df[df['City'].isin(['Delhi','Chennai'])])

# Filter and print rows where Name contains the letter 'a' (case-sensitive — check what you get vs a lowercase-only search).
# print(df[df['Name'].str.contains('a')])

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 28],
#     'City': ['Delhi', 'Mumbai', 'Chennai', 'Pune']
# }
# df = pd.DataFrame(data)

# Add a new column 'Age_plus_10' that's Age + 10.
# df['Age_plus_10'] = df['Age'] + 10
# print(df['Age_plus_10'])

# Add a column 'Is_Adult' that's True if Age >= 18, else False (hint: use .apply() with a lambda, or simply df['Age'] >= 18 directly).
# df['Is_Adult'] = df['Age'].apply(lambda x: 'True' if x >= 18 else 'False')
# df['Is_Adult'] = df['Age'] >= 18
# print(df)

# Rename 'City' to 'Location' — and make sure the change actually sticks on df (using either method above).
# df.rename(columns={'City': 'Location'}, inplace=True)
# print(df)

# Drop the 'Age_plus_10' column.
# df.drop(columns={'Age_plus_10'}, inplace=True)
# print(df)

# Drop the row at index 2 (Charlie) and print the result — notice what happens to the index numbering afterward.
# df.drop(2, inplace=True)
# print(df)

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, np.nan, 35, np.nan, 22],
#     'City': ['Delhi', 'Mumbai', np.nan, 'Pune', 'Delhi'],
#     'Salary': [50000, 60000, np.nan, 45000, 52000]
# }
# df = pd.DataFrame(data)

# Print how many missing values exist in each column.
# print(df.isnull().sum())

# Drop all rows that have ANY missing value, print the result.
# print(df.dropna())

# Instead, fill missing Age values with the column's mean.
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# print(df)

# Fill missing City values with the string 'Unknown'.
# df['City'] = df['City'].fillna('Unknown')
# print(df)

# Fill missing Salary values with the column's median instead of mean — check .median() vs .mean() and think about when median might be a better choice (hint: outliers).
# An outlier is a value that is very different from most of the other values in a dataset.
# Mean → sensitive to outliers
# Median → less sensitive to outliers
# df['Salary'] = df['Salary'].fillna(df['Salary'].median())
# print(df)

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, 35, 22, 30, 28],
#     'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai'],
#     'Salary': [50000, 65000, 42000, 58000, 61000]
# }
# df = pd.DataFrame(data)

# Sort by Age ascending, print the result.
# print(df.sort_values('Age', ascending=True))

# Sort by Salary descending, print the result.
# print(df.sort_values('Salary', ascending=False))

# Sort by City first, then Age within each city.
# print(df.sort_values(['City', 'Age']))

# Sort by Age descending, then reset the index cleanly (no leftover old-index column).
# df_sorted = df.sort_values('Age', ascending=False).reset_index(drop=True)
# print(df_sorted)

# After sorting by Age, use sort_index() to bring it back to the original row order — confirm it matches the very first unsorted DataFrame.
# sorted_df = df.sort_values('Age')
# original_order = sorted_df.sort_index()
# print(original_order)
# print(original_order.equals(df))

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
#     'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai', 'Delhi'],
#     'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
#     'Salary': [50000, 65000, 42000, 58000, 61000, 47000]
# }
# df = pd.DataFrame(data)

# Group by City and find the average Salary per city.
# print(df.groupby('City')['Salary'].mean())

# Group by City and find the count of employees per city (try both .count() on Salary and .size() — compare).
# print(df.groupby('City')['Salary'].agg(['count', 'size']))

# Group by City and get mean, max, and min of Salary all at once using .agg().
# print(df.groupby('City') ['Salary'].agg(['mean', 'max', 'min']))

# Group by both City AND Department, and find the average Salary for each combination.
# print(df.groupby(['City', 'Department'])['Salary'].mean())

# Take the result from step 1, and use .reset_index() so City becomes a normal column again instead of the index.
# print(df.groupby('City')['Salary'].mean().reset_index())



# Inner Join (default) — only matching rows
# Left Join — keep everything from the left table
# Right Join — keep everything from the right table
# Outer Join — keep everything from both sides

# students = pd.DataFrame({
#     'student_id': [1, 2, 3, 4],
#     'Name': ['Riya', 'Aman', 'Sara', 'Vikram']
# })

# marks = pd.DataFrame({
#     'student_id': [1, 2, 3, 5],
#     'Marks': [85, 90, 78, 60]
# })

# Perform an inner join on student_id — print the result and note who got dropped.
# print(pd.merge(students, marks, on="student_id", how="inner"))

# Perform a left join — print the result and note what happens to Vikram's Marks.
# print(pd.merge(students, marks, on="student_id" ,how="left"))

# Perform a right join — print the result and note what happens to student_id=5's Name.
# print(pd.merge(students, marks, on="student_id", how="right"))

# Perform an outer join — print the result and confirm it includes both Vikram AND the mystery student_id=5.
# print(pd.merge(students, marks, on="student_id", how="outer"))

# Count how many NaN values appear in the outer join result using .isnull().sum().
# print(pd.merge(students, marks, on="student_id", how="outer").isnull().sum())

# q1_sales = pd.DataFrame({
#     'Product': ['Pen', 'Notebook', 'Eraser'],
#     'Revenue': [1000, 2000, 500]
# })

# q2_sales = pd.DataFrame({
#     'Product': ['Pen', 'Marker', 'Notebook'],
#     'Revenue': [1200, 800, 2200]
# })

# Concatenate q1_sales and q2_sales row-wise (stack them), print the result — notice the repeated index.
# print(pd.concat([q1_sales, q2_sales]))

# Repeat step 1, but this time reset the index cleanly.
# print(pd.concat([q1_sales, q2_sales]).reset_index(drop=True))

# Create two small DataFrames with matching row order (e.g., Name and Score) and concatenate them column-wise (axis=1).
# print(pd.concat([q1_sales,q2_sales], axis=1))
# names = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie']
# })

# scores = pd.DataFrame({
#     'Score': [85, 90, 78]
# })

# print(pd.concat([names, scores], axis=1))

# Create two DataFrames where one has an extra column the other doesn't (like the df1/df2 example above), concatenate them row-wise, and observe where NaN shows up.
# df1 = pd.DataFrame({
#     'Name': ['Alice', 'Bob'],
#     'Age': [25, 30]
# })

# df2 = pd.DataFrame({
#     'Name': ['Charlie', 'David'],
#     'Salary': [50000, 60000]
# })

# print(pd.concat([df1, df2], ignore_index=True))

# In your own words (just a sentence), explain to yourself when you'd reach for merge() instead of concat().
# Use concat() when you want to stack or combine DataFrames, and use merge() when you want to combine related DataFrames based on a common key/column.



# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Math': [80, 45, 90],
#     'Science': [85, 50, 95]
# })

# Use .map() to create a new column 'First_Letter' that holds just the first letter of each Name (hint: x[0]).
# df['First_Letter'] = df['Name'].map(lambda x: x[0])
# print(df)

# Use .apply() on the Math column to create a 'Math_Pass' column: 'Pass' if Math >= 50, else 'Fail'.
# df['Math_Pass'] = df['Math'].apply(
#     lambda x: 'Pass' if x >= 50 else 'Fail'
# )
# print(df)

# Use .apply(..., axis=1) to create a 'Total' column that's Math + Science for each row.
# df['Total'] = df.apply(
#     lambda row: row['Math'] + row['Science'],
#     axis=1
# )
# print(df)

# Use .apply(..., axis=1) to create a 'Result' column: 'Pass' only if BOTH Math and Science are >= 50, else 'Fail'.
# df['Result'] = df.apply(
#     lambda row: 'Pass' if row['Math'] >= 50 and row['Science'] >= 50 else 'Fail',
#     axis=1
# )
# print(df)

# Use .applymap() (or df[['Math','Science']].applymap(...)) to add 5 bonus marks to every value in the Math and Science columns at once.
# df[['Math', 'Science']] = df[['Math', 'Science']].applymap(
#     lambda x: x + 5
# )
# df[['Math', 'Science']] = df[['Math', 'Science']].map(
#     lambda x: x + 5
# )
# print(df)



# df = pd.DataFrame({
#     'Name': ['Riya', 'Aman', 'Riya', 'Sara', 'Aman', 'Vikram'],
#     'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai', 'Delhi'],
#     'Score': [85, 90, 85, 78, 90, 88]
# })

# Print df.duplicated() and identify which rows are flagged.
# print(df.duplicated())

# Print the total count of duplicate rows using .sum().
# print(df.duplicated().sum())

# Drop duplicates keeping the first occurrence — print the result.
# print(df.drop_duplicates(keep='first'))

# Drop duplicates keeping the last occurrence instead — compare which rows survive vs step 3.
# print(df.drop_duplicates(keep='last'))

# Suppose you only care about duplicate Name+City combinations (ignore Score). Use subset=['Name','City'] to find and drop those duplicates.
# print(df.duplicated(subset=['Name', 'City']))



# df = pd.DataFrame({
#     'Department': ['IT', 'HR', 'IT', 'Sales', 'IT', 'HR', 'Sales', 'IT'],
#     'Status': ['Active', 'Active', 'Inactive', 'Active', 'Active', 'Inactive', 'Active', 'Active']
# })

# Find the frequency count of each Department.
# print(df['Department'].value_counts())

# Find the frequency count of Department as percentages instead of raw counts (normalize=True).
# print(df['Department'].value_counts(normalize=True))

# Find the list of unique values in Status.
# print(df['Status'].unique())

# Find how many unique values exist in Department.
# print(df['Department'].nunique())

# Find which Department has the fewest occurrences (hint: look at the last row of value_counts(), or use .value_counts().idxmin()).
# print(df['Department'].idxmin())
# print(df['Department'].tail())



# df = pd.DataFrame({
#     'City': ['Delhi', 'Delhi', 'Mumbai', 'Mumbai', 'Delhi', 'Mumbai', 'Pune'],
#     'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'IT', 'HR'],
#     'Salary': [50000, 45000, 60000, 55000, 52000, 58000, 40000]
# })

# Create a pivot table showing average Salary by City (rows) and Department (columns).
# print(df.pivot_table(values='Salary', index='City', columns='Department', aggfunc='mean'))

# Change aggfunc to 'sum' instead of 'mean' — compare the results.
# print(df.pivot_table(values='Salary', index='City', columns='Department', aggfunc='sum'))

# Add fill_value=0 and observe what happens to the City/Department combination that doesn't exist in the data (Pune has no IT row).
# print(df.pivot_table(values='Salary', index='City', columns='Department', aggfunc='mean', fill_value=0))

# Add margins=True to include row/column totals.
# print(df.pivot_table(values='Salary', index='City', columns='Department', aggfunc='mean', margins=True))

# Recreate the same result using groupby(['City','Department'])['Salary'].mean() instead, and compare the output format to the pivot table.
# print(df.groupby(['City', 'Department'])['Salary'].mean())




# df = pd.DataFrame({
#     'student_id': [101, 102, 103, 104],
#     'Name': ['Riya', 'Aman', 'Sara', 'Vikram'],
#     'Marks': [85, 90, 78, 88]
# })

# Set student_id as the index, print the result.
# df = df.set_index('student_id')
# print(df)

# Using the new index, select the row for student_id=103 with .loc.
# print(df.loc[103])

# Reset the index back to default numbering, keeping student_id as a normal column again.
# df = df.reset_index()
# print(df)

# Reset the index again, but this time use drop=True and compare — what's different about the output?
# df = df.set_index('student_id')
# df = df.reset_index(drop=True)
# print(df)

# Create two small DataFrames sharing the same index values (like the Age/Salary example above) and combine them using .join().
# names = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie']
# })

# scores = pd.DataFrame({
#     'Score': [85, 90, 78]
# })

# print(names.join(scores))



# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['Delhi', 'Mumbai', 'Pune']
# })
# print(df)


# Save df to a CSV file called 'output.csv', making sure NOT to include the index column.
# df.to_csv('output.csv', index=False)

# Read 'output.csv' back into a new DataFrame and print it — confirm it matches the original.
# df = pd.read_csv('output.csv')
# print(df)

# Save df to 'output.json' using orient='records', then read it back with pd.read_json('output.json').
# df.to_json('output.json', orient='records')
# df_json = pd.read_json('output.json')
# print(df_json)

# Try reading 'output.csv' again, but this time using usecols=['Name'] — confirm only that column loads.
# df = pd.read_csv('output.csv', usecols=['Name'])
# print(df)

# Deliberately save df WITHOUT index=False this time, read it back, and observe the extra unwanted column that appears.
# df.to_csv('output.csv')



df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 55000, 52000]
})

# Try df[df['Age'] > 27]['Salary'] = 0 — see if you get the warning (behavior can vary slightly by Pandas version, but the pattern itself is always risky).


# Fix it the safe way using .copy(): create an independent subset where Age > 27, then set Salary to 0 in that copy — confirm the original df is unaffected.


# Now do it the OTHER safe way: directly modify df using .loc[condition, 'Salary'] = 0 for rows where Age > 27 — confirm df itself changed this time.


# In your own words, explain when you'd want .copy() (independent) vs .loc[...] = (modify original) — think of a real scenario for each.


# Bonus: try chained indexing with two brackets, like df['Salary'][df['Age']>27] = 0, and compare to .loc — which is considered the safer, recommended style?