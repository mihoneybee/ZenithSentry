import streamlit as st
from logic import calcular_status_saude

st.set_page_config(page_title="ZenithSentry — Entrega Final", page_icon="🛡️")

st.title("🛡️ ZenithSentry — Entrega Final")
st.subheader("Versão simplificada sem dependências externas")

horas = st.number_input("Horas trabalhadas hoje:", min_value=0.0, max_value=24.0, value=8.0)

if st.button("Analisar Status"):
    try:
        status, mensagem = calcular_status_saude(horas)
    except Exception as e:
        st.error(f"Erro ao calcular status: {e}")
    else:
        if status == "VERDE":
            st.success(f"✅ **Status: {status}**")
        elif status == "AMARELO":
            st.warning(f"⚠️ **Status: {status}**")
        else:
            st.error(f"🚨 **Status: {status}**")

        st.info(f"💬 {mensagem}")

    st.divider()
    st.write("### 💡 Pensamento do dia:")
    st.info("Mantenha pausas regulares e cuide da sua saúde mental.")
