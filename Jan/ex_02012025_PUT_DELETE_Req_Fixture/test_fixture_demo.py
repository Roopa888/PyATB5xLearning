import pytest

@pytest.fixture()
def is_married_beforerun():
    return True

def test_update(is_married_beforerun):
    assert is_married_beforerun==True