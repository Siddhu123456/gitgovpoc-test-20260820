from app import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 999  # intentionally broken for merge-gate live test
