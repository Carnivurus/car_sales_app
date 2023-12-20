import streamlit as st
import pandas as pd
import plotly_express as px

# base de datos del proyecto
car_data = pd.read_csv(
    "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv")


st.header("Car Sales Dashboard")

# Establecemos la configuración de todos nuestros filtros
model_year = car_data["model_year"].unique()
models = car_data["model"].unique()


# Asignamos un boton que despliegue cada elemento y una variable que lo guarde
selected_year = st.multiselect("Select the model year(s)", model_year)
selected_model = st.multiselect("Select the model(s)", models)

if not selected_year:
    selected_year = model_year

if not selected_model:
    selected_model = models

df_filtered = car_data.query(
    "@selected_year in model_year and @selected_model in model")

st.text(selected_year)
st.text(selected_model)
st.dataframe(df_filtered)

sales_per_model_button = st.checkbox("Show sales graphic per model")

if sales_per_model_button:

    fig = px.bar(df_filtered, x="model", y="price")
    st.plotly_chart(fig, use_container_width=True)


# hist_button = st.checkbox("Histograma")
# dist_button = st.checkbox("Dispersión")

# if hist_button:  # al hacer click en el botón
#     st.write(
#         "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
#     # Creación de un histograma
#     fig = px.histogram(car_data, x="odometer")

#     # mostrar un gráfico interactivo
#     st.plotly_chart(fig, use_container_width=True)

# if dist_button:
#     st.write(
#         "Se ha contruido una gráfica de dispersión"
#     )
#     fig2 = px.scatter(car_data, x="odometer", y="price")

#     st.plotly_chart(fig2, use_container_width=True)


# import streamlit as st
# import pandas as pd
# import plotly_express as px

# # base de datos del proyecto
# car_data = pd.read_csv(
#     "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv")


# st.header("Titulo del proyecto")

# hist_button = st.checkbox("Histograma")
# dist_button = st.checkbox("Dispersión")

# if hist_button:  # al hacer click en el botón
#     st.write(
#         "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
#     # Creación de un histograma
#     fig = px.histogram(car_data, x="odometer")

#     # mostrar un gráfico interactivo
#     st.plotly_chart(fig, use_container_width=True)

# if dist_button:
#     st.write(
#         "Se ha contruido una gráfica de dispersión"
#     )
#     fig2 = px.scatter(car_data, x="odometer", y="price")

#     st.plotly_chart(fig2, use_container_width=True)
