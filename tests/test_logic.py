import pytest
from src.logic import calcular_status_saude, obter_cor_ansi, obter_reset_ansi


# ===== Testes dos Cinco Níveis de Classificação =====

def test_nivel_azul_carga_muito_leve():
    """Testa classificação AZUL (0h a 4h): Carga muito leve"""
    status, mensagem = calcular_status_saude(2)
    assert status == "AZUL"
    assert "Carga Muito Leve" in mensagem


def test_nivel_verde_ritmo_saudavel():
    """Testa classificação VERDE (4h a 6h): Ritmo saudável"""
    status, mensagem = calcular_status_saude(5)
    assert status == "VERDE"
    assert "Ritmo Saudável" in mensagem


def test_nivel_amarelo_atencao():
    """Testa classificação AMARELO (6h a 8h): Atenção"""
    status, mensagem = calcular_status_saude(7)
    assert status == "AMARELO"
    assert "Atenção" in mensagem


def test_nivel_laranja_risco_elevado():
    """Testa classificação LARANJA (8h a 10h): Risco elevado"""
    status, mensagem = calcular_status_saude(9)
    assert status == "LARANJA"
    assert "Risco Elevado" in mensagem


def test_nivel_vermelho_risco_critico():
    """Testa classificação VERMELHO (acima de 10h): Risco crítico"""
    status, mensagem = calcular_status_saude(11)
    assert status == "VERMELHO"
    assert "RISCO CRÍTICO" in mensagem


# ===== Testes dos Limites de Intervalos =====

def test_limite_azul_4_horas():
    """Testa se 4 horas está no limite superior do AZUL"""
    status, _ = calcular_status_saude(4)
    assert status == "AZUL"


def test_limite_verde_4_horas():
    """Testa se 4 horas no VERDE (limite inferior)"""
    status, _ = calcular_status_saude(4.1)
    assert status == "VERDE"


def test_limite_verde_6_horas():
    """Testa se 6 horas está no limite superior do VERDE"""
    status, _ = calcular_status_saude(6)
    assert status == "VERDE"


def test_limite_amarelo_6_horas():
    """Testa se 6 horas está no limite inferior do AMARELO"""
    status, _ = calcular_status_saude(6.1)
    assert status == "AMARELO"


def test_limite_amarelo_8_horas():
    """Testa se 8 horas está no limite superior do AMARELO"""
    status, _ = calcular_status_saude(8)
    assert status == "AMARELO"


def test_limite_laranja_8_horas():
    """Testa se 8 horas está no limite inferior do LARANJA"""
    status, _ = calcular_status_saude(8.1)
    assert status == "LARANJA"


def test_limite_laranja_10_horas():
    """Testa se 10 horas está no limite superior do LARANJA"""
    status, _ = calcular_status_saude(10)
    assert status == "LARANJA"


def test_limite_vermelho_10_horas():
    """Testa se 10 horas está no limite inferior do VERMELHO"""
    status, _ = calcular_status_saude(10.1)
    assert status == "VERMELHO"


# ===== Testes de Valores Especiais =====

def test_zero_horas():
    """Testa comportamento com 0 horas trabalhadas"""
    status, mensagem = calcular_status_saude(0)
    assert status == "AZUL"
    assert "Carga Muito Leve" in mensagem


def test_horas_negativas():
    """Testa se valores negativos geram erro"""
    with pytest.raises(ValueError, match="A carga horária não pode ser negativa"):
        calcular_status_saude(-5)


def test_horas_negativas_pequeno():
    """Testa se um pequeno valor negativo também gera erro"""
    with pytest.raises(ValueError):
        calcular_status_saude(-0.1)


# ===== Testes de Cores ANSI =====

def test_obter_cor_ansi_azul():
    """Testa se a cor AZUL retorna o código ANSI correto"""
    cor = obter_cor_ansi("AZUL")
    assert cor == "\033[94m"


def test_obter_cor_ansi_verde():
    """Testa se a cor VERDE retorna o código ANSI correto"""
    cor = obter_cor_ansi("VERDE")
    assert cor == "\033[92m"


def test_obter_cor_ansi_amarelo():
    """Testa se a cor AMARELO retorna o código ANSI correto"""
    cor = obter_cor_ansi("AMARELO")
    assert cor == "\033[93m"


def test_obter_cor_ansi_laranja():
    """Testa se a cor LARANJA retorna o código ANSI correto"""
    cor = obter_cor_ansi("LARANJA")
    assert cor == "\033[38;5;208m"


def test_obter_cor_ansi_vermelho():
    """Testa se a cor VERMELHO retorna o código ANSI correto"""
    cor = obter_cor_ansi("VERMELHO")
    assert cor == "\033[91m"


def test_obter_cor_ansi_invalida():
    """Testa se uma cor inválida retorna reset ANSI"""
    cor = obter_cor_ansi("INVALIDA")
    assert cor == "\033[0m"


def test_obter_reset_ansi():
    """Testa se reset ANSI retorna o código correto"""
    reset = obter_reset_ansi()
    assert reset == "\033[0m"
