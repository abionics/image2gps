import datetime
from pathlib import Path

from PIL import Image

from image2gps import image2gps
from image2gps.config import TimeType, CoordsType

IMAGE_TIME = datetime.datetime(year=2008, month=11, day=1, hour=21, minute=15, second=7)
IMAGE_COORDS = (43.46744833333334, 11.885126666663888)


def test_parse():
    time, coords = image2gps('demo.jpg')
    assert time == IMAGE_TIME
    assert coords == IMAGE_COORDS
    _check(time, coords)


def test_pillow():
    image = Image.open('demo.jpg')
    time, coords = image2gps(image)
    assert time == IMAGE_TIME
    assert coords == IMAGE_COORDS
    _check(time, coords)


def test_pathlib():
    path = Path('demo.jpg')
    time, coords = image2gps(path)
    _check(time, coords)


def _check(time: TimeType, coords: CoordsType):
    assert time == IMAGE_TIME
    assert coords == IMAGE_COORDS
