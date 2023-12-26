import pandas as pd
import plotly.express as px
import streamlit as st

# Histograma con boton 

data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Construccion de Histograma')


button = st.button('Construir histograma') # crear un botón

if button: # al hacer clic en el botón
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(data, x="odometer")

    # mostrar grafico
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')

# botón gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # gráfico de dispersión
    fig = px.scatter(data, x="price", y="odometer")

    # mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)
