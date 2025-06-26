import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PROJET FORTUNE Dashboard", layout="wide")

st.title("📈 PROJET FORTUNE - Dashboard de trading automatique")

# Load memory data
memory_file = "memory/trading_memory.json"
if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        memory = json.load(f)
    if memory:
        df = pd.DataFrame([
            {"Date": k, "Prix": v["data"]["price"], "Décision": v["decision"], "Votes": v["votes"]}
            for k, v in memory.items()
        ])
        df["Date"] = pd.to_datetime(df["Date"])
        df.sort_values("Date", inplace=True)
        fig = px.line(df, x="Date", y="Prix", title="Évolution des prix")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df[["Date", "Prix", "Décision"]].tail(10))
    else:
        st.warning("Aucune donnée mémoire disponible.")
else:
    st.error("Fichier de mémoire introuvable.")

# Boutons manuels
st.sidebar.header("🛠️ Contrôle Manuel")
if st.sidebar.button("Forcer une décision"):
    st.sidebar.success("Décision forcée exécutée (mock).")

if st.sidebar.button("Pause / Stop"):
    st.sidebar.warning("Trading mis en pause (mock).")