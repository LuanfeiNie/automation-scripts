# tests/test_hello.py
from scripts.hello import greet

def test_greet_returns_string():
    assert isinstance(greet("Alice"), str)

def test_greet_content():
    assert greet("Alice") == "Hello, Alice!"
