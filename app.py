import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer los datos del archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Configurar la página de Streamlit
st.header("Vehiculos en USA")

# Crear un boton en la aplicación Streamlit
hist_button = st.button("Construir Histograma")

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches en USA")

    # Crear un historgrama usando Plotly
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=df["odometer"])])

    fig.update_layout(title_text="Distribución del odómetro")

    # Mostrar el gráfico en plotly interactivo en la aplicación streamlit
    st.plotly_chart(fig, use_container_width=True)

# Crear un boton de dispersión en la aplicación Streamlit
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches en USA")
    fig = go.Figure(
        data=[go.Scatter(x=df["odometer"], y=df["price"], mode="markers")])
    fig.update_layout(title_text="Relación entre Odómetro y Precio")
    st.plotly_chart(fig, use_container_width=True)
