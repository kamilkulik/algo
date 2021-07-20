from src.run_length_encoding.run_length_encoding import run_length_encoding

def test_run_length_encoding_1():
    assert run_length_encoding('AAAAAAAAAAAAABBBBCCDDDDD') == '9A4A4B2C5D'

def test_run_length_encoding_2():
    assert run_length_encoding('aA') == '1a1A'
    
def test_run_length_encoding_3():
    assert run_length_encoding('*********^^^^^))))))@@') == '9*5^6)2@'

def test_run_length_encoding_4():
    assert run_length_encoding('                          ') == '9 9 8 '

def test_run_length_encoding_5():
    assert run_length_encoding('1A2B3CCC') == '111A121B133C'
