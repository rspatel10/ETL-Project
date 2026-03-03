## Python Data Analysis Practice – NumPy & pandas (Student Version)

This set of questions is designed to help you practice **writing code** using **NumPy** and **pandas**, from **beginner** to **advanced**, finishing with **real-world style tasks**.

Try to write and run code for each question. Do **not** look at the solutions until you have tried.

---

### 1. NumPy – Beginner

1. **Create a 1D array**
   - Create a NumPy array containing the integers from 1 to 10 (inclusive).

2. **Create a 2D array**
   - Create a 3x3 NumPy array with the values 1 to 9.

3. **Array of zeros and ones**
   - Create an array of 10 zeros and an array of 10 ones.

4. **Array with a specific step**
   - Create an array of even numbers from 0 to 20 (inclusive).

5. **Basic element-wise operations**
   - Given `a = np.array([1, 2, 3])` and `b = np.array([4, 5, 6])`, compute:
     - `a + b`
     - `a * b`
     - `a ** 2`

6. **Array shape and reshaping**
   - Create an array with values 0 to 11 and reshape it into a 3x4 matrix.
   - Print its shape and number of dimensions.

---

### 2. NumPy – Intermediate

7. **Indexing and slicing**
   - For the 3x4 matrix from Question 6:
     - Select the first row.
     - Select the last column.
     - Select the submatrix containing the first 2 rows and first 3 columns.

8. **Boolean indexing**
   - Create an array of integers from 0 to 20.
   - Select only the numbers that are:
     - Greater than 10
     - Even

9. **Statistical methods**
   - Create a 1D array of 10 random integers between 1 and 100.
   - Compute the array’s mean, median (you can use NumPy for median), minimum, and maximum.

10. **Random arrays and seeding**
    - Set a random seed (e.g. 42).
    - Create a 2x3 array of random numbers from a standard normal distribution.

11. **Matrix multiplication**
    - Create two compatible 2D arrays and perform matrix multiplication using `np.dot` or the `@` operator.

12. **Broadcasting**
    - Given a 3x3 matrix of ones and a 1D array `[1, 2, 3]`, add them using broadcasting.

---

### 3. pandas – Beginner

13. **Create a Series**
    - Create a `pandas.Series` from the list `[10, 20, 30, 40]` with custom index labels `['a', 'b', 'c', 'd']`.
    - Access the element with label `'c'`.

14. **Create a DataFrame from a dict**
    - Create a DataFrame that represents students:
      - Columns: `name`, `age`, `score`
      - Data: at least 4 rows of your choice.

15. **Read data from CSV (conceptual if no file)**
    - Write code that reads a CSV file named `students.csv` into a DataFrame.
    - Show the first 5 rows.

16. **Basic DataFrame info**
    - For the students DataFrame:
      - Display the column names.
      - Display the data types of each column.
      - Get basic statistics for numeric columns.

17. **Selecting rows and columns**
    - From the students DataFrame, select:
      - Only the `name` and `score` columns.
      - Rows where `age` is greater than 20.

---

### 4. pandas – Intermediate

18. **Filtering with conditions**
    - Given a DataFrame `df` with columns `city`, `temperature`, and `humidity`, write code to:
      - Select rows where `temperature` is above 30.
      - Select rows where `temperature` is above 30 **and** `humidity` is below 50.

19. **Adding and modifying columns**
    - For the students DataFrame:
      - Add a new column `passed` which is `True` if `score` is at least 50, else `False`.
      - Increase every student’s score by 5 points.

20. **Handling missing values**
    - Create a small DataFrame with some `NaN` values.
    - Show how to:
      - Find which values are missing.
      - Fill missing values with a constant (e.g. 0).
      - Drop rows that contain any missing values.

21. **Sorting**
    - Sort the students DataFrame:
      - By `score` in descending order.
      - Then by `age` (ascending) and `score` (descending).

22. **Grouping and aggregation**
    - Create a DataFrame with columns: `department`, `employee`, `salary`.
    - Group by `department` and calculate:
      - Average salary per department.
      - Total salary per department.

23. **Merging / joining DataFrames**
    - Create two small DataFrames:
      - One with columns `student_id`, `name`
      - Another with columns `student_id`, `course`
    - Merge them on `student_id`.

---

### 5. Advanced NumPy & pandas

24. **Vectorization vs loops (NumPy)**
    - Create a large 1D array (e.g. size 1,000,000) of random numbers.
    - Compute the square of each element using:
      - A Python `for` loop.
      - Pure NumPy vectorized operation.
    - Compare the time taken (use `time` or `%timeit` in a notebook).

25. **Custom function on arrays (NumPy)**
    - Write a function that normalizes a NumPy array so that its values are between 0 and 1.
    - Apply this function to a random array.

26. **Multi-indexing (pandas)**
    - Create a DataFrame with a MultiIndex based on two columns, for example:
      - Index levels: `city` and `year`
      - Column: `population`
    - Show how to:
      - Select data for a specific city.
      - Select data for a specific city and year.

27. **Pivot tables (pandas)**
    - Suppose you have a DataFrame with columns: `region`, `product`, `sales`.
    - Create a pivot table that shows total `sales` for each combination of `region` and `product`.

28. **Apply and lambda (pandas)**
    - For the students DataFrame:
      - Create a new column `grade` using `apply` and a custom function:
        - `score >= 90` → `'A'`
        - `80–89` → `'B'`
        - `70–79` → `'C'`
        - `60–69` → `'D'`
        - `< 60` → `'F'`

---

### 6. Real-World Style Questions (Mini Projects)

For these questions, imagine you are working as a **data analyst**. You receive some data and need to answer business‑style questions. You can create dummy data or load from a real CSV if you have one.

29. **Sales analysis (pandas + NumPy)**
    - You have a dataset with columns: `order_id`, `date`, `customer_id`, `product`, `quantity`, `price`.
    - Tasks:
      - Compute a new column `revenue = quantity * price`.
      - Find the **total revenue**.
      - Find the **top 3 products** by total revenue.
      - Find the **number of unique customers**.
      - Group by `date` to compute **daily total revenue**.

30. **Customer behavior**
    - Using the same sales dataset:
      - Compute **total revenue per customer**.
      - Find the **top 5 customers** by total revenue.
      - Compute the **average order value** (revenue per order).

31. **Time series analysis (basic)**
    - Assume your dataset has a `date` column (string) and `revenue` column.
    - Tasks:
      - Convert `date` to a `datetime` type.
      - Set `date` as the index and sort the DataFrame by date.
      - Resample the data to get **monthly total revenue**.

32. **Employee performance**
    - You have a dataset with columns:
      - `employee_id`, `department`, `month`, `tasks_completed`, `hours_worked`.
    - Tasks:
      - Compute `tasks_per_hour = tasks_completed / hours_worked`.
      - For each department, calculate the **average tasks per hour**.
      - Find the **top 3 employees** across the company by `tasks_per_hour`.

33. **Real dataset cleanup and summary (open‑ended)**
    - Take any messy CSV file you can find (for example, from Kaggle or any open dataset).
    - Using pandas and NumPy, do the following:
      - Load the data.
      - Inspect the first rows and column info.
      - Clean the data:
        - Handle missing values.
        - Fix data types (e.g. convert strings to numbers or dates).
        - Remove obviously incorrect or duplicate rows.
      - Create at least **3 meaningful summary statistics or visualizations** (if you know plotting).
      - Write down **3–5 insights** you discovered from the data.

---

Try to write clean, well‑commented code for each question. When you are done, compare your solutions with `answers.md`.

