import requests

def buscar_frase_motivacional():
    """Consome a API ZenQuotes para retornar uma frase e autor."""
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        if response.status_code == 200:
            dados = response.json()
            return f'"{dados[0]["q"]}" — {dados[0]["a"]}'
        return "Respire fundo e continue cuidando de você."
    except Exception:
        return "O equilíbrio é a chave para o sucesso duradouro."
