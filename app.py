# importamos librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Leemos datos y creamos DataFrame
car_data = pd.read_csv('/Users/iansc/Documentos/vehicles_env/vehicles_us.csv')
df = pd.DataFrame(car_data)

st.title('Vehículos en venta')

st.header('Información del histograma mostrando el odómetro de los vehículos')

# Crear botón para histograma
hist_button = st.button('Crear Histograma')

if hist_button:
    # escribe un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crea histograma
    hist_fig = px.histogram(car_data, x="odometer")

    # Mostrar un gáfico Plotly interactivo
    st.plotly_chart(hist_fig, use_container_width=True)

st.divider()

st.header('Gráficos de dispersión en base a diferentes comparativas de datos')


price_year_check = st.checkbox('Compara precio con año del modelo')
price_odom_check = st.checkbox('Compara precio con millaje recorrido')

if price_year_check:
    # escribe un mensaje
    st.write(
        'Creación de un gráfico de dispersión del precio en relación al año del modelo')

    # crea histograma
    scat_pr_ye = px.scatter(car_data, x="model_year", y="price")

    # Mostrar un gáfico Plotly interactivo
    st.plotly_chart(scat_pr_ye, use_container_width=True)

if price_odom_check:
    # escribe un mensaje
    st.write(
        'Creación de un gráfico de dispersión del precio en relación al millaje recorrido del vehículo')

    # crea histograma
    scat_pr_od = px.scatter(car_data, x="odometer", y="price")

    # Mostrar un gáfico Plotly interactivo
    st.plotly_chart(scat_pr_od, use_container_width=True)
