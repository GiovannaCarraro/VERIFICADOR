import pytest
from escola import verificador_media

def test_string_entrada():
    with pytest.raises(TypeError, match="Tipo inválido, a entrada deve ser númerica"):
        verificador_media("CASA")

def test_numero_negativo():
    with pytest.raises(ValueError, match="O valor deve ser menor ou igual a 0 ou igual a 10"):
        verificador_media(-5)

def test_numero_maior():
    with pytest.raises(ValueError, match="O valor deve ser maior ou igual a 0 ou igual a 10"):
        verificador_media(2000)