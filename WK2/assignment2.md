## **Week 2: Data Manipulation in Python: Pandas, Polars, Dask, and Modin**

### **Objective**: 
Delve deeper into data manipulation using Python's prominent libraries. Explore the functionalities of Pandas and get a glimpse of alternatives like Polars, Dask, and Modin.

### **Instructions**:

#### **1. Data Cleaning with Pandas:**
- Load the dataset `WK2/data/healthcare_data_cleaning.csv` in your Colab notebook (preferably one from the previous assignment) **OR** in a new python script.
- Identify and handle missing values in the dataset.
- Remove any duplicate rows and columns, if they exist.
- Clean column names 
- Add either a markdown cell if using a notebook, or comments if using a script, to document the changes made to the dataset.

#### **2. Data Transformation:**
- Create new columns based on existing ones (e.g., if you have a 'birth_date' column, create an 'age' column).
- Aggregate data using groupby and compute summary statistics.
- Use pivot tables or cross-tabulations for multi-dimensional analysis.

#### **3. Introduction to Alternative Libraries:**
- Read about Polars, Dask, and Modin in Chapter 2.
- Load your dataset using Polars and Modin.
- Compare the load times and write your observations in a markdown cell or in your script.
  - Please see [Chapter 2 - Adv Exercises](https://book.datascience.appliedhealthinformatics.com/docs/Ch2/distributed-computation#advanced-exercises) to see how to use the `import time` module as an example of capturing start time and end time

### **4. Submission**:
- Create a new GitHub repository named `datasci_2_manipulation` in your GitHub account.
- Organize your GitHub repository with the following:
  - A "datasets" folder containing the dataset you worked on.
  - Save your Colab notebook to your GitHub repository.
  - Submit the link to your GitHub repository.

#### **Resources:**

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Polars GitHub Repository](https://github.com/pola-rs/polars)
- [Dask Documentation](https://docs.dask.org/en/latest/)
- [Modin Documentation](https://modin.readthedocs.io/en/latest/)

---

**Tip**: Remember, while Pandas is powerful, it's essential to explore alternative libraries to handle larger datasets efficiently.
