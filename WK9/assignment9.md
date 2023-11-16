## **Week 9: Data Preparation for Machine Learning**

### **Objective**: 
Focus on selecting datasets suitable for a machine learning experiment, with an emphasis on data cleaning, encoding, and transformation steps necessary to prepare the data.

### **Instructions**:

#### **1. Dataset Selection:**
- Choose two datasets from healthdata.gov or data.gov that you wish to prepare for a machine learning experiment.
- The datasets can be related to any health or public domain topic but should be suitable for either classification or regression tasks.

#### **2. Data Cleaning and Transformation Plan:**
- Document your plan for data cleaning and transformation in a markdown file. Include the following:
  - A brief description of each dataset.
  - The intended machine learning task for each dataset (classification or regression).
  - The steps needed to clean and transform the data. Consider aspects like missing values, outliers, encoding categorical variables, standardizing or normalizing, etc.
  - Identify the independent (predictors) and dependent (target) variables in each dataset.

#### **3. Data Cleaning Execution (Optional Challenge):**
- If you wish to challenge yourself, perform the actual data cleaning and transformation steps in Python. 
- Use Pandas, NumPy, or other relevant libraries for data manipulation.

#### **4. Dataset Splitting:**
- Create a separate script to split each dataset into three parts:
  - Training data (`train_x`, `train_y`)
  - Validation data (`val_x`, `val_y`)
  - Testing data (`test_x`, `test_y`)
- Follow the standard practices of dataset splitting as discussed in class.

#### **5. Documentation:**
- Document each step of your process. Include screenshots of any errors encountered and how you resolved them.
- Explain your decisions during the data cleaning and transformation process.

#### **6. Submission**:
- Create a new GitHub repository named `datasci_9_data_prep` in your GitHub account.
- Organize your GitHub repository with the following:
  - A "datasets" folder containing the datasets you chose.
  - The markdown file with your data preparation plan.
  - Python scripts used for data cleaning and dataset splitting.
  - Submit the link to your GitHub repository.

---

**Tip**: Proper data preparation is crucial in machine learning. It can significantly impact the performance of your models. Pay attention to the details of each dataset and the specific requirements of the machine learning tasks you plan to perform.

---