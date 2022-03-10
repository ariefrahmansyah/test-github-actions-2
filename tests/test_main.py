import pytest

from hello import hello

@pytest.mark.integration
def test_hello():
    got = hello("Arief")
    assert got == "Hello, Arief!"
