from supabase import create_client, Client

# Substitua com as informações que você copiou do painel do Supabase
SUPABASE_URL = "https://zgwbwiqbqesriutdejzj.supabase.co"
SUPABASE_KEY = "miwJaz-rakwy4-vagryj"

# Inicializa o cliente do banco de dados
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def salvar_historico(horas, status, mensagem):
    """Função para ESCREVER (Create) dados no banco"""
    dados = {
        "horas_trabalhadas": horas,
        "status_calculado": status,
        "mensagem_suporte": mensagem
    }
    # Envia os dados para a tabela correspondente no Supabase
    resposta = supabase.table("historico_saude").insert(dados).execute()
    return resposta

def ler_historico():
    """Função para LER (Read) os dados do banco"""
    # Busca todos os registros do banco ordenados pelo mais recente
    resposta = supabase.table("historico_saude").select("*").order("created_at", desc=True).execute()
    return resposta.data
