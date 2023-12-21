import streamlit as st
import pandas as pd
import plotly_express as px

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

# Filtered data frame
dataframe_toggle = st.toggle("Hide/Show Dataframe", value=True)
if dataframe_toggle:
    st.write(
        "The next element shows the dataframe that will be manipulated trough the filters in the side bar, feel free to use it.")
    st.write(
        "Important: If there are no filters selected, the elements below will show the entire database.")
    st.dataframe(df_filtered.head(15))

# Bar Graphics
sales_per_model_button = st.checkbox("Show sales bar graphic per model")
if sales_per_model_button:
    st.write("With the following bar chart, you can have an overview of the average prices of the models.")
    fig = px.bar(df_filtered, x="model", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Histogram
condition_button = st.checkbox("Show Condition Histogram")
if condition_button:
    st.write("Use this chart to have an idea of the conditions of the vehicules that are being sold, use the filters to have an specific insight.")
    fig = px.histogram(df_filtered["condition"])
    st.plotly_chart(fig, use_container_width=True)

# Boxplot
sales_boxplot_button = st.checkbox("Show Sales Boxplot")
if sales_boxplot_button:
    st.write(
        "The current graphic shows a boxplot of the elements related with their price.")
    fig = px.box(df_filtered, x="price")
    st.plotly_chart(fig, use_container_width=True)

odometer_hist_button = st.checkbox("Odometer Distribution Histogram")
if odometer_hist_button:  # al hacer click en el botón
    st.write(
        "With this graphic you can see odometers of the vehicles in sale")
    # Creación de un histograma
    fig = px.histogram(df_filtered, x="odometer")

    # mostrar un gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_dist_button = st.checkbox("Scatter Plot")
if scatter_dist_button:
    st.write(
        "As a second view, the scatter chart show us the behaviour of the elements related to their odometer"
    )
    fig2 = px.scatter(df_filtered, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
#######################
