"""
Python Data Analysis Practice - NumPy & pandas Solutions
This script contains all the code examples from answers.md
"""

import numpy as np
import pandas as pd
import time

print("=" * 60)
print("NumPy & pandas Practice Solutions")
print("=" * 60)

# ============================================================================
# 1. NumPy – Beginner
# ============================================================================
print("\n" + "=" * 60)
print("1. NumPy – Beginner")
print("=" * 60)

# 1. Create a 1D array
print("\n1. Create a 1D array:")
arr = np.arange(1, 11)
print(f"   arr = {arr}")

# 2. Create a 2D array
print("\n2. Create a 2D array:")
arr2d = np.arange(1, 10).reshape(3, 3)
print(f"   arr2d =\n{arr2d}")

# 3. Array of zeros and ones
print("\n3. Array of zeros and ones:")
zeros = np.zeros(10)
ones = np.ones(10)
print(f"   zeros = {zeros}")
print(f"   ones = {ones}")

# 4. Array with a specific step
print("\n4. Array with a specific step:")
even = np.arange(0, 21, 2)
print(f"   even = {even}")

# 5. Basic element-wise operations
print("\n5. Basic element-wise operations:")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
add = a + b
mul = a * b
square = a ** 2
print(f"   a + b = {add}")
print(f"   a * b = {mul}")
print(f"   a ** 2 = {square}")

# 6. Array shape and reshaping
print("\n6. Array shape and reshaping:")
arr = np.arange(12)
matrix = arr.reshape(3, 4)
shape = matrix.shape
ndim = matrix.ndim
print(f"   matrix =\n{matrix}")
print(f"   shape = {shape}")
print(f"   ndim = {ndim}")

# ============================================================================
# 2. NumPy – Intermediate
# ============================================================================
print("\n" + "=" * 60)
print("2. NumPy – Intermediate")
print("=" * 60)

# 7. Indexing and slicing
print("\n7. Indexing and slicing:")
m = np.arange(12).reshape(3, 4)
print(f"   Original matrix:\n{m}")
first_row = m[0, :]
last_col = m[:, -1]
submatrix = m[:2, :3]
print(f"   First row: {first_row}")
print(f"   Last column: {last_col}")
print(f"   Submatrix (first 2 rows, first 3 cols):\n{submatrix}")

# 8. Boolean indexing
print("\n8. Boolean indexing:")
arr = np.arange(21)
greater_than_10 = arr[arr > 10]
even = arr[arr % 2 == 0]
print(f"   Numbers > 10: {greater_than_10}")
print(f"   Even numbers: {even}")

# 9. Statistical methods
print("\n9. Statistical methods:")
rand_arr = np.random.randint(1, 101, size=10)
mean_val = rand_arr.mean()
median_val = np.median(rand_arr)
min_val = rand_arr.min()
max_val = rand_arr.max()
print(f"   Random array: {rand_arr}")
print(f"   Mean: {mean_val:.2f}")
print(f"   Median: {median_val:.2f}")
print(f"   Min: {min_val}")
print(f"   Max: {max_val}")

# 10. Random arrays and seeding
print("\n10. Random arrays and seeding:")
np.random.seed(42)
rand_matrix = np.random.randn(2, 3)
print(f"   Random matrix:\n{rand_matrix}")

# 11. Matrix multiplication
print("\n11. Matrix multiplication:")
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
prod = A @ B
print(f"   A =\n{A}")
print(f"   B =\n{B}")
print(f"   A @ B =\n{prod}")

# 12. Broadcasting
print("\n12. Broadcasting:")
matrix = np.ones((3, 3))
row = np.array([1, 2, 3])
result = matrix + row
print(f"   Matrix:\n{matrix}")
print(f"   Row: {row}")
print(f"   Result:\n{result}")

# ============================================================================
# 3. pandas – Beginner
# ============================================================================
print("\n" + "=" * 60)
print("3. pandas – Beginner")
print("=" * 60)

# 13. Create a Series
print("\n13. Create a Series:")
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
val_c = s['c']
print(f"   Series:\n{s}")
print(f"   Value at 'c': {val_c}")

# 14. Create a DataFrame from a dict
print("\n14. Create a DataFrame from a dict:")
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [20, 22, 19, 21],
    'score': [85, 70, 95, 60]
}
students = pd.DataFrame(data)
print(f"   Students DataFrame:\n{students}")

# 15. Read data from CSV (skipped - file doesn't exist)
print("\n15. Read data from CSV:")
csv_path = 'students.csv'
try:
    students_csv = pd.read_csv(csv_path)
    # normalize column names to lowercase for consistency
    students_csv.columns = [c.strip().lower() for c in students_csv.columns]
    print(f"   Loaded {csv_path}:\n{students_csv}")
    # Replace the in-memory `students` DataFrame with CSV contents
    students = students_csv
except Exception as e:
    print(f"   Could not read {csv_path}: {e}")
    print("   Using previously defined `students` DataFrame (in-memory example).")


