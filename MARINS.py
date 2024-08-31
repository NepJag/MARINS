import streamlit as st

st.title("Maritime Random Inspection (MARINS)")

st.markdown(
    """
Esta herramienta fue diseñada para ayudar a realizar inspecciones aleatorias en barcos de carga.

El foco de este proyecto es apoyar a realizar inspecciones de containers traidos por barcos de carga, de forma más fiable.

La idea es que luego de la evaluación de riesgo, se toma un subconjunto aleatorio de los containers riesgosos para inspeccionarlos. Además, se toma un subconjunto pequeño y aleatorio de los containers no riesgosos para inspeccionar, y así verificar la efectividad del modelo de evaluación de riesgo.

Luego de tener los containers que requieren una verificación física, se asignan de manera aleatoria a los fiscalizadores, y se les notifica de la inspección.
"""
)

st.sidebar.html("<h1 style='text-align: center;'>MARINS</h1>")
st.sidebar.image("img/logo.png", use_column_width=True)
