def obter_cor_ansi(nivel):
    """
    Retorna o código ANSI para a cor correspondente ao nível de risco.
    
    Args:
        nivel (str): O nível de classificação (AZUL, VERDE, AMARELO, LARANJA, VERMELHO)
    
    Returns:
        str: Código ANSI da cor
    """
    cores = {
        "AZUL": "\033[94m",      # Azul claro
        "VERDE": "\033[92m",     # Verde claro
        "AMARELO": "\033[93m",   # Amarelo claro
        "LARANJA": "\033[38;5;208m",  # Laranja (256 cores)
        "VERMELHO": "\033[91m"   # Vermelho claro
    }
    return cores.get(nivel, "\033[0m")


def obter_reset_ansi():
    """Retorna o código ANSI para resetar a cor."""
    return "\033[0m"


def calcular_status_saude(horas_trabalhadas):
    """
    Analisa a carga horária e retorna o status de risco de burnout com novo sistema de 5 níveis.
    
    Níveis de classificação:
    - AZUL (0h a 4h): Carga muito leve
    - VERDE (4h a 6h): Ritmo saudável
    - AMARELO (6h a 8h): Atenção
    - LARANJA (8h a 10h): Risco elevado
    - VERMELHO (acima de 10h): Risco crítico
    
    Args:
        horas_trabalhadas (float): Total de horas trabalhadas no dia
    
    Returns:
        tuple: (nivel, mensagem) contendo o status e mensagem descritiva
    
    Raises:
        ValueError: Se a carga horária for negativa
    """
    if horas_trabalhadas < 0:
        raise ValueError("A carga horária não pode ser negativa.")
    
    if horas_trabalhadas <= 4:
        return "AZUL", "Status: Carga Muito Leve. Você pode aumentar sua produtividade se desejar."
    elif horas_trabalhadas <= 6:
        return "VERDE", "Status: Ritmo Saudável. Seu ritmo está equilibrado e sustentável."
    elif horas_trabalhadas <= 8:
        return "AMARELO", "Status: Atenção. Você está no limite saudável. Considere fazer uma pausa longa."
    elif horas_trabalhadas <= 10:
        return "LARANJA", "Status: Risco Elevado. Você está entrando em zona de perigo. Considere encerrar em breve."
    else:
        return "VERMELHO", "Status: RISCO CRÍTICO. Limite de exaustão atingido. Pare imediatamente!"
