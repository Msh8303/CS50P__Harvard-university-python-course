import pytest
from jar import Jar

def test_init():
    Jar()

def test_str():
    jar = Jar()

    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(-2)

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(5)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(29)

