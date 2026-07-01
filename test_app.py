from app import greet

def test_greet():
    assert "Hello, there" in greet()
