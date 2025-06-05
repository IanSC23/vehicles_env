# importamos librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Leemos datos y creamos DataFrame
car_data = pd.read_csv('/Users/iansc/Documentos/vehicles_env/vehicles_us.csv')
df = pd.DataFrame(car_data)

st.header('Vehículos en venta')

hist_button = st.button('Crear Histograma')

if hist_button:
    # escribe un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crea histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gáfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
