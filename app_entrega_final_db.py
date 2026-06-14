import streamlit as st
import pandas as pd
from logic import calcular_status_saude
from api_service import buscar_frase_motivacional
import database

st.set_page_config(page_title="ZenithSentry — Entrega Final (DB)", page_icon="🛡️")

st.title("🛡️ ZenithSentry — Entrega Final (com banco)")
st.subheader("Versão final com persistência local (SQLite)")

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

    # Salva no banco
    try:
        database.salvar_registro(horas, status, mensagem)
        st.success("Registro salvo no banco.")
    except Exception as e:
        st.error(f"Falha ao salvar registro: {e}")

    st.divider()
    st.write("### 💡 Pensamento do dia:")
    st.info(buscar_frase_motivacional())

# --- Seção de histórico ---
st.markdown("---")
st.header("📋 Histórico de Monitoramento")

try:
    dados_do_banco = database.ler_historico()
except Exception as e:
    st.error(f"Erro ao ler banco: {e}")
    dados_do_banco = []

if not dados_do_banco:
    st.info("Nenhum registro encontrado no banco de dados até o momento.")
else:
    df = pd.DataFrame(dados_do_banco)
    df = df.rename(columns={
        "horas_trabalhadas": "Horas Trabalhadas",
        "status_calculado": "Status de Saúde",
        "mensagem_suporte": "Mensagem / Suporte",
        "created_at": "Data/Hora de Registro"
    })

    if "id" in df.columns:
        df = df.drop(columns=["id"])

    st.write("### 📊 Tabela de Auditoria Completa")
    st.dataframe(df, use_container_width=True)
