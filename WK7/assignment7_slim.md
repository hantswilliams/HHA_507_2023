## **Week 7 (SLIM): Geospatial Data with GCP Maps API and Geopandas**

### **Objective**: 
Gain hands-on experience with geospatial data processing and visualization using the GCP Maps API and Geopandas. Understand the fundamentals of geocoding, reverse geocoding, and geospatial data visualization in Python.

### **Instructions**:

#### **1. GCP Maps API:**
- **Geocoding**: Use the GCP Maps API to perform geocoding on 100 addresses. This can be accomplished using a loop or function.
- **Reverse Geocoding**: Similarly, perform reverse geocoding on 100 latitude and longitude pairs.
- Datasets: 
    - Please usee `assignment7_slim_hospital_addresses.csv `and `assignment7_slim_hospital_coordinates.csv` for the datasets that contain the addresses and lat/long pairs. You can just randomly select 100 rows from each dataset.

#### **2. Acquire Geospatial Datasets:**
- Find at least 5 geospatial datasets that interest you, ensuring each dataset contains latitude, longitude, and other attributes (e.g., temperature, population density, or land use).

#### **3. Geospatial Data Processing and Visualization:**
- Load each dataset into a Python environment (e.g., Jupyter or Colab) using `geopandas`.
- For each dataset:
  - Perform basic data cleaning to ensure geospatial values are consistent and accurate.
  - Generate at least one basic map visualization using `geopandas` or other suitable libraries (e.g., `folium`, `matplotlib`). Ensure your map provides clear information, such as color scales for variables or markers for specific locations.

#### **4. Analysis Insights:**
- For each dataset:
  - Briefly describe the dataset and its attributes in markdown cells.
  - Highlight any patterns or anomalies you noticed on the map.
  - Explain any visualization decisions you made (e.g., choice of specific colors or markers).

#### **5. Submission**:
- Create a new GitHub repository named `datasci_7_geospatial` in your GitHub account.
- Organize your GitHub repository with the following:
  - A "datasets" folder containing the geospatial datasets you used.
  - Save your Colab/Jupyter notebook to your GitHub repository.
  - Submit the link to your GitHub repository.

---

**Tip**: Geospatial data can come in various formats (e.g., Shapefile, GeoJSON, KML). Familiarize yourself with the format of your chosen datasets and use the appropriate methods to load and process them.