import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np

#######################
# Base of the project
car_data = pd.read_csv(
    "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv")

# Cleaning database
car_data = car_data.dropna(subset="model_year")
car_data["date_posted"] = pd.to_datetime(car_data["date_posted"])
car_data["model_year"] = car_data["model_year"].astype(int)

#######################
# Page configuration
st.set_page_config(
    page_title="Car Sales Dashboard",
    page_icon=":blue_car:",
    initial_sidebar_state="expanded"
)

st.header("Car Sales Dashboard")

# Extraemos los elementos para usarlos en una lista desplegable
model_year = sorted(car_data["model_year"].unique().tolist(), reverse=True)
models = sorted(car_data["model"].unique().tolist())
type_car = sorted(car_data["type"].unique().tolist())
fuel = sorted(car_data["fuel"].unique().tolist())
cylinders = sorted(car_data["cylinders"].unique().tolist())

#######################
# Sidebar


with st.sidebar:
    selected_year = st.multiselect(
        "Select the model year(s)", model_year) or model_year
    selected_model = st.multiselect(
        "Select the model", sorted(car_data.query("@selected_year in model_year")["model"].unique())) or models
    selected_type = st.multiselect(
        "Select the type of car", sorted(car_data.query("@selected_year in model_year and @selected_model in model")["type"].unique())) or type_car
    selected_fuel = st.multiselect(
        "Select the type of fuel", sorted(car_data.query("@selected_year in model_year and @selected_model in model and @selected_type in type")["fuel"].unique())) or fuel
    selected_cylinders = st.multiselect(
        "Select the cylinders", sorted(car_data.query("@selected_year in model_year and @selected_model in model and @selected_type in type and @selected_fuel in fuel")["cylinders"].unique())) or cylinders

# st.text(selected_year)
# st.text(selected_model)
# st.text(selected_type)
# st.text(selected_fuel)
# st.text(selected_cylinders)

df_filtered = car_data.query(
    "@selected_year in model_year and @selected_model in model and @selected_type in type and @selected_fuel in fuel and @selected_cylinders in cylinders")

#######################
# Data Visualization


dataframe_button = st.checkbox("Show Dataframe")
sales_per_model_button = st.checkbox("Show Sales Bar Graphic per model")
sales_per_model_button = st.checkbox("Show Condition Histogram")
sales_per_model_button = st.checkbox("Show Sales Boxplot")
odometer_hist_button = st.checkbox("Odometer Distribution Histogram")
odometer_dist_button = st.checkbox("Scatter Plot")

# Filtered data frame
if dataframe_button:
    st.dataframe(df_filtered.head(15))

# Bar Graphics
if sales_per_model_button:
    fig = px.bar(df_filtered, x="model", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Histogram
if sales_per_model_button:
    fig = px.histogram(df_filtered["condition"])
    st.plotly_chart(fig, use_container_width=True)

# Boxplot
if sales_per_model_button:
    fig = px.box(df_filtered, x="price")
    st.plotly_chart(fig, use_container_width=True)


if odometer_hist_button:  # al hacer click en el botón
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    # Creación de un histograma
    fig = px.histogram(df_filtered, x="odometer")

    # mostrar un gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

if odometer_dist_button:
    st.write(
        "Se ha contruido una gráfica de dispersión"
    )
    fig2 = px.scatter(df_filtered, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
#######################
