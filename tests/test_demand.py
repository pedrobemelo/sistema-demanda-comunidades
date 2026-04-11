import pytest
from src.demand import Demand

def test_create_demand():
    d = Demand("Teste", "Desc", "Infra")
    assert d.title == "Teste"
    assert d.status == "Aberto"

def test_invalid_title():
    with pytest.raises(ValueError):
        Demand("", "Desc", "Infra")

def test_status_update():
    d = Demand("Teste", "Desc", "Infra")
    d.status = "Resolvido"
    assert d.status == "Resolvido"