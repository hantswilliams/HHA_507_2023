## **Week 14: Cron Jobs**

### **Objective**: 
Learn how to automate data-related tasks by setting up and running Cron Jobs.

### **Instructions**:

#### **1. Setting Up a Simple Cron Job:**
- Set up a Python script that logs the current date and time into a text file.
- Using a local environment or a cloud platform, set up a cron job to run this script every 10 minutes.

#### **2. Data Automation:**
- Modify your script to pull new data from an API of your choice (it can be the same API you used in week 13).
- Store the newly fetched data in a structured format, such as a CSV or a database.
- Set up a cron job to run this script once a day.

#### **3. Notifications:**
- Integrate a notification mechanism in your script. This could be sending an email or an SMS notification after data has been fetched and stored successfully.
- Test the notification mechanism by triggering it manually.

#### **4. Reflection & Monitoring:**
- In markdown cells, discuss:
  - The challenges you faced while setting up and monitoring cron jobs.
  - Potential scenarios where automating data acquisition might be beneficial or detrimental.
  - The importance of notifications and monitoring in automated tasks.

#### **5. Submission**:
- Create a new GitHub repository named `datasci_14_cron_jobs` in your GitHub account.
- Organize your GitHub repository with the following:
  - A "logs" folder containing the generated log files.
  - A "data" folder containing the fetched data if feasible and not too large.
  - Save your Colab/Jupyter notebook and the Python script to your GitHub repository.
  - Submit the link to your GitHub repository.

#### **Resources**:

- [Python Cron Jobs: How To Schedule Python Scripts](https://www.simplifiedpython.net/python-cron-job/)
- [How To Send Emails with Python](https://realpython.com/python-send-email/)
- [Setting up Cron Jobs in Cloud Platforms](https://www.cloudsavvyit.com/961/how-to-use-cron-jobs-on-a-cloud-server/)

---

**Tip**: Ensure your cron jobs are properly scheduled to avoid overwhelming servers or reaching API limits. Always monitor your scheduled tasks for any issues or anomalies.
