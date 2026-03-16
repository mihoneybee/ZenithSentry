def calcular_status_saude(horas_trabalhadas):
    """
    Analisa a carga horária e retorna o status de risco de burnout.
    """
    if horas_trabalhadas < 0:
        raise ValueError("A carga horária não pode ser negativa.")
        
    if horas_trabalhadas <= 6:
        return "VERDE", "Status: Equilibrado. Seu ritmo está saudável."
    elif horas_trabalhadas <= 9:
        return "AMARELO", "Status: Atenção. Considere fazer uma pausa longa agora."
    else:
        return "VERMELHO", "Status: RISCO CRÍTICO. Limite de exaustão atingido. Pare imediatamente!"
