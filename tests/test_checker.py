from checker import is_strong

def test_strong_password():
    assert is_strong("Abc!1234") is True

def test_weak_password():
    assert is_strong("abc123") is False
