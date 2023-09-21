---
marp: true
theme: default
paginate: true
size: 16:9
---

# Introduction to Shiny (20 slides)

A powerful tool for creating interactive web apps straight developed first in R (but now also in Python!)

---

# Why Use Shiny?

Started off as a R only tool that allowed for: 

- **Interactivity**: Instantly see changes and results.
- **No HTML, CSS, or JavaScript required**: Develop using R.
- **Easy Sharing**: Deploy apps on Shinyapps.io or a Shiny Server.
- **Integration**: Incorporate numerous R packages and datasets.

---

# Shiny at Stony Brook University

Stony Brook has leveraged Shiny in various capacities:

- **Cancer Center**: Utilized Shiny apps for visualizing patient data, outcomes, and trends.
- **Biomedical Informatics Department**: Incorporated Shiny for interactive research tools and to aid in data analysis.

![Stony Brook Logo](https://www.stonybrookmedicine.edu/sites/default/files/cckimages/page/medlogo.jpg)

---

# Shiny for Python

Shiny isn't just for R anymore!

- **Python Integration**: There's now a package available for Python users to create Shiny-like applications.
- **Expands Reach**: Enables a broader audience to benefit from the reactivity and interactivity Shiny offers.

---

# Introduction to R for Pythonistas

![R vs Python](../../WK4/slides/images/r_python.png)

---

# Language Basics

- **R**:
  - Developed primarily for statistical computing and graphics.
  - Rich ecosystem for data analysis, visualization, and statistical testing.
  - Generally uses the assignment operator `<-` (but `=` works too).

- **Python**:
  - General-purpose language with rich libraries for web development, scripting, etc.
  - Uses the assignment operator `=`.

*Python*: `x = 10`  
*R*: `x <- 10`

---

# Data Structures

- **R**:
  - Main data structures: vector, matrix, data frame, list.
  - Data frame (`data.frame`): table-like structure, columns can be different types.

- **Python**:
  - Lists, dictionaries, tuples, sets.
  - Data frame equivalent via the `pandas` library: `DataFrame`.

---

# Indexing

- **R**:
  - 1-based indexing.
  - Access data frame columns with `$`.

- **Python**:
  - 0-based indexing.
  - Access `DataFrame` columns with dot `.` or brackets `[]`.

*Python*: `df.column_name` or `df['column_name']`  
*R*: `df$column_name`

---

# Libraries vs Packages

- **R**:
  - Libraries are collections of functions and data sets.
  - Use `library()` to load them.

- **Python**:
  - Libraries (or packages) are collections of modules.
  - Use `import` to load them.

*Python*: `import pandas as pd`  
*R*: `library(dplyr)`

---

#  Functions

- Both languages use functions heavily.
  
*Python*: 
```python
def function_name(parameters):
    # code
    return value
```

*R*: 
```R
function_name <- function(parameters) {
  # code
  return(value)
}
```

---

# Python Libraries and Their R Equivalents

| Python         | R Equivalent                   | Description                                                      |
| -------------- | ------------------------------ | ---------------------------------------------------------------- |
| `pandas`       | `dplyr` (for data manipulation), `tidyr` (for data tidying) | Data manipulation and tidying.                                   |
| `plotly/seaborn` | `ggplot2`                       | Data visualization using grammar of graphics.                   |
| `scipy`        | `stats` (base R package)       | Wide variety of statistical functions.                           |
| `sqlalchemy`   | `DBI` with connectors like `RPostgres`, `RSQLite` | Database connectivity and operations.                           |

---

# Testing R Code with Posit.cloud

- Need a quick environment to test your R code without installations?
- **Posit.cloud** offers a browser-based R environment.
- Go to [posit.cloud](https://posit.cloud/) and start coding!

---


# Now, on to Shiny R Components

- **UI**: The user interface. What the end-user interacts with.
- **Server**: The backend. Where the reactive programming and data manipulation occurs.

```R
ui <- fluidPage( ... )
server <- function(input, output) { ... }
shinyApp(ui = ui, server = server)
```

---

# Shiny Python Components 


1. **UI** (User Interface): Defines how the app looks.
2. **Server**: Contains the logic; reacts to user input and changes the output.
3. **App**: Combines UI and Server.


```python
from shiny import App, ui

app_ui = ui.page_fluid("Hello, world!")
def server(input, output, session): ...
app = App(app_ui, server)
```

---


# Reactive Programming

Shiny is built on the concept of reactivity.

- Inputs change.
- Reactive objects recompute.
- Outputs update.

---

# Basic Shiny App Structure

```R
library(shiny)

ui <- fluidPage(
  titlePanel("My Shiny App"),
  sidebarLayout(
    sidebarPanel( ... ),
    mainPanel( ... )
  )
)

server <- function(input, output) {
  ...
}

shinyApp(ui = ui, server = server)
```


---

# Python - Shiny Components

```python
from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_select("x", "Select input", {"a": "Choice A", "b": "Choice B"}),
    ui.output_text_verbatim("txt"),
)
```

**Inputs**: Widgets like sliders, dropdowns, and buttons. Capture user's input.

**Outputs**: Places where rendered data, plots, or text will be displayed.

---

# Python - Rendering Outputs

Use decorators to determine how outputs (like texts or plots) should be rendered.

```python
def server(input, output, session):
    @output
    @render.text
    def txt():
        return f'x: "{input.x()}"'
```


---
# Running Shiny Apps
---

## Running Shiny in R

### Steps:

1. Ensure you have the `shiny` library installed in R:
```R
install.packages("shiny")
```

2. Write your Shiny app code in an R script, like a `app.R` file.

---

3. Set your working directory to where your Shiny app resides:
```R
setwd("/path/to/your/app_directory")
```

4. Run your Shiny app using:
```R
shiny::runApp()
```

### Terminal Command:
If you're outside R (e.g., in the terminal), navigate to the directory and run:
```bash
R -e "shiny::runApp()"
```

---

## Running Shiny in Python

### Steps:

1. Ensure you have the Python `shiny` package installed:
```bash
pip install shiny
```

2. Write your Shiny app code in a Python script, say `app.py`.

3. Navigate to the directory where your Python Shiny app resides.

4. Run your Shiny app using:
```bash
shiny run app.py --reload
```

---

# Deploying Shiny Apps on the Web

1. **Shinyapps.io**: RStudio's platform for hosting Shiny apps.
2. **Shiny Server**: Your own server for hosting Shiny apps.
3. **Shiny Server Pro**: RStudio's professional server offering, with authentication and more.

We will also learn about deploying a shiny app or our VM on a GCP/Azure environment, and how we can then perform a terminal command like below to run the application on our own cloud enviornment
`uvicorn app:app --host 0.0.0.0 --port 80` 

---

# Example resources 

Python shiny apps: [official examples](https://shinylive.io/py/examples/#basic-app)
- Official [github repo](https://github.com/posit-dev/py-shiny)

R shiny apps: [official examples](https://shiny.posit.co/r/gallery/)
- Official [github repo](https://github.com/rstudio/shiny)

---

# Conclusions

- Shiny offers a seamless experience for creating interactive web apps using just R.
- It provides a robust framework for reactivity and data visualization.
- Allows for easy deployment and sharing.

