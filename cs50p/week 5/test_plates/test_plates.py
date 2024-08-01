from plates import is_valid



def test_start():
    assert is_valid("Cs50") == True
    assert is_valid("C50s") == False
    assert is_valid("C") == False
    assert is_valid("50cs") == False
    assert is_valid("Cs") == True

def test_length():
    assert is_valid('C') == False
    assert is_valid('Cs') == True
    assert is_valid('Cs50cs') == False
    assert is_valid('Cscscscscs') == False

def test_number():
    assert is_valid('111') == False
    assert is_valid('1A1') == False
    assert is_valid('Cs50') == True

def test_zero():
    assert is_valid('Cs05') == False
    assert is_valid('Cs50') == True
    assert is_valid('0cs5') == False

def test_signs():
    assert is_valid('Cs50!') == False
    assert is_valid('Cs50,x') == False
