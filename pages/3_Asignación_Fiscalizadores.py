import streamlit as st
import pandas as pd
import utils as ut

st.sidebar.html("<h1 style='text-align: center;'>MARINS</h1>")
st.sidebar.image("img/logo.png", use_column_width=True)

# CARGA DE DATOS #
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

riesgosos_df = riesgo_df[riesgo_df["Riesgo de Materiales Ilicitos"] >= 0.9][
    "Número de Contenedor"
]
no_riesgosos_df = riesgo_df[riesgo_df["Riesgo de Materiales Ilicitos"] < 0.9][
    "Número de Contenedor"
]

fiscalizadores_df = pd.read_csv("data/fiscalizadores.csv")
fiscalizadores_id = fiscalizadores_df["ID"].to_list()

# FIN CARGA DE DATOS #

st.title("Asignación de Fiscalizadores")

col1, col2 = st.columns(2)

with col1:
    st.write("### Fiscalizadores")
    st.data_editor(fiscalizadores_df, use_container_width=True, hide_index=True)

with col2:
    st.write("### Contenedores riesgosos")
    st.markdown("Los contenedores con riesgo mayor 0.9 son considerados riesgosos")
    st.data_editor(riesgosos_df, use_container_width=True, hide_index=True)

# separacion
st.write("---")

final_sample, non_risk_sample = ut.risk_nonrisk_sample(
    riesgosos_df.to_list(), no_riesgosos_df.to_list(), 10
)

asignaciones = ut.run_association(final_sample, fiscalizadores_id, n=2)

asignaciones_df = pd.DataFrame(
    asignaciones.items(), columns=["Fiscalizador", "Contenedores"]
)

st.write("### Asignaciones aleatorias y verificables")

st.data_editor(asignaciones_df, use_container_width=True, hide_index=True)
