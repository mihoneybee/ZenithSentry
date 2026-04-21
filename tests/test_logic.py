import pytest
from src.logic import calcular_status_saude

def test_carga_saudavel():
    status, _ = calcular_status_saude(5)
    assert status == "VERDE"

def test_alerta_burnout_critico():
    status, _ = calcular_status_saude(10)
    assert status == "VERMELHO"

def test_impedir_horas_negativas():
    with pytest.raises(ValueError):
        calcular_status_saude(-5)
