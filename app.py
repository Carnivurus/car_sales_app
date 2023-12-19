import streamlit as st
import pandas as pd
import plotly_express as px

# base de datos del proyecto
car_data = pd.read_csv("D:\\Tripleten\\datasets\\vehicles_us.csv")

st.header("Titulo del proyecto")

hist_button = st.checkbox("Histograma")
dist_button = st.checkbox("Dispersión")

if hist_button:  # al hacer click en el botón
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    # Creación de un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

if dist_button:
    st.write(
        "Se ha contruido una gráfica de dispersión"
    )
    fig2 = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig2, use_container_width=True)
