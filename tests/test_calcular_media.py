import pytest

def test_calcular_media():
    from main import calcular_media

    assert calcular_media([10, 20, 30]) == 20
    assert calcular_media([5, 5, 5]) == 5
    assert calcular_media([1]) == 1
    assert pytest.raises(ValueError, calcular_media, [])