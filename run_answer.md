# run_answer.py - Code Explanation

## Overview
This is a comprehensive Python script that demonstrates **NumPy and pandas** practical examples, ranging from beginner to advanced level. The script showcases how to work with arrays, data frames, and perform data analysis operations efficiently. It's designed as an educational resource to learn key concepts in numerical computing and data manipulation.

---

## 1. Initial Setup

### Code:
```python
"""
Python Data Analysis Practice - NumPy & pandas Solutions
This script contains all the code examples from answers.md
"""

import numpy as np
import pandas as pd
import time
```

### Explanation:
- **Docstring**: Describes the purpose of the script in triple quotes
- **`import numpy as np`**: Imports NumPy library with alias `np` for numerical operations on arrays
- **`import pandas as pd`**: Imports pandas library with alias `pd` for data frame operations
- **`import time`**: Imports time module to measure execution duration (useful for performance comparison)

### Why We Write This:
- Libraries provide pre-built functions for numerical/data operations (faster and more reliable than custom code)
- Aliases make code more concise and easier to read
- Time module helps benchmark performance comparisons

---

## 2. Section 1: NumPy – Beginner

### Why This Section:
NumPy is fundamental for numerical computing. These beginner examples show how to create and manipulate basic arrays.

### 1.1 Create a 1D Array
```python
arr = np.arange(1, 11)
print(f"   arr = {arr}")
```
**Why**: `np.arange()` efficiently creates arrays with sequential values. This is faster than using Python loops.

### 1.2 Create a 2D Array
```python
arr2d = np.arange(1, 10).reshape(3, 3)
print(f"   arr2d =\n{arr2d}")
```
**Why**: `.reshape()` transforms 1D array into 2D matrix (3×3). Useful for matrix operations and multi-dimensional data.

### 1.3 Array of Zeros and Ones
```python
zeros = np.zeros(10)
ones = np.ones(10)
```
**Why**: These are commonly used initializers in machine learning and numerical algorithms.

### 1.4 Array with Specific Step
```python
even = np.arange(0, 21, 2)
```
**Why**: The step parameter (third argument) creates arrays with custom increments. Here, it creates even numbers 0-20.

