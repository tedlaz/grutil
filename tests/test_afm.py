from grutil.afm import is_valid_afm


def test_is_valid_afm():
    assert not is_valid_afm(1)
    assert not is_valid_afm("1")
    assert not is_valid_afm("1a")
    assert not is_valid_afm("123456789")
    assert not is_valid_afm("123456789b")
    assert is_valid_afm("012312312")