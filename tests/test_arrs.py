from utils import arrs
import pytest

@pytest.fixture()
def coll():
    return [1, 2, 3, 4, 5, 6]

def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(coll):
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3, 4, 5, 6]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(coll, -2, -1) == [5]
    assert arrs.my_slice(coll, -7, -1) == [1, 2, 3, 4, 5]
