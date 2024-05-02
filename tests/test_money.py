from grutil.money import Money


def test_money():
    assert Money.euro(123.45).cents == 12345
    assert Money.euro(123.451).cents == 12345
    assert Money.euro(-10.10).cents == -1010
    va1 = Money.euro(10)
    va2 = Money.euro(0.24)
    va3 = Money.euro(20)
    res1 = va1 + va2
    assert res1.cents == 1024
    res2 = va3 - va1
    assert res2.cents == 1000
    res3 = va1 * va2
    assert res3.cents == 240
    assert res3.__str__() == "2.40€"
    assert Money.euro(1328).gr == "1.328,00€"
    assert Money.euro(1328).gr_ == "1.328,00€"
    assert Money.euro(-0).gr_ == ""
    assert Money.euro(-0).gr =="0,00€"
