import streamlit as st
import pandas as pd
from logic import calcular_status_saude
from api_service import buscar_frase_motivacional

st.set_page_config(page_title="ZenithSentry — Entrega Intermediária", page_icon="🛡️")

st.title("🛡️ ZenithSentry — Entrega Intermediária")
st.subheader("Versão sem integração com o banco de dados")

horas = st.number_input("Horas trabalhadas hoje:", min_value=0.0, max_value=24.0, value=8.0)

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

st.markdown("---")
st.info("Esta versão não realiza leitura/escrita em banco de dados. Use a versão 'entrega final' para testes com banco.")
