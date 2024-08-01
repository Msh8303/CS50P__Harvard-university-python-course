from numb3rs import validate
import sys

def main():
    test_numbers()
    test_not_separated()
    test_punc()
    test_chars()
    sys.exit()


def test_numbers():
    assert validate('253.255.255.255') == True
    assert validate('127.0.1.1') == True
    assert validate('256.256.2.2') == False

def test_chars():
    assert validate('c.2.2.2') == False
    assert validate('cat') == False

def test_punc():
    assert validate('2.2.2.!') == False
    assert validate ('?1111') == False

def test_not_separated():
    assert validate('255255255255') == False
    assert validate('0000') == False
    assert validate ('1.1.1.1') == True