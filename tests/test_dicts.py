from utils import dicts


def test_get_val():
    assert dicts.get_val({"a": "1", "b": "2", "c": "3"}, "a", "git") == "1"
    assert dicts.get_val({"a": "1", "b": "2", "c": "3"}, "d", "git") == "git"
    assert dicts.get_val({}, "d", "git") == "git"