# 16. Basic DataFrame info
print("\n16. Basic DataFrame info:")
print(f"   Columns: {list(students.columns)}")
print(f"   Data types:\n{students.dtypes}")
print(f"   Describe:\n{students.describe()}")

# 17. Selecting rows and columns
print("\n17. Selecting rows and columns:")
name_score = students[['name', 'score']]
older_than_20 = students[students['age'] > 20]
print(f"   Name and Score columns:\n{name_score}")
print(f"   Students older than 20:\n{older_than_20}")

# ============================================================================
# 4. pandas – Intermediate
# ============================================================================
print("\n" + "=" * 60)
print("4. pandas – Intermediate")
print("=" * 60)

# 18. Filtering with conditions
print("\n18. Filtering with conditions:")
df = pd.DataFrame({
    'city': ['NYC', 'LA', 'Chicago', 'Miami'],
    'temperature': [25, 35, 20, 32],
    'humidity': [60, 45, 70, 55]
})
hot = df[df['temperature'] > 30]
hot_and_dry = df[(df['temperature'] > 30) & (df['humidity'] < 50)]
print(f"   Original DataFrame:\n{df}")
print(f"   Temperature > 30:\n{hot}")
print(f"   Temperature > 30 AND humidity < 50:\n{hot_and_dry}")

# 19. Adding and modifying columns
print("\n19. Adding and modifying columns:")
students['passed'] = students['score'] >= 50
students['score'] = students['score'] + 5
print(f"   Updated students DataFrame:\n{students}")

# 20. Handling missing values
print("\n20. Handling missing values:")
data_na = {
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6]
}
df_na = pd.DataFrame(data_na)
missing_bool = df_na.isna()
filled = df_na.fillna(0)
dropped = df_na.dropna()
print(f"   Original DataFrame:\n{df_na}")
print(f"   Missing values:\n{missing_bool}")
print(f"   Filled with 0:\n{filled}")
print(f"   Dropped rows:\n{dropped}")

# 21. Sorting
print("\n21. Sorting:")
sorted_by_score = students.sort_values('score', ascending=False)
sorted_multi = students.sort_values(['age', 'score'], ascending=[True, False])
print(f"   Sorted by score (descending):\n{sorted_by_score}")
print(f"   Sorted by age (asc) then score (desc):\n{sorted_multi}")

# 22. Grouping and aggregation
print("\n22. Grouping and aggregation:")
data_emps = {
    'department': ['IT', 'IT', 'HR', 'HR', 'Sales'],
    'employee': ['A', 'B', 'C', 'D', 'E'],
    'salary': [50000, 60000, 45000, 47000, 52000]
}
emps = pd.DataFrame(data_emps)
avg_salary = emps.groupby('department')['salary'].mean()
total_salary = emps.groupby('department')['salary'].sum()
print(f"   Employees DataFrame:\n{emps}")
print(f"   Average salary by department:\n{avg_salary}")
print(f"   Total salary by department:\n{total_salary}")

# 23. Merging / joining DataFrames
print("\n23. Merging / joining DataFrames:")
left = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})
right = pd.DataFrame({
    'student_id': [1, 2, 2, 3],
    'course': ['Math', 'Math', 'CS', 'History']
})
merged = pd.merge(left, right, on='student_id')
print(f"   Left DataFrame:\n{left}")
print(f"   Right DataFrame:\n{right}")
print(f"   Merged DataFrame:\n{merged}")

# ============================================================================
# 5. Advanced NumPy & pandas
# ============================================================================
print("\n" + "=" * 60)
print("5. Advanced NumPy & pandas")
print("=" * 60)

# 24. Vectorization vs loops
print("\n24. Vectorization vs loops:")
arr = np.random.rand(1_000_000)

# loop
start = time.time()
sq_loop = np.empty_like(arr)
for i in range(len(arr)):
    sq_loop[i] = arr[i] ** 2
end = time.time()
loop_time = end - start

# vectorized
start = time.time()
sq_vec = arr ** 2
end = time.time()
vec_time = end - start

print(f"   Loop time: {loop_time:.4f} seconds")
print(f"   Vectorized time: {vec_time:.4f} seconds")
print(f"   Speedup: {loop_time/vec_time:.2f}x faster")

# 25. Custom function on arrays
print("\n25. Custom function on arrays:")
def normalize(x):
    x = np.asarray(x)
    x_min = x.min()
    x_max = x.max()
    return (x - x_min) / (x_max - x_min)

arr = np.random.randint(0, 100, size=10)
norm_arr = normalize(arr)
print(f"   Original array: {arr}")
print(f"   Normalized array: {norm_arr}")

# 26. Multi-indexing
print("\n26. Multi-indexing:")
data_mi = {
    'city': ['London', 'London', 'Paris', 'Paris'],
    'year': [2020, 2021, 2020, 2021],
    'population': [9.0, 9.1, 2.2, 2.3]
}
df_mi = pd.DataFrame(data_mi)
df_mi = df_mi.set_index(['city', 'year'])
london = df_mi.loc['London']
london_2020 = df_mi.loc[('London', 2020)]
print(f"   Multi-index DataFrame:\n{df_mi}")
print(f"   London data:\n{london}")
print(f"   London 2020: {london_2020['population']}")

