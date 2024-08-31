import streamlit as st

st.title("Maritime Random Inspection (MARINS)")

st.markdown(
    """
Esta herramienta fue diseñada para ayudar a los inspectores de los puertos a evaluar el riesgo de los contenedores que llegan a los puertos.

En la siguiente tabla se muestra un resumen de los manifiestos de carga marítima.
"""
)

st.sidebar.html("<h1 style='text-align: center;'>MARINS</h1>")
st.sidebar.image("img/logo.png", use_column_width=True)
