import datetime

import piexif

from image2gps.config import TimeType
from image2gps.parse_time import parse_time

DEFAULT_EXPECTED_1 = datetime.datetime(year=2001, month=10, day=30)
DEFAULT_EXPECTED_2 = datetime.datetime(year=2001, month=10, day=30, hour=20, minute=30, second=40)


def test_date_patter_1():
    _check('2001:10:30', DEFAULT_EXPECTED_1)


def test_date_patter_2():
    _check('2001/10/30', DEFAULT_EXPECTED_1)


def test_date_patter_3():
    _check('30/10/2001', DEFAULT_EXPECTED_1)


def test_date_patter_4():
    _check('2001-10-30', DEFAULT_EXPECTED_1)


def test_date_patter_5():
    _check('30 Oct 2001', DEFAULT_EXPECTED_1)


def test_date_patter_5_lang():
    import locale
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    _check('30 Окт 2001 г.', DEFAULT_EXPECTED_1)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # reset


def test_time_patter_1_1():
    _check('2001:10:30 20:30:40', DEFAULT_EXPECTED_2)


def test_time_patter_1_2():
    expected = datetime.datetime(year=2001, month=10, day=30, hour=2, minute=3, second=5)
    _check('2001:10:30 2:3:5', expected)


def test_time_patter_1_3():
    _check('  2001:10:30  \t  20:30:40   ', DEFAULT_EXPECTED_2)


def test_time_patter_2():
    _check('2001:10:30 20:30:40+03:00', DEFAULT_EXPECTED_2)


def test_time_patter_3_1():
    expected = datetime.datetime(year=2001, month=10, day=30, hour=20, minute=30)
    _check('2001:10:30 20:30', expected)


def test_time_patter_3_2():
    expected = datetime.datetime(year=2001, month=10, day=30, hour=2, minute=5)
    _check('2001:10:30 2:5', expected)


def test_date_patter_5_with_time():
    _check('30 Oct 2001 20:30:40', DEFAULT_EXPECTED_2)


def test_time_overflow_1():
    expected = datetime.datetime(year=2001, month=10, day=30, hour=0, minute=30, second=40)
    _check('2001:10:30 24:30:40', expected)


def test_time_overflow_2():
    expected = datetime.datetime(year=2001, month=10, day=30, hour=0, minute=30, second=30)
    _check('2001:10:30 24:30:90', expected)


def test_none_1():
    _check('', None)


def test_none_2():
    _check('0000:00:00', None)


def test_min():
    _check('1900:01:01', None)


def test_max():
    _check('2100:01:01', None)


def _check(value: str, expected: TimeType):
    exif = {'0th': {piexif.ImageIFD.DateTime: value.encode()}}
    actual = parse_time(exif)
    assert actual == expected
