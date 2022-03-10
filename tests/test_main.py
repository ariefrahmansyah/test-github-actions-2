import os
import pytest
import subprocess

from hello import hello

@pytest.fixture(scope="module", autouse=True)
def prepare_db():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    setup_db_script = os.path.join(dir_path, "setup_db.sh")

    print("preparing db")
    subprocess.run(setup_db_script)
    print("db is ready")
    yield

def test_hello():
    got = hello("Arief")
    assert got == "Hello, Arief!"
