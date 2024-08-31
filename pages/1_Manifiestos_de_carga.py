import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MARIN Random Inspection",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.html("<h1 style='text-align: center;'>MARINS</h1>")
st.sidebar.image("img/logo.png", use_column_width=True)

manifiestos_df = pd.read_csv("data/manifiestos.csv")
manifiestos_df["Fecha"] = pd.to_datetime(manifiestos_df["Fecha"])


st.write("# Manifiestos de carga marítima")

st.markdown(
    "En la siguiente tabla se muestra un resumen de "
    "los manifiestos de carga marítima"
)

data_table = st.data_editor(
    manifiestos_df,
    column_config={
        "Fecha": st.column_config.DateColumn(format="YYYY-MM-DD"),
        "Peso (kg)": st.column_config.NumberColumn(
            min_value=0, max_value=1_000_000, step=1
        ),
    },
    use_container_width=True,
    hide_index=True,
)


st.toast("Datos cargados exitosamente", icon="📊")
