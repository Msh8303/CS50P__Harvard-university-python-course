import pytest
from fuel import convert, gauge


def test_convert():
    assert convert('5/10') == 50
    assert convert('2/3') == 67
    assert convert('1/100') == 1
    assert convert('99/100') == 99


def test_gauge():
    assert gauge(50) == '50%'
    assert gauge(1) == 'E'
    assert gauge(99) == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value():
    with pytest.raises(ValueError):
        convert('2/1')

