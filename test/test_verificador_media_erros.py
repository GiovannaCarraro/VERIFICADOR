import pytest
from escola import verificador_media

def test_string_entrada():
    with pytest.raises(TypeError, match="Tipo inválido, a entrada deve ser númerica"):
        verificador_media("CASA")