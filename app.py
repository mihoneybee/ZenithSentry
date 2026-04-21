import streamlit as st
import sys
import os

# Força o diretório atual no PATH do Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    # Tentativa 1: Importação padrão
    from src.logic import calcular_status_saude
    from src.api_service import buscar_frase_motivacional
except ImportError:
    # Tentativa 2: Importação caso o servidor considere 'src' o ponto de entrada
    from logic import calcular_status_saude
    from api_service import buscar_frase_motivacional

st.set_page_config(page_title="ZenithSentry 🛡️", page_icon="🛡️")

st.title("🛡️ ZenithSentry - Monitor de Saúde Mental")
st.write("Mantenha o equilíbrio entre produtividade e bem-estar.")

horas = st.number_input("Quantas horas você trabalhou hoje?", min_value=0.0, max_value=24.0, value=8.0)

if st.button("Analisar meu status"):
    status, mensagem = calcular_status_saude(horas)
    
    if status == "VERDE":
        st.success(f"**Status: {status}**")
    elif status == "AMARELO":
        st.warning(f"**Status: {status}**")
    else:
        st.error(f"**Status: {status}**")
        
    st.info(f"💡 {mensagem}")
    
    st.divider()
    st.subheader("Pensamento do dia:")
    st.write(buscar_frase_motivacional())
