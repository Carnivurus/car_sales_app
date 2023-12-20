import streamlit as st
import pandas as pd
import plotly_express as px

# Base of the project
car_data = pd.read_csv(
    "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv")

#######################
# Page condiguration
st.set_page_config(
    page_title="Car Sales Dashboard",
    page_icon=":blue_car:",
    initial_sidebar_state="expanded"
)

st.header("Car Sales Dashboard")

# Extraemos los elementos para usarlos en una lista desplegable
model_year = car_data["model_year"].unique()
models = car_data["model"].unique()
type_car = car_data["type"].unique()
fuel = car_data["fuel"].unique()
cylinders = car_data["cylinders"].unique()


#######################
# Sidebar
with st.sidebar:
    # Asignamos un boton que despliegue cada elemento y una variable que lo guarde
    selected_year = st.multiselect("Select the model year(s)", model_year)
    selected_model = st.multiselect(
        "Select the model(s) of the vehicle", models)
    selected_type = st.multiselect("Select the type of car", type_car)
    selected_fuel = st.multiselect("Select the type of fuel", fuel)
    selected_cylinders = st.multiselect("Select the cylinders", cylinders)

if not selected_year:
    selected_year = model_year

if not selected_model:
    selected_model = models

if not selected_type:
    selected_type = type_car

if not selected_fuel:
    selected_fuel = fuel

if not selected_cylinders:
    selected_cylinders = cylinders

# st.text(selected_year)
# st.text(selected_model)
# st.text(selected_type)
# st.text(selected_fuel)
# st.text(selected_cylinders)

df_filtered = car_data.query(
    "@selected_year in model_year and @selected_model in model and @selected_type in type and @selected_fuel in fuel and @selected_cylinders in cylinders")

#######################
# Data Visualization

# Filtered data frame
dataframe_button = st.checkbox("Show Dataframe")
if dataframe_button:
    st.dataframe(df_filtered)

# Bar Graphics
sales_per_model_button = st.checkbox("Show Sales graphic per model")

if sales_per_model_button:
    fig = px.bar(df_filtered, x="model", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Histogram
sales_per_model_button = st.checkbox("Show condition Histogram")

if sales_per_model_button:
    fig = px.bar(df_filtered["condition"])
    st.plotly_chart(fig, use_container_width=True)

#######################
