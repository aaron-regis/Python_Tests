from app import add

def test_add_correct():
    # This should pass
    assert add(10, 10) == 20

def test_add_wrong():
    # This will FAIL 
    assert add(5, 5) == 4 