# 27. Pivot tables
print("\n27. Pivot tables:")
data_pivot = {
    'region': ['North', 'North', 'South', 'South'],
    'product': ['A', 'B', 'A', 'B'],
    'sales': [100, 150, 80, 200]
}
sales_df = pd.DataFrame(data_pivot)
pivot = sales_df.pivot_table(
    values='sales',
    index='region',
    columns='product',
    aggfunc='sum',
    fill_value=0
)
print(f"   Sales DataFrame:\n{sales_df}")
print(f"   Pivot table:\n{pivot}")

# 28. Apply and lambda
print("\n28. Apply and lambda:")
def grade_from_score(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Reset students DataFrame for this example
students = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [20, 22, 19, 21],
    'score': [85, 70, 95, 60]
})
students['grade'] = students['score'].apply(grade_from_score)
print(f"   Students with grades:\n{students}")

# ============================================================================
# 6. Real-World Style Questions
# ============================================================================
print("\n" + "=" * 60)
print("6. Real-World Style Questions (Mini Projects)")
print("=" * 60)

# 29. Sales analysis
print("\n29. Sales analysis:")
sales = pd.DataFrame({
    'order_id': [1, 2, 3, 4],
    'date': ['2025-01-01', '2025-01-01', '2025-01-02', '2025-01-02'],
    'customer_id': [101, 102, 101, 103],
    'product': ['A', 'B', 'A', 'C'],
    'quantity': [2, 1, 3, 5],
    'price': [10.0, 20.0, 10.0, 5.0]
})

sales['revenue'] = sales['quantity'] * sales['price']
total_revenue = sales['revenue'].sum()
revenue_by_product = (
    sales.groupby('product')['revenue']
         .sum()
         .sort_values(ascending=False)
)
top3_products = revenue_by_product.head(3)
num_unique_customers = sales['customer_id'].nunique()
daily_revenue = sales.groupby('date')['revenue'].sum()

print(f"   Sales DataFrame:\n{sales}")
print(f"   Total revenue: ${total_revenue:.2f}")
print(f"   Top 3 products by revenue:\n{top3_products}")
print(f"   Number of unique customers: {num_unique_customers}")
print(f"   Daily revenue:\n{daily_revenue}")

# 30. Customer behavior
print("\n30. Customer behavior:")
revenue_per_customer = (
    sales.groupby('customer_id')['revenue']
         .sum()
         .sort_values(ascending=False)
)
top5_customers = revenue_per_customer.head(5)
total_revenue = sales['revenue'].sum()
num_orders = sales['order_id'].nunique()
avg_order_value = total_revenue / num_orders

print(f"   Revenue per customer:\n{revenue_per_customer}")
print(f"   Top 5 customers:\n{top5_customers}")
print(f"   Average order value: ${avg_order_value:.2f}")

# 31. Time series analysis
print("\n31. Time series analysis:")
df_ts = sales[['date', 'revenue']].copy()
df_ts['date'] = pd.to_datetime(df_ts['date'])
df_ts = df_ts.set_index('date').sort_index()
monthly_revenue = df_ts['revenue'].resample('ME').sum()

print(f"   Time series DataFrame:\n{df_ts}")
print(f"   Monthly revenue:\n{monthly_revenue}")

# 32. Employee performance
print("\n32. Employee performance:")
perf = pd.DataFrame({
    'employee_id': [1, 2, 3, 4],
    'department': ['IT', 'IT', 'HR', 'Sales'],
    'month': ['2025-01', '2025-01', '2025-01', '2025-01'],
    'tasks_completed': [50, 60, 40, 70],
    'hours_worked': [160, 150, 155, 165]
})

perf['tasks_per_hour'] = perf['tasks_completed'] / perf['hours_worked']
avg_tph_by_dept = perf.groupby('department')['tasks_per_hour'].mean()
top3_employees = perf.sort_values('tasks_per_hour', ascending=False).head(3)

print(f"   Performance DataFrame:\n{perf}")
print(f"   Average tasks per hour by department:\n{avg_tph_by_dept}")
print(f"   Top 3 employees:\n{top3_employees[['employee_id', 'department', 'tasks_per_hour']]}")

# 33. Real dataset cleanup (example pattern - skipped as it requires external file)
print("\n33. Real dataset cleanup and summary:")
print("   (Skipped - requires external CSV file)")
print("   Example pattern:")
print("   - Load: df = pd.read_csv('dataset.csv')")
print("   - Inspect: df.head(), df.info()")
print("   - Clean: handle missing values, fix data types, remove duplicates")
print("   - Summarize: df.describe(), groupby(), correlations")

print("\n" + "=" * 60)
print("All examples completed successfully!")
print("=" * 60)

