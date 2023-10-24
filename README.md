# HHA 507 2023

## **Week 1: Introduction to Jupyter Notebooks (Google Colab) and Health Data Acquisition**
### Lecture Topic:
- Introduction to Jupyter, Google Colab, and their relevance in Health Informatics.

### Subtopics:
- **Health Data Sources**:
  - Electronic Health Records (EHRs) and Personal Health Records (PHRs).
  - Bioinformatics data: Genomic, proteomic, and other '-omics' data.
  - Sensor data: Medical devices, wearable health monitors.
  - Web data: Health forums, telemedicine logs, patient portals.
- **Data Licensing & Ethics in Health Informatics**:
  - Patient privacy and HIPAA compliance.
  - Consent management and data anonymization techniques.
  - Open health data vs. proprietary data.
  - Understanding and mitigating biases in health data.
- **Data Provenance**: Ensuring traceability of patient data.
- **Data Integrity & Validation in Health**: Importance of clean and consistent data for patient care and research.
- **Data Acquisition in Healthcare**:
  - Acquiring and integrating health data from diverse sources.
  - Challenges and nuances of health data formats.
- **Using pandas for Health Data**:
  - Importing common formats in health informatics: HL7, FHIR, DICOM.
  - Health database systems: SQLite, MySQL, PostgreSQL in healthcare applications.
- **Native Python File Handling in Health Data**:
  - Extracting and processing raw health data.
  - Addressing health-specific data challenges: Timestamps, multi-modal data, etc.
- **General Data Formats**: 
  - JSON, XML: Hierarchical and structured data formats, including FHIR for healthcare.
  - Pickle: Python native serialization.
  - Parquet, Feather: Storage solutions for large-scale health datasets.
  - NoSQL databases: Patient-centric data storage solutions.
  - Avro, Protocol Buffers: Serialization formats suitable for health data streams.

