import pytest

####################################################################################################
@pytest.fixture(scope="module")
def some_fixture():
    yield 1
    # some TearDown 

def test_something(some_fixture):
    assert some_fixture == 1