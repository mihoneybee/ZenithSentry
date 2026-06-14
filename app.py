import streamlit as st
from logic import calcular_status_saude
from api_service import buscar_frase_motivacional

st.set_page_config(page_title="ZenithSentry 🛡️", page_icon="🛡️")

st.title("🛡️ ZenithSentry")
st.subheader("Versão pública — sem conexão ao banco")

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
st.info("Esta instância do app foi configurada para rodar sem integração com banco de dados. Para a versão com banco, use o app de entrega final.")