### Readings:
- Williams, H. (2023). Chapter 1 - Data Acquisition and Notebooks. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- Project Jupyter. (n.d.). Jupyter documentation. Retrieved from [https://jupyter-notebook.readthedocs.io/en/stable/](https://jupyter-notebook.readthedocs.io/en/stable/)
- Google Colab. (n.d.). Google Colab documentation. Retrieved from [https://colab.research.google.com/notebooks/welcome.ipynb](https://colab.research.google.com/notebooks/welcome.ipynb)
- pandas development team. (n.d.). pandas documentation. Retrieved from [https://pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/)

### Resources:
- [Jupyter](https://jupyter.org/)
- [Google Colab](https://colab.research.google.com/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [HL7 Standards](https://www.hl7.org/implement/standards/)
- [FHIR Standards](https://www.hl7.org/fhir/)
- [DICOM Standards](https://www.dicomstandard.org/)

### Homework:
- [Assignment 1](WK1/assignment1.md)


## **Week 2: Health Data Manipulation in Python: Pandas, Polars, Dask, and Modin**
### Lecture Topic:
- Introduction to data manipulation libraries in Python tailored for health informatics challenges.

### Subtopics:
- **Pandas in Health Informatics**:
  - Cleaning and preprocessing patient data: Handling missing values, outliers, and inconsistencies.
  - Time series data: Analyzing medical test results, monitoring vitals, and patient history.
  - Merging and combining datasets: Integrating lab results, doctor notes, and imaging data.
- **Polars in Health Data Analysis**:
  - Features and advantages of Polars over Pandas for large health datasets.
  - Efficient operations for genomics and longitudinal patient data.
- **Dask and Modin in Health Informatics**:
  - Scaling Pandas for large-scale health data analyses.
  - Parallel processing: Accelerating computations for patient cohorts, genomic data, and health trends.
  - Use cases: When to choose Dask or Modin over traditional Pandas.
- **Data Confidentiality and Masking in Python**:
  - Techniques to anonymize and pseudonymize patient data.
  - The importance of data masking and its relevance in data manipulation.
- **Data Interoperability in Health**:
  - Transforming health data formats: HL7, FHIR, DICOM, and others.
  - Bridging gaps between heterogeneous health data sources using Python.

### Readings:
- Williams, H. (2023). Chapter 2 - Data Processing and Cleaning. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- pandas development team. (n.d.). pandas documentation. Retrieved from [https://pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/)
- Polars. (n.d.). Polars documentation. Retrieved from [https://github.com/pola-rs/polars](https://github.com/pola-rs/polars)
- Dask. (n.d.). Dask documentation. Retrieved from [https://dask.org/](https://dask.org/)
- Modin. (n.d.). Modin documentation. Retrieved from [https://modin.readthedocs.io/en/latest/](https://modin.readthedocs.io/en/latest/)

### Resources:
- [Pandas](https://pandas.pydata.org/)
- [Polars](https://github.com/pola-rs/polars)
- [Dask](https://dask.org/)
- [Modin](https://modin.readthedocs.io/en/latest/)
- [HL7 Standards](https://www.hl7.org/implement/standards/)
- [FHIR Standards](https://www.hl7.org/fhir/)
- [DICOM Standards](https://www.dicomstandard.org/)

### Homework:
- [Assignment 2](WK2/assignment2.md)


## **Week 3: Exploratory Data Analysis (EDA) in Health Informatics**
### Lecture Topic:
- Introduction to the process and importance of Exploratory Data Analysis in health informatics.

### Subtopics:
- **Understanding Health Data Distribution**:
  - Descriptive statistics for patient data: mean, median, mode, and variance.
  - Distribution curves and skewness in health metrics.
- **Outlier Detection and Handling in Health Data**:
  - Identifying anomalies in vitals, test results, and medical imaging.
  - Strategies for handling outliers: imputation, truncation, and clinical consultation.
- **Correlations and Covariances in Medical Metrics**:
  - Identifying relationships between health parameters.
  - Pitfalls of correlations: spurious associations and confounding variables in health studies.
- **Handling Missing Values in Clinical Data**:
  - Causes of missing health data: skipped tests, unrecorded vitals, and device malfunctions.
  - Imputation techniques: mean, median, mode, and predictive methods.
- **Visualization Techniques in Health EDA**:
  - Histograms and box plots for patient metric distribution.
  - Heatmaps for correlation matrices in multi-test results.
  - Time series plots for tracking patient health trends and treatment effects.
- **Population Health Analysis**:
  - Segmenting patient populations based on demographics and conditions.
  - Understanding health determinants through EDA.
- **Introduction to Medical Imaging EDA**:
  - Basics of analyzing imaging data: X-rays, MRIs, and CT scans.
  - Identifying patterns and anomalies in medical images.

### Readings:
- Williams, H. (2023). Chapter 3 - Exploratory Data Analysis (EDA). Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- pandas development team. (n.d.). pandas visualization documentation. Retrieved from [https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
- Seaborn. (n.d.). Seaborn documentation. Retrieved from [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
- pydicom. (n.d.). pydicom documentation. Retrieved from [https://pydicom.github.io/](https://pydicom.github.io/)

### Resources:
- [EDA with Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
- [Seaborn: Statistical Data Visualization](https://seaborn.pydata.org/)
- [Medical Imaging in Python](https://pydicom.github.io/)

### Homework:
- [Assignment 3](WK3/assignment3.md)



## **Week 4: Data Visualization in Health Informatics with Seaborn and Plotly**
### Lecture Topic:
- The role and importance of visual representation in health informatics.

### Subtopics:
- **Understanding Health Data through Visualization**:
  - The significance of clear visualizations in clinical decision-making.
  - Ethical considerations: ensuring data privacy in visual outputs.
- **Basic Plotting Techniques with Seaborn in a Health Context**:
  - Using histograms, box plots, and swarm plots to visualize patient data distributions.
  - Line and scatter plots for trends in patient vitals and medication effectiveness.
  - Heatmaps to visualize correlations between different health parameters.
- **Interactive Health Data Dashboards using Plotly**:
  - Creating patient health dashboards.
  - Interactive plots to track epidemic and disease spread in communities.
  - Time series visualizations for tracking the progress of disease treatments.
- **Visualizing Categorical vs Numerical Health Data**:
  - Visual comparisons of treatment outcomes across different patient groups.
  - Analyzing the impact of categorical factors like genetic markers on health outcomes.
- **Advanced Visualization Techniques**:
  - Using violin and pair plots for deeper insights into patient data.
  - 3D visualizations for complex datasets such as genetic sequences or neural activity.
- **Medical Imaging Visualization**:
  - Introduction to basic medical imaging plots.
  - Utilizing Seaborn and Plotly to complement traditional imaging tools.

### Readings:
- Williams, H. (2023). Chapter 4 - Visualizations and Dashboards. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- Seaborn. (n.d.). Seaborn documentation. Retrieved from [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
- Plotly. (n.d.). Plotly documentation. Retrieved from [https://plotly.com/python/](https://plotly.com/python/)
- Dash. (n.d.). Dash documentation. Retrieved from [https://dash-gallery.plotly.host/Portal/](https://dash-gallery.plotly.host/Portal/)

### Resources:
- [Seaborn in Medical Data Visualization](https://seaborn.pydata.org/examples/index.html#)
- [Plotly for Interactive Health Dashboards](https://plotly.com/python/)
- [Plotly and Dash for Medical Imaging](https://dash-gallery.plotly.host/Portal/)

### Homework:
- [Assignment 4](WK4/assignment4.md)


## **Week 5: Inferential Statistics in Health Informatics**
### Lecture Topic:
- Using inferential statistics to derive insights from health data and inform clinical decisions.

### Subtopics:
- **The Role of Inferential Statistics in Health Informatics**:
  - The difference between descriptive and inferential statistics in a healthcare context.
  - Ethical considerations: making responsible inferences from health data.
- **Hypothesis Testing in Clinical Research**:
  - Formulating null and alternative hypotheses.
  - Types of errors in hypothesis testing and their implications in healthcare decisions.
- **Confidence Intervals in Health Studies**:
  - Interpreting confidence intervals for medical tests and treatment efficacies.
  - The relationship between sample size, effect size, and confidence intervals.
- **Chi-square Tests in Health Research**:
  - Testing relationships between categorical variables in health datasets.
  - Examples: Testing associations between genetic markers and disease occurrences.

### Readings:
- Williams, H. (2023). Chapter 5 - Inferential Statistics. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- SciPy. (n.d.). SciPy stats documentation. Retrieved from [https://docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)


### Resources:
- [SciPy Stats for Health Research](https://docs.scipy.org/doc/scipy/reference/stats.html)

### Homework:
- [Assignment 5](WK5/assignment5.md)

---

## **Week 6: Regression Analysis in Clinical Research**
### Lecture Topic:
- Exploring the role of regression analysis in determining relationships between health variables.

### Subtopics:
- **Understanding Regression in a Health Context**:
  - Why regression is crucial in clinical studies.
  - Distinguishing causation from correlation in health outcomes.
- **Simple Linear Regression for Health Variables**:
  - Predicting one health outcome from another (e.g., predicting blood pressure from salt intake).
  - Evaluating regression assumptions using health data.
- **Multiple Regression in Clinical Trials**:
  - Controlling for confounders in health studies.
  - Interpreting coefficients and their significance in a clinical context.
- **Polynomial Regression in Health Informatics**:
  - Modeling non-linear relationships in health datasets (e.g., drug dosage and response).
  - Overfitting and its implications in health predictions.
- **Logistic Regression for Disease Prediction**:
  - Predicting categorical outcomes such as disease occurrence.
  - Understanding odds ratios and their importance in clinical decisions.

### Readings
- Williams, H. (2023). Chapter 6 - Regression Analyses. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- StatsModels. (n.d.). StatsModels documentation. Retrieved from [https://www.statsmodels.org/stable/index.html](https://www.statsmodels.org/stable/index.html)

### Resources:
- [StatsModels for Clinical Research](https://www.statsmodels.org/stable/index.html)

### Homework:
- [Assignment 6](WK6/assignment6.md)


## **Week 7: Geospatial Data in Healthcare**
### Lecture Topic:
- Leveraging geographical and spatial information for health insights and planning.

### Subtopics:
- **Introduction to Geospatial Health Data**:
  - Importance of geospatial data in epidemiology and public health planning.
  - Case studies: Tracking disease outbreaks, hospital locations, and healthcare access.
- **Working with Geospatial Data in Python**:
  - Manipulating health-related geospatial data using Geopandas.
  - Geocoding patient addresses and integrating other health datasets.
- **Visualizing Geospatial Health Data**:
  - Creating health maps: disease prevalence, vaccination rates, hospital locations.
  - Heatmaps, choropleths, and spatial clustering for health data insights.

### Readings:
- Williams, H. (2023). Chapter 7 - Geospatial Data. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- GeoPandas. (n.d.). GeoPandas documentation. Retrieved from [https://geopandas.org/](https://geopandas.org/)

### Homework:
- [Assignment 7](WK7/assignment7.md)

---

## **Week 8: Classification Techniques in Clinical Predictions**
### Lecture Topic:
- Applying classification methods to predict health outcomes and disease classifications.

### Subtopics:
- **Logistic Regression in Healthcare**:
  - Predicting binary health outcomes (e.g., presence or absence of a disease).
  - Assessing risk factors and interpreting odds ratios for clinical decision-making.
- **Decision Trees for Clinical Decision Support**:
  - Building intuitive, hierarchical models for diagnosis or treatment suggestions.
  - Understanding the decision-making process and its implications in patient care.
- **Naive Bayes for Diagnostic Tests**:
  - The basics of Bayes' theorem in the context of medical testing.
  - Using Naive Bayes for predicting disease presence based on test results and prior information.
- **Evaluating Classifier Performance in Healthcare**:
  - The importance of sensitivity, specificity, and ROC curves.
  - Addressing class imbalance in health data, and its impact on classifier performance.

### Readings:
- Williams, H. (2023). Chapter 8 - ML based Classification Techniques. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- scikit-learn. (n.d.). scikit-learn documentation. Retrieved from [https://scikit-learn.org/stable/supervised_learning.html#supervised-learning](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)

### Resources:
- [Scikit-learn for Clinical Predictions](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)

### Homework:
- [Assignment 8](WK8/assignment8.md)



## **Week 9: Ensemble Methods in Predictive Health Analytics**
### Lecture Topic:
- Enhancing clinical predictions using ensemble approaches.

### Subtopics:
- **Bagging and Boosting in Clinical Models**:
  - Concept of bootstrapping and its role in improving stability of health predictions.
  - Using boosting to reduce bias in health data models.
- **Random Forests for Patient Outcomes**:
  - The strength of decision tree ensembles in predicting patient outcomes.
  - Feature importance in random forests for identifying key health indicators.
- **Gradient Boosted Trees in Disease Prognosis**:
  - Predicting disease progression and patient trajectories.
  - Handling imbalanced datasets typical in rare disease predictions.

### Readings:
- Williams, H. (2023). Chapter 9 - Ensemble Methods in Predictive Analytics. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- scikit-learn. (n.d.). scikit-learn ensemble methods documentation. Retrieved from [https://scikit-learn.org/stable/modules/ensemble.html](https://scikit-learn.org/stable/modules/ensemble.html)

### Resources:
- [Scikit-learn Ensemble Methods for Health Informatics](https://scikit-learn.org/stable/modules/ensemble.html)

### Homework:
- [Assignment 9](WK9/assignment9.md)

---

## **Week 10: Unsupervised Learning and Model Interpretability in Healthcare**
### Lecture Topic:
- Extracting hidden patterns from health datasets and understanding the "black box" of machine learning models.

### Subtopics:
- **Clustering Techniques in Patient Segmentation**:
  - K-means clustering for patient grouping based on health metrics.
  - Hierarchical clustering for understanding patient similarity in a nested manner.
  - Case studies: Stratifying patients for personalized care.
  
- **Principal Component Analysis (PCA) in Genomics**:
  - Reducing dimensionality in high-dimensional health datasets like genomics.
  - Visualizing patient data in lower dimensions to spot patterns or anomalies.

- **Exploratory Data Analysis with Unsupervised Techniques**:
  - Using unsupervised learning for feature discovery.
  - Identifying subgroups in patient populations for targeted interventions.

- **Interpreting the "Black Box" for Clinicians**:
  - Challenges of model interpretability in healthcare.
  - Introduction to SHAP (SHapley Additive exPlanations) for explaining model predictions.
  - Visualizing feature importance and impact on predictions using SHAP plots.
  - Case studies: Ensuring trust and transparency in diagnostic AI tools.

### Readings:
- Williams, H. (2023). Chapter 10 - Unsupervised Learning and Model Interpretability. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- scikit-learn. (n.d.). scikit-learn clustering documentation. Retrieved from [https://scikit-learn.org/stable/modules/clustering.html](https://scikit-learn.org/stable/modules/clustering.html)
- SHAP. (n.d.). SHAP documentation. Retrieved from [https://github.com/slundberg/shap](https://github.com/slundberg/shap)

### Resources:
- [Scikit-learn Unsupervised Methods for Health Data](https://scikit-learn.org/stable/modules/clustering.html)
- [Interpretable Machine Learning with SHAP](https://github.com/slundberg/shap)

### Homework:
- [Assignment 10](WK10/assignment10.md)




## **Week 11: Time Series Analysis in Healthcare**
### Lecture Topic:
- Investigating health trends and forecasting future health metrics using time-indexed data.

### Subtopics:
- **Basics of Time Series in Healthcare**:
  - The importance of temporal data in health: EHRs, vitals, and more.
  - Introduction to the Pandas datetime object and time-based indexing.

- **Time Series Decomposition**:
  - Breaking down health trends into seasonality, trend, and residuals.
  - Application: Seasonal patterns in infectious disease outbreaks.

- **ARIMA Models for Patient Metrics**:
  - Introduction to ARIMA and its applicability in predicting patient vitals.
  - Case studies: Predicting hospital admissions from historical data.

- **Advanced Forecasting with Prophet**:
  - Introduction to Prophet: A tool for forecasting at scale.
  - Use cases: Predicting disease outbreaks or patient admissions with Prophet.

### Readings:
- Williams, H. (2023). Chapter 11 - Time Series Analysis. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- pandas development team. (n.d.). pandas time series documentation. Retrieved from [https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
- StatsModels. (n.d.). StatsModels time series analysis documentation. Retrieved from [https://www.statsmodels.org/stable/tsa.html](https://www.statsmodels.org/stable/tsa.html)
- Prophet. (n.d.). Prophet documentation. Retrieved from [https://facebook.github.io/prophet/](https://facebook.github.io/prophet/)

### Resources:
- [Pandas Time Series Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
- [Statsmodels for Time Series Analysis](https://www.statsmodels.org/stable/tsa.html)
- [Prophet](https://facebook.github.io/prophet/)

### Homework:
- [Assignment 11](WK11/assignment11.md)

## **Week 12: Natural Language Processing (NLP) in Clinical Contexts**
### Lecture Topic:
- Extracting actionable insights from clinical texts and patient feedback.

### Subtopics:
- **Text Preprocessing Techniques for Medical Data**:
  - Medical tokenization and the challenges of clinical texts.
  - Cleaning and standardizing clinical notes for NLP tasks.

- **Sentiment Analysis for Patient Feedback**:
  - Analyzing sentiments from patient reviews or feedback.
  - Case studies: Improving hospital services based on NLP insights.

- **Topic Modeling in Clinical Notes**:
  - Extracting key topics from a vast array of clinical documents.
  - Use cases: Identifying frequently mentioned symptoms or treatments in patient notes.

- **Information Extraction from Clinical Narratives**:
  - Named Entity Recognition (NER) with tools like MedSpacy and ScispaCy.
  - Relationships extraction for understanding drug-disease or symptom-condition links.

### Readings:
- Williams, H. (2023). Chapter 12 - Natural Language Processing (NLP). Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- Natural Language Toolkit (NLTK). (n.d.). NLTK documentation. Retrieved from [https://www.nltk.org/](https://www.nltk.org/)
- Spacy. (n.d.). Spacy documentation. Retrieved from [https://spacy.io/](https://spacy.io/)
- ScispaCy. (n.d.). ScispaCy documentation. Retrieved from [https://spacy.io/universe/project/scispacy](https://spacy.io/universe/project/scispacy)
- MedSpacy. (n.d.). MedSpacy documentation. Retrieved from [https://github.com/medspacy/medspacy](https://github.com/medspacy/medspacy)


### Resources:
- [Natural Language Toolkit (NLTK)](https://www.nltk.org/)
- [Spacy](https://spacy.io/)
- [ScispaCy](https://spacy.io/universe/project/scispacy)
- [MedSpacy](https://github.com/medspacy/medspacy)

### Homework:
- [Assignment 12](WK12/assignment12.md)


## **Week 13: Advanced Data Acquisition in Healthcare: APIs and Web-scraping**
### Lecture Topic:
- Retrieving health data and clinical information from online sources.

### Subtopics:
- **Introduction to APIs in Healthcare**:
  - Understanding health data APIs: EHRs, health datasets, wearable data, etc.
  - Hands-on: Connecting to health-related APIs for data extraction.

- **Web Scraping for Health Information**:
  - The ethics of scraping health websites: respecting robots.txt and terms of service.
  - Practical examples: Gathering clinical guidelines or drug information using Beautiful Soup and Scrapy.

### Readings:
- Williams, H. (2023). Chapter 13 - Advanced Data Acquisition: APIs and Web-scraping. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- Requests. (n.d.). Requests documentation. Retrieved from [https://docs.python-requests.org/en/master/](https://docs.python-requests.org/en/master/)
- Beautiful Soup. (n.d.). Beautiful Soup documentation. Retrieved from [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Scrapy. (n.d.). Scrapy documentation. Retrieved from [https://scrapy.org/](https://scrapy.org/)

### Resources:
- [Requests for API connections](https://docs.python-requests.org/en/master/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Scrapy](https://scrapy.org/)

### Homework:
- [Assignment 13](WK13/assignment13.md)

## **Week 14: Automating Health Data Tasks: Cron Jobs and Workflow Automation**
### Lecture Topic:
- Streamlining regular health data tasks to save time and improve consistency.

### Subtopics:
- **Introduction to Cron for Health Data Operations**:
  - Understanding the basics of cron jobs and their applications in health data processes.
  - Examples: Automatically downloading weekly health datasets or updating patient records.

- **Workflow Automation in Clinical Settings**:
  - Benefits of automating routine tasks: Patient appointment reminders, medical inventory updates, etc.
  - Hands-on: Setting up a simple automated task relevant to health informatics.

### Readings:
- Williams, H. (2023). Chapter 14 - Automating Data Tasks: Cron Jobs and Workflow Automation. Retrieved from [https://book.datascience.appliedhealthinformatics.com/](https://book.datascience.appliedhealthinformatics.com/)
- python-crontab. (n.d.). python-crontab documentation. Retrieved from [https://pypi.org/project/python-crontab/](https://pypi.org/project/python-crontab/)
- Apache Airflow. (n.d.). Apache Airflow documentation. Retrieved from [https://airflow.apache.org/](https://airflow.apache.org/)

### Resources:
- [Python Cron Libraries](https://pypi.org/project/python-crontab/)
- [Apache Airflow for Workflow Automation](https://airflow.apache.org/)

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
