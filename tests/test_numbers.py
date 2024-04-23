from grutil.numbers import float2grnum, float2grnum_or_space, grnum2float


def test_float2grnum():
    assert float2grnum(1234567.89) == "1.234.567,89"
    assert float2grnum(1234567.89, 0) == "1.234.568"
    assert float2grnum(1234567.89, 1) == "1.234.567,9"
    assert float2grnum(0) == "0,00"


def test_float2grnum_or_space():
    assert float2grnum_or_space(1234567.89) == "1.234.567,89"
    assert float2grnum_or_space(1234567.89, 0) == "1.234.568"
    assert float2grnum_or_space(1234567.89, 1) == "1.234.567,9"
    assert float2grnum_or_space(0) == ""


def test_grnum2float():
    assert grnum2float("1.234.567,89") == 1234567.89
