import os
from supabase import create_client, Client

# Busca as chaves diretamente do ambiente (seguro)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Valida se as variáveis de ambiente foram configuradas
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Erro: As variáveis SUPABASE_URL e SUPABASE_KEY não foram configuradas!")

# Inicializa o cliente do banco de dados Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def salvar_historico(horas, status, mensagem):
    """Função para salvar (Create) os dados no banco de dados"""
    dados = {
        "horas_trabalhadas": horas,
        "status_calculado": status,
        "mensagem_suporte": mensagem
    }
    try:
        resposta = supabase.table("historico_saude").insert(dados).execute()
        return resposta
    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")
        return None

def ler_historico():
    """Função para buscar (Read) todos os registros do banco"""
    try:
        resposta = supabase.table("historico_saude").select("*").order("created_at", desc=True).execute()
        return resposta.data
    except Exception as e:
        print(f"Erro ao ler o banco: {e}")
        return []
