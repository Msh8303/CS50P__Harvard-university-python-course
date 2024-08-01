from twttr import shorten


def test_no_vowel():
    assert shorten('cdf') == 'cdf'

def test_small_vowel():
    assert shorten('hello') == 'hll'
    assert shorten ('good') == 'gd'

def test_capital_vowel():
    assert shorten('HELLO') == 'HLL'
    assert shorten ('GOOD') == 'GD'

def test_mixed():
    assert shorten('HEllo') == 'Hll'

def test_punc():
    assert shorten ('Hello, Emma!') == 'Hll, mm!'

def test_num():
    assert shorten ('I Am 12 years old') == ' m 12 yrs ld'

