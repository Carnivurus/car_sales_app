# car_sales_app
App using streamlit

#### Overview

This project involves analyzing a dataset of used car sales. It employs various data visualization techniques to present insights about vehicle conditions, prices, and other attributes using a Streamlit-based interactive dashboard. The goal is to create a dashboard that stakeholders can use to explore various aspects of the car sales dataset, such as average prices, conditions of vehicles, and other significant factors.

Applink: https://car-sales-vm0b.onrender.com

#### Objectives

1. Clean and preprocess the car sales dataset to prepare it for analysis.
2. Implement an interactive dashboard to filter and visualize car sales data based on several criteria such as model year, car type, fuel type, etc.
3. Provide various data visualizations including bar charts, histograms, and scatter plots to derive insights.

#### Way to Work

1. **Data Importing:** Load the car sales data into a DataFrame from a CSV file.
2. **Data Cleaning:**
    - Remove rows with missing values in the `model_year` column.
    - Convert columns to appropriate data types (e.g., converting `date_posted` to datetime).
3. **Interactive Dashboard:**
    - Use Streamlit to create an interactive dashboard.
    - Allow users to filter data based on model year, model, type, fuel type, and cylinders.
    - Present the filtered data in various visual formats, including bar charts, histograms, box plots, and scatter plots.
4. **Data Visualization:**
    - Enable users to toggle between different views and visualizations.
    - Visualize data to show key insights about car conditions, prices, odometer readings, etc.
  
#### Requirements

- pandas
- plotly_express
- Streamlit

#### Installation for Requirements

To install the required packages, use the following command:

```bash
pip install -r requirements.txt
```
