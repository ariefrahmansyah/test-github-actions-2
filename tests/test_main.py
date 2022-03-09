from hello import hello


def test_hello():
    got = hello("Arief")
    assert got == "Hello, Arief!"
