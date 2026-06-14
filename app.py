import streamlit as st
import pandas as pd
from logic import calcular_status_saude
from api_service import buscar_frase_motivacional
from database import ler_historico

st.set_page_config(page_title="ZenithSentry 🛡️", page_icon="🛡️")

st.title("🛡️ ZenithSentry")
st.subheader("Monitor de Saúde Mental")

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

# --- SEÇÃO DE HISTÓRICO DO BANCO DE DADOS ---
st.markdown("---")
st.header("📋 Histórico de Monitoramento")
st.subheader("Dados guardados em tempo real no Supabase")

# Busca os dados do banco usando a função da Mel
dados_do_banco = ler_historico()

if not dados_do_banco:
    st.info("Nenhum registro encontrado no banco de dados até o momento.")
else:
    df = pd.DataFrame(dados_do_banco)
    df_formatado = df.rename(columns={
        "horas_trabalhadas": "Horas Trabalhadas",
        "status_calculado": "Status de Saúde",
        "mensagem_suporte": "Mensagem / Suporte",
        "created_at": "Data/Hora de Registro"
    })

    if "id" in df_formatado.columns:
        df_formatado = df_formatado.drop(columns=["id"])

    st.write("### 📊 Tabela de Auditoria Completa")
    st.dataframe(df_formatado, use_container_width=True)

    st.write("### 🗂️ Últimos Registros Individuais")
    for registro in dados_do_banco[:3]:
        with st.container():
            status = registro.get("status_calculado", "Indefinido")
            emoji = "🟢" if "Bom" in status or "Estável" in status else "🟡" if "Alerta" in status else "🔴"
            st.markdown(f"""
                <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #4CAF50; color: black;">
                    <h4 style="margin-top: 0; color: black;">{emoji} Status: {status}</h4>
                    <p style="color: black;"><strong>⏱️ Horas Trabalhadas:</strong> {registro.get('horas_trabalhadas')} horas</p>
                    <p style="color: black;"><strong>💬 Nota de Suporte:</strong> {registro.get('mensagem_suporte')}</p>
                </div>
            """, unsafe_allow_html=True)
