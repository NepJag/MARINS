import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MARIN Random Inspection",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.html("<h1 style='text-align: center;'>MARINS</h1>")
st.sidebar.image("img/logo.png", use_column_width=True)

riesgo_df = pd.read_csv("data/riesgo.csv")[
    [
        "Fecha",
        "Número de Contenedor",
        "Tipo de Carga",
        "Peso (kg)",
        "Nombre del Exportador",
        "Riesgo de Materiales Ilicitos",
    ]
]
riesgo_df["Fecha"] = pd.to_datetime(riesgo_df["Fecha"])

st.title("Evaluación de riesgo")

st.markdown(
    "En la siguiente tabla se muestra un resumen de " "las evaluaciones de riesgo"
)

st.data_editor(
    riesgo_df,
    column_config={
        "Fecha": st.column_config.DateColumn(format="YYYY-MM-DD"),
    },
    use_container_width=True,
    hide_index=True,
)

# grafico de densidad de riesgo
st.write("## Densidad de riesgo")

fig = px.histogram(
    riesgo_df,
    x="Riesgo de Materiales Ilicitos",
    marginal="rug",
)

st.plotly_chart(fig)

col1, col2 = st.columns(2)

with col1:
    st.write("### Exportadores con mayor riesgo")
    exportadores_riesgo = (
        riesgo_df.groupby("Nombre del Exportador")["Riesgo de Materiales Ilicitos"]
        .mean()
        .sort_values(ascending=False)
        .head(4)
    )

    st.write(exportadores_riesgo.head(10))

with col2:
    st.write("### Exportadores con menor riesgo")
    exportadores_riesgo = (
        riesgo_df.groupby("Nombre del Exportador")["Riesgo de Materiales Ilicitos"]
        .mean()
        .sort_values(ascending=True)
        .head(4)
    )

    st.write(exportadores_riesgo.head(10))
