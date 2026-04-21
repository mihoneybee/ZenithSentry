import streamlit as st
import sys
import os

# Isso ajuda o Streamlit a encontrar a pasta 'src'
sys.path.append(os.path.abspath(os.path.curdir))

from src.logic import calcular_status_saude
from src.api_service import buscar_frase_motivacional

st.title("🛡️ ZenithSentry Web")
horas = st.number_input("Horas trabalhadas:", min_value=0.0, max_value=24.0)

if st.button("Analisar Saúde"):
    status, msg = calcular_status_saude(horas)
    st.subheader(f"Status: {status}")
    st.write(msg)
    st.info(buscar_frase_motivacional())