### 1.5 Element-wise Operations
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
add = a + b       # [5, 7, 9]
mul = a * b       # [4, 10, 18]
square = a ** 2   # [1, 4, 9]
```
**Why**: NumPy allows operations on entire arrays without loops. This is **vectorization** - much faster than looping.

### 1.6 Array Shape and Reshaping
```python
shape = matrix.shape  # Returns (3, 4)
ndim = matrix.ndim    # Returns 2 (number of dimensions)
```
**Why**: Understanding array dimensions is critical for debugging shape mismatches and performing correct operations.

---

## 3. Section 2: NumPy – Intermediate

### Why This Section:
These examples show more advanced array manipulation, indexing, and statistical operations.

### 2.7 Indexing and Slicing
```python
first_row = m[0, :]      # Get entire first row
last_col = m[:, -1]      # Get last column (negative indexing)
submatrix = m[:2, :3]    # Get first 2 rows, first 3 columns
```
**Why**: Slicing allows extracting specific data without creating new arrays, saving memory.

### 2.8 Boolean Indexing
```python
greater_than_10 = arr[arr > 10]  # Filter elements > 10
even = arr[arr % 2 == 0]          # Filter even numbers
```
**Why**: Boolean indexing is powerful for filtering data based on conditions, replacing the need for loops.

### 2.9 Statistical Methods
```python
mean_val = rand_arr.mean()
median_val = np.median(rand_arr)
min_val = rand_arr.min()
max_val = rand_arr.max()
```
**Why**: These are built-in functions. Using them is faster and cleaner than manually calculating statistics.

### 2.10 Random Arrays and Seeding
```python
np.random.seed(42)
rand_matrix = np.random.randn(2, 3)
```
**Why**: Setting seed ensures reproducibility - same random numbers generate every time code runs. Critical for testing and debugging.

### 2.11 Matrix Multiplication
```python
prod = A @ B
```
**Why**: The `@` operator performs matrix multiplication (not element-wise). Essential for linear algebra operations and machine learning.

### 2.12 Broadcasting
```python
matrix = np.ones((3, 3))  # 3×3 array of 1s
row = np.array([1, 2, 3]) # 1D array
result = matrix + row      # Each row gets [1,2,3] added
```
**Why**: Broadcasting automatically expands shapes to match without explicitly creating multiple copies. Memory efficient.

---

## 4. Section 3: pandas – Beginner

### Why This Section:
pandas works with labeled data (Series and DataFrames). These examples show how to create and manipulate structured data.

### 3.13 Create a Series
```python
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
val_c = s['c']  # Access by label, not position
```
**Why**: Series have labeled indices (like dictionaries), making data access intuitive and self-documenting.

### 3.14 Create a DataFrame from Dict
```python
students = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [20, 22, 19, 21],
    'score': [85, 70, 95, 60]
})
```
**Why**: DataFrames are like CSV files in memory - columns with different data types. Standard format for data analysis.

### 3.16 DataFrame Info
```python
print(f"   Columns: {list(students.columns)}")
print(students.dtypes)
print(students.describe())
```
**Why**: These provide quick data profiling - check columns, data types, and summary statistics before analysis.

### 3.17 Selecting Rows and Columns
```python
name_score = students[['name', 'score']]        # Select columns
older_than_20 = students[students['age'] > 20]  # Filter rows
```
**Why**: Column/row selection is how you subset data for specific analysis tasks.

---

## 5. Section 4: pandas – Intermediate

### Why This Section:
These examples show data cleaning, transformation, and aggregation - core skills in real-world data analysis.

### 4.18 Filtering with Conditions
```python
hot = df[df['temperature'] > 30]
hot_and_dry = df[(df['temperature'] > 30) & (df['humidity'] < 50)]
```
**Why**: Combining multiple conditions (`&` for AND, `|` for OR) allows complex data filtering.

### 4.19 Adding and Modifying Columns
```python
students['passed'] = students['score'] >= 50      # New column
students['score'] = students['score'] + 5         # Modify existing
```
**Why**: Creating derived columns is fundamental - e.g., "passed/failed" from scores, or adjusted values.

### 4.20 Handling Missing Values
```python
missing_bool = df_na.isna()     # Identify NaN values
filled = df_na.fillna(0)        # Replace NaN with 0
dropped = df_na.dropna()        # Remove rows with NaN
```
**Why**: Real data always has missing values. You must decide whether to fill, drop, or impute them.

### 4.21 Sorting
```python
sorted_by_score = students.sort_values('score', ascending=False)
sorted_multi = students.sort_values(['age', 'score'], ascending=[True, False])
```
**Why**: Sorting helps identify extremes (highest/lowest) or organize data for presentation/analysis.

### 4.22 Grouping and Aggregation
```python
avg_salary = emps.groupby('department')['salary'].mean()
total_salary = emps.groupby('department')['salary'].sum()
```
**Why**: Groupby is crucial for aggregating by categories. E.g., find average salary per department.

### 4.23 Merging DataFrames
```python
merged = pd.merge(left, right, on='student_id')
```
**Why**: Merge combines two tables on common column (like SQL JOIN). Essential for combining data from multiple sources.

---

## 6. Section 5: Advanced NumPy & pandas

### Why This Section:
These examples demonstrate performance optimization, custom functions, and advanced pandas features.

### 5.24 Vectorization vs Loops (Performance Testing)
```python
# Loop version - SLOW
for i in range(len(arr)):
    sq_loop[i] = arr[i] ** 2

# Vectorized version - FAST
sq_vec = arr ** 2
```
**Why**: This demonstrates why vectorization matters. With 1 million elements, vectorized code is often **100x faster**. Always prefer vectorized operations over loops when possible.

### 5.25 Custom Function on Arrays
```python
def normalize(x):
    x = np.asarray(x)
    x_min = x.min()
    x_max = x.max()
    return (x - x_min) / (x_max - x_min)

