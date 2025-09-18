from app import greet

def test_greet_message():
    result = greet("TestUser")
    assert "Hello, TestUser!" in result

