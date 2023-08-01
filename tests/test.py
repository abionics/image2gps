import datetime
from pathlib import Path

from PIL import Image

from image2gps import image2gps

IMAGE_TIME = datetime.datetime(year=2008, month=11, day=1, hour=21, minute=15, second=7)
IMAGE_LOCATION = (43.46744833333334, 11.885126666663888)


def test_parse():
    time, location = image2gps('demo.jpg')
    assert time == IMAGE_TIME
    assert location == IMAGE_LOCATION


def test_pillow():
    image = Image.open('demo.jpg')
    time, location = image2gps(image)
    assert time == IMAGE_TIME
    assert location == IMAGE_LOCATION


def test_pathlib():
    path = Path('demo.jpg')
    time, location = image2gps(path)
    assert time == IMAGE_TIME
    assert location == IMAGE_LOCATION