norm_arr = normalize(arr)
```
**Why**: Min-max normalization scales values to 0-1 range. Common preprocessing step in machine learning.

### 5.26 Multi-indexing
```python
df_mi = df_mi.set_index(['city', 'year'])
london = df_mi.loc['London']
london_2020 = df_mi.loc[('London', 2020)]
```
**Why**: Multi-index allows hierarchical row labels. Great for time series or geographic data (city → year → data).

### 5.27 Pivot Tables
```python
pivot = sales_df.pivot_table(
    values='sales',
    index='region',
    columns='product',
    aggfunc='sum'
)
```
**Why**: Pivot tables reshape data for cross-tabulation analysis. E.g., see sales by region AND product in one view.

### 5.28 Apply and Lambda
```python
students['grade'] = students['score'].apply(grade_from_score)
```
**Why**: `.apply()` applies a custom function to each row. Here, converting numeric scores to letter grades.

---

## 7. Section 6: Real-World Examples

### Why This Section:
These practical examples simulate real business scenarios, combining multiple techniques.

### 6.29 Sales Analysis
```python
sales['revenue'] = sales['quantity'] * sales['price']
total_revenue = sales['revenue'].sum()
revenue_by_product = sales.groupby('product')['revenue'].sum().sort_values(ascending=False)
```
**Why**: Common business task - calculate totals and rankings. Shows creating derived columns and aggregation.

### 6.30 Customer Behavior
```python
revenue_per_customer = sales.groupby('customer_id')['revenue'].sum().sort_values(ascending=False)
avg_order_value = total_revenue / num_orders
```
**Why**: Business insight - who are top customers? What's the average order? Vital for marketing and strategy.

### 6.31 Time Series Analysis
```python
df_ts['date'] = pd.to_datetime(df_ts['date'])
df_ts = df_ts.set_index('date').sort_index()
monthly_revenue = df_ts['revenue'].resample('ME').sum()
```
**Why**: Converting to datetime and resampling allows aggregation by time periods (daily, monthly, yearly).

### 6.32 Employee Performance
```python
perf['tasks_per_hour'] = perf['tasks_completed'] / perf['hours_worked']
avg_tph_by_dept = perf.groupby('department')['tasks_per_hour'].mean()
```
**Why**: Computing efficiency metrics (tasks/hour) and comparing across departments identifies high-performers.

### 6.33 Real Dataset Cleanup
```python
# Example pattern shown:
df = pd.read_csv('dataset.csv')
df.head()
df.info()
# Handle missing values, fix data types, remove duplicates
```
**Why**: The typical workflow for any data analysis project - load, inspect, clean, analyze.

---

## 8. Print Formatting

### Why All the `print()` Statements:
```python
print("=" * 60)
print("1. NumPy – Beginner")
print("=" * 60)
```
**Why**: These create clear visual sections in the output, making it easy to:
- Navigate the output
- Separate thousands of lines of output
- Identify which example currently running
- Understand the progression from beginner to advanced

---

## 9. Key Programming Concepts Used

| Concept | Example | Why Important |
|---------|---------|---------------|
| **Vectorization** | `arr ** 2` instead of loops | Massive performance gains (100x+) |
| **Boolean Indexing** | `arr[arr > 10]` | Elegant filtering without loops |
| **Groupby Aggregation** | `df.groupby('dept')['salary'].mean()` | Summarize data by categories |
| **Broadcasting** | Matrix + row vector | Memory efficient operations |
| **Method Chaining** | `df.groupby().sum().sort_values()` | Write concise, readable code |
| **Lambda & Apply** | `.apply(func)` | Apply custom logic to data |
| **Time Complexity** | `time.time()` comparisons | Understand performance implications |

---

## 10. Summary

**Why This Script Exists:**
1. **Educational**: Teaches NumPy and pandas from basics to advanced
2. **Practical**: Real-world examples simulate actual data analysis tasks
3. **Reference**: Can be run repeatedly to test understanding or as a cheat sheet
4. **Benchmark**: Demonstrates performance differences (vectorization vs loops)
5. **Comprehensive**: Covers 33 different techniques and patterns

**When to Use This Script:**
- Learning NumPy and pandas
- Refreshing knowledge on specific operations
- Benchmarking performance
- Using as a template for your own projects

**Key Takeaway:**
NumPy and pandas allow processing large datasets efficiently through vectorization, avoiding slow Python loops. These are essential tools for any data scientist or analyst.
