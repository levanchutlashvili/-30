from plates import is_valid

def test_valid_plate():
    assert is_valid("PLATE") == True

def test_invalid_plate():
    assert is_valid("PLATE12") == False
    assert is_valid("PLATE14") == False
    assert is_valid("PLATE16") == False
    assert is_valid("PLATE18") == False

def test_lowercase_digit():
    assert is_valid("plate123") == False