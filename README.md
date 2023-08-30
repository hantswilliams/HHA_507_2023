# HHA 507 2023

## **Week 1: Introduction to Jupyter Notebooks (Google Colab) and Data Acquisition**
### Lecture Topic:
- Introduction to Jupyter and Google Colab.
### Subtopics:
- Data Sources:
  - Web data: Web pages, logs, streams.
  - Sensor data: Internet of Things (IoT), wearables.
  - Streaming data: Real-time data feeds, social media streams.
- Data Licensing & Ethics:
  - Open Data vs. Proprietary Data.
  - Respecting privacy and terms of use.
  - GDPR, CCPA, and other data protection regulations.
  - Data derivatives 
- Data Provenance: Tracking the source of data and understanding its lineage.
- Data Integrity & Validation: Techniques to ensure accuracy and consistency in the acquired data.
- Data acquisition basics: Importing CSV, Excel, SQL databases, and more.
- Using pandas to import various file formats: CSV, Excel, JSON, and more.
- Native Python file handling: Opening and reading files without the aid of external libraries.
- Data formats: 
  - JSON, XML: Hierarchical and structured data formats.
  - Pickle: Python native serialization.
  - Parquet, Feather: Columnar storage, often used with big data tools.
  - HDF5: Hierarchical Data Format suitable for storing large datasets.
  - SQL databases: SQLite, MySQL, PostgreSQL, etc.
  - NoSQL databases: MongoDB, CouchDB, etc.
  - Avro, Protocol Buffers: Serialization formats suitable for Big Data and distributed systems. 
### Resources:
- [Jupyter](https://jupyter.org/)
- [Google Colab](https://colab.research.google.com/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

### Homework:
- [Assignment 1](WK1/assignment1.md)

## **Week 2: Data Manipulation in Python: Pandas, Polars, Dask, and Modin**
### Lecture Topic:
- Introduction to data manipulation libraries in Python.
### Subtopics:
- Pandas for data manipulation: Filtering, sorting, and transforming data.
- Introduction to Polars: Features and advantages.
- Dask and Modin: Scaling Pandas – how and when to use them.
### Resources:
- [Pandas](https://pandas.pydata.org/)
- [Polars](https://github.com/pola-rs/polars)
- [Dask](https://dask.org/)
- [Modin](https://modin.readthedocs.io/en/latest/)

### Homework:
- [Assignment 2](WK2/assignment2.md)

## **Week 3: Exploratory Data Analysis (EDA)**
### Lecture Topic:
- Introduction to the process and importance of Exploratory Data Analysis.
### Subtopics:
- Outlier detection and handling.
- Correlations and covariances.
- Handling missing values.
- Visualization techniques in EDA.
### Resources:
- [EDA with Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
### Homework:
- [Assignment 3](WK3/assignment3.md)
## **Week 4: Data Visualization with Seaborn and Plotly**
### Lecture Topic:
- The significance of visual representation in Data Science.
### Subtopics:
- Basic plotting techniques with Seaborn.
- Interactive plots using Plotly.
- Plotting categorical vs numerical data.
### Resources:
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/python/)

### Homework:
- [Assignment 4](WK4/assignment4.md)

## **Week 5: Inferential Statistics**
### Lecture Topic:
- Going beyond descriptive statistics to make inferences about the population.
### Subtopics:
- Hypothesis testing.
- Confidence intervals.
- Chi-square tests.
### Resources:
- [SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
### Homework:
- [Assignment 5](WK5/assignment5.md)
## **Week 6: Regression Analysis**
### Lecture Topic:
- Introduction to linear relationships and regression analysis.
### Subtopics:
- Simple linear regression.
- Multiple regression.
- Polynomial regression.
### Resources:
- [StatsModels](https://www.statsmodels.org/stable/index.html)
### Homework:
- [Assignment 6](WK6/assignment6.md)
## **Week 7: Geospatial Data**
### Lecture Topic:
- Analysis involving geographical and spatial information.
### Subtopics:
- Working with Geospatial data in Python.
- Visualizing Geospatial data.
### Resources:
- [Geopandas](https://geopandas.org/)
### Homework:
- [Assignment 7](WK7/assignment7.md)
## **Week 8: Classification Techniques**
### Lecture Topic:
- Categorizing data points based on known classifications.
### Subtopics:
- Logistic regression.
- Decision trees.
- Naive Bayes.
### Resources:
- [Scikit-learn Classification](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
### Homework:
- [Assignment 8](WK8/assignment8.md)
## **Week 9: Ensemble Methods and Advanced Models**
### Lecture Topic:
- Improving prediction accuracy with ensemble methods.
### Subtopics:
- Bagging and Boosting.
- Random forests.
- Gradient boosted trees.
### Resources:
- [Scikit-learn Ensemble](https://scikit-learn.org/stable/modules/ensemble.html)
### Homework:
- [Assignment 9](WK9/assignment9.md)

## **Week 10: Unsupervised Learning**
### Lecture Topic:
- Machine learning methods for discovering patterns in data.
### Subtopics:
- Clustering techniques.
- Principal component analysis (PCA).
### Resources:
- [Scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
### Homework:
- [Assignment 10](WK10/assignment10.md)
## **Week 11: Time Series Analysis**
### Lecture Topic:
- Analyzing data points ordered or indexed in time.
### Subtopics:
- Time series decomposition.
- ARIMA models.
- Forecasting techniques.
### Resources:
- [Pandas Time Series](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
### Homework:
- [Assignment 11](WK11/assignment11.md)
## **Week 12: Natural Language Processing (NLP)**
### Lecture Topic:
- Processing and analyzing human language data.
### Subtopics:
- Text preprocessing techniques.
- Sentiment analysis.
- Topic modeling.
### Resources:
- [NLTK](https://www.nltk.org/)
- [Spacy](https://spacy.io/)
### Homework:
- [Assignment 12](WK12/assignment12.md)

## **Week 13: Advanced Data Acquisition: APIs and Web-scraping**
### Lecture Topic:
- Acquiring data from web sources.
### Subtopics:
- Introduction to APIs.
- Web scraping using Beautiful Soup and Scrapy.
### Resources:
- [Requests](https://docs.python-requests.org/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
### Homework:
- [Assignment 13](WK13/assignment13.md)
## **Week 14: Cron Jobs**
### Lecture Topic:
- Automating data fetching and processing tasks.
### Subtopics:
- Introduction to Cron.
- Setting up regular data fetching tasks.
### Resources:
- [Python Cron Libraries](https://pypi.org/project/python-crontab/)
### Homework:
- [Assignment 14](WK14/assignment14.md)
## **Week 15: Course Review and Final Project Presentation**
### Lecture Topic:
- Recap of major course topics and final project presentation.
### Subtopics:
- Discussion and QA session.
- Presentation of student projects.
### Resources:
- [Python Documentation](https://docs.python.org/3/)
- [Course GitHub Repository](#)
