# importamos librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Leemos datos y creamos DataFrame
car_data = pd.read_csv('/Users/iansc/Documentos/vehicles_env/vehicles_us.csv')
df = pd.DataFrame(car_data)

st.header('Vehículos en venta')

hist_check = st.checkbox('Crear Histograma')
scat_check = st.checkbox('Crear un gráfico de dispersión')

if hist_check:
    # escribe un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crea histograma
    hist_fig = px.histogram(car_data, x="odometer")

    # Mostrar un gáfico Plotly interactivo
    st.plotly_chart(hist_fig, use_container_width=True)

if scat_check:
    # escribe un mensaje
    st.write(
        'Creación de un gráfico de dispersión del precio en relación al año del modelo')

    # crea histograma
    scat_fig = px.scatter(car_data, x="model_year", y="price")

    # Mostrar un gáfico Plotly interactivo
    st.plotly_chart(scat_fig, use_container_width=True)
