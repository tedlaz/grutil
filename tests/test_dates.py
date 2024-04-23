from datetime import date, datetime

from grutil.dates import (
    date2grdate,
    grdate2date,
    grdate2isodate,
    isodate2gr,
    isodate2yearmonth,
    is_greek_date,
    delta_hours,
    round_half,
    daynight_hours,
    do_overlap,
    iso2dtime,
    time_range
)


def test_date2grdate():
    assert date2grdate(date(2020, 1, 1)) == "01/01/2020"


def test_isodate2gr():
    assert isodate2gr("2020-01-15") == "15/01/2020"


def test_isodate2yearmonth():
    assert isodate2yearmonth("2020-01-15") == "2020-01"


def test_grdate2isodate():
    assert grdate2isodate("15/01/2020") == "2020-01-15"


def test_grdate2date():
    assert grdate2date("15/01/2020") == date(2020, 1, 15)


def test_is_greek_date():
    assert is_greek_date("15/01/2020")
    assert not is_greek_date("15/1/2020")

def test_delta_hours():
    assert delta_hours(datetime(2020, 1, 1, 0, 0), datetime(2020, 1, 1, 1, 0)) == 1
    assert delta_hours(datetime(2020, 1, 1, 0, 0), datetime(2020, 1, 1, 1, 30)) == 1.5

def test_round_half():
    assert round_half(0) == 0
    assert round_half(0.5) == 0.5
    assert round_half(1) == 1
    assert round_half(1.1) == 1
    assert round_half(1.2) == 1
    assert round_half(1.3) == 1.5
    assert round_half(1.4) == 1.5
    assert round_half(1.5) == 1.5
    assert round_half(1.6) == 1.5
    assert round_half(1.7) == 1.5
    assert round_half(1.8) == 2
    assert round_half(1.9) == 2
    assert round_half(2) == 2

def test_daynight_hours():
    dapo = datetime(2020, 1, 1, 0, 0)
    deos = datetime(2020, 1, 1, 1, 30)
    assert daynight_hours(dapo, deos) == {"day_hours": 0, "night_hours": 1.5}

def test_do_overlap():
    a1 = datetime(2020, 1, 1, 0, 0)
    a2 = datetime(2020, 1, 1, 5, 30)
    b1 = datetime(2020, 1, 1, 1, 30)
    b2 = datetime(2020, 1, 1, 2, 0)
    assert do_overlap(a1, a2, b1, b2)

def test_iso2dtime():
    assert iso2dtime("2020-01-01T10:30:00") == datetime(2020, 1, 1, 10, 30, 0)
    assert iso2dtime("2020-01-01T10:30") == datetime(2020, 1, 1, 10, 30)


def test_time_range():
    assert time_range("2024-01-01T08:00T16:00") == (
        datetime(2024, 1, 1, 8, 0), datetime(2024, 1, 1, 16, 0)
    )
    assert time_range("2024-01-01T22:00T06:00") == (
        datetime(2024, 1, 1, 22, 0), datetime(2024, 1, 2, 6, 0)
    )
    assert time_range("2024-12-31T22:00T06:00") == (
        datetime(2024, 12, 31, 22, 0), datetime(2025, 1, 1, 6, 0)
    )