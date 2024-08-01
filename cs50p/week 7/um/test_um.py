
from um import count



def test_input():
    assert count("Um......., are you um, David UM, yummy?") == 3
    assert count("UM...") == 1
    assert count("YummY, UM, UM...") == 2
    assert count("um...") == 1
    assert count("yummy") == 0
