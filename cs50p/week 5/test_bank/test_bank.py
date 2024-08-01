from bank import value


def test_not_h():
    assert value("Greetigs") == 100


def test_hello():
    assert value("HELLO") == 0



def test_start_with_h():
    assert value("Hey, world") == 20
    assert value("Hi, world") == 20