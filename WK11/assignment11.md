## **Week 11: Time Series Analysis**

### **Objective**: 
Delve deep into time series data, understanding its characteristics, and applying various analytical methods to extract meaningful insights from temporal datasets.

### **Instructions**:

#### **1. Dataset Selection:**
- Find a time series dataset of your choice. This could be stock prices, weather data, sales data over time, etc. Make sure the dataset has at least 100 data points for meaningful analysis.

#### **2. Time Series Decomposition:**
- Perform a decomposition of the time series to observe its trend, seasonality, and residuals.
- Visualize each of these components in separate plots.

#### **3. Stationarity Check:**
- Check if your time series data is stationary using the Augmented Dickey-Fuller test.
- If not stationary, apply techniques such as differencing or transformations to make it stationary and retest.

#### **4. Forecasting:**
- Choose an appropriate forecasting model (e.g., ARIMA, Exponential Smoothing, Prophet).
- Train the model and make predictions for a specified future period (e.g., next 30 data points).
- Plot the original time series, the forecast, and any confidence intervals on the same graph.

#### **5. Interpretation & Reflection:**
- In markdown cells, discuss:
  - The nature of your time series data (e.g., presence of trend, seasonality).
  - Results of the stationarity test and any transformations applied.
  - Insights from the forecast and the chosen model's rationale.

#### **6. Submission**:
- Create a new GitHub repository named `datasci_11_timeseries` in your GitHub account.
- Organize your GitHub repository with the following:
  - A "datasets" folder containing your time series dataset.
  - Save your Colab/Jupyter notebook to your GitHub repository.
  - Submit the link to your GitHub repository.

#### **Resources**:

- [Time Series Decomposition](https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/)
- [Checking and Making Time Series Stationary](https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/)
- [ARIMA in Python](https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/)
- [Prophet Forecasting Tool](https://facebook.github.io/prophet/docs/quick_start.html#python-api)

---

**Tip**: Time series data can be intricate due to its temporal nature. It's crucial to understand and account for the data's components before making predictions.
