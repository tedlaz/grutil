from grutil.amka import is_valid_amka


def test_is_valid_amka():
    assert not is_valid_amka(1)
    assert not is_valid_amka("1")
    assert not is_valid_amka("1a")
    assert not is_valid_amka("12345678912")
    assert not is_valid_amka("12345678912cb")
    assert is_valid_amka("13080002382")
