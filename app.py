import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')

sys.path.append(current_dir)
sys.path.append(src_path)

try:
    from logic import calcular_status_saude
    from api_service import buscar_frase_motivacional
except ImportError:
    from src.logic import calcular_status_saude
    from src.api_service import buscar_frase_motivacional

st.set_page_config(page_title="ZenithSentry 🛡️", page_icon="🛡️")

st.title("🛡️ ZenithSentry")
st.subheader("Monitor de Saúde Mental e Produtividade")

horas = st.number_input("Quantas horas você trabalhou hoje?", min_value=0.0, max_value=24.0, value=8.0)

if st.button("Analisar Status"):
    status, mensagem = calcular_status_saude(horas)
    
    if status == "VERDE":
        st.success(f"✅ **Status: {status}**")
    elif status == "AMARELO":
        st.warning(f"⚠️ **Status: {status}**")
    else:
        st.error(f"🚨 **Status: {status}**")
        
    st.info(f"💬 {mensagem}")
    
    st.divider()
    st.write("### 💡 Pensamento do dia:")
    st.info(buscar_frase_motivacional())