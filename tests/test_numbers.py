from grutil.numbers import float2gr, float2gr_, gr2float


def test_float2gr():
    assert float2gr(1234567.89) == "1.234.567,89"
    assert float2gr(1234567.89, 0) == "1.234.568"
    assert float2gr(1234567.89, 1) == "1.234.567,9"
    assert float2gr(0) == "0,00"


def test_float2gr_():
    assert float2gr_(1234567.89) == "1.234.567,89"
    assert float2gr_(1234567.89, 0) == "1.234.568"
    assert float2gr_(1234567.89, 1) == "1.234.567,9"
    assert float2gr_(0) == ""


def test_gr2float():
    assert gr2float("1.234.567,89") == 1234567.89
