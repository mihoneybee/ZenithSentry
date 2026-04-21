import pytest
from api_service import buscar_frase_motivacional

def test_integracao_api_frases():
    """Verifica se a API retorna uma string não vazia (sucesso na conexão)."""
    frase = buscar_frase_motivacional()
    assert isinstance(frase, str)
    assert len(frase) > 10
