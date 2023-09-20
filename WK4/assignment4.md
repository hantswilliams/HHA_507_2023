## **Week 4: Web-Based Data Visualization Using Shiny and Flask**

### **Objective**: 
Explore web-based platforms for interactive data visualization, contrasting R's Shiny with Python's equivalents. Harness these tools to present data in interactive and user-friendly ways.

### **Instructions**:

#### **1. R's Shiny Visualization:**
- Use a subset of data from the most recent CDC Healthy Places that is either not NY (e.g., just one state that is not NY) or includes NY plus a select number of other states for comparison (e.g., NY vs TX vs CA). You can find the [original source data here](https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb)
- Create a basic Shiny app that:
  - Allows users to filter or select data based on one or more criteria.
  - Displays a visualization (e.g., a bar chart or scatter plot) that updates based on user input.
  
You **must** use the **posit.cloud** environment for this task as we haven't covered local R setups.

#### **2. Python's Shiny Visualization:**
- Using the same subset of data, replicate the Shiny app using Python's shiny package.
- Your app should have the same functionalities and user interactivity as the R version.
  
#### **3. Flask with Matplotlib Visualization:**
- Again, using the same subset of data, create a Flask application that:
  - Presents a dropdown (or other form of user input) to select data criteria.
  - Displays a Matplotlib visualization that changes based on user input.
  - Make sure the image is served dynamically using the techniques learned (i.e., `io` and `base64`).

#### **4. Markdown Reflections:**
- For each application (Shiny R, Python's shiny, Flask):
  - Describe the challenges you encountered and how you overcame them.
  - Share insights or patterns you observed in terms of coding, interactivity, and user experience.
  
#### **5. Submission**:
- Create a new GitHub repository named `datasci_4_web_viz` in your GitHub account.
- Organize your GitHub repository with the following:
  - A "datasets" folder containing the subset of data you worked on.
  - Separate folders for each of the approaches:
    1. `shiny_r`
    2. `shiny_python`
    3. `python_flask`
  - In each folder, include the source code and any additional resources needed to run the app. You should start with the base code provided during our lesson and modify it as needed.
  - Submit the link to your GitHub repository.

#### **Resources**:

- [Shiny from RStudio](https://shiny.rstudio.com/)
- [Python's shiny package documentation](https://pypi.org/project/shiny/)
- [Flask documentation](https://flask.palletsprojects.com/en/2.1.x/)
- [Using Flask with Matplotlib](https://flask.palletsprojects.com/en/2.1.x/patterns/streaming/)
  
---

**Tip**: The goal is to not just replicate functionalities across platforms, but to understand the nuances and specialties of each. While coding, consider the strengths and weaknesses of each platform and how they might be best leveraged in real-world scenarios.

