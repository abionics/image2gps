from pathlib import Path

import piexif
from PIL import Image
from PIL.Image import Image as ImageType

from image2gps.config import TimeType, LocationType
from image2gps.parse_location import parse_location
from image2gps.parse_time import parse_time


def image2gps(image: ImageType | Path | str) -> tuple[TimeType, LocationType]:
    if not isinstance(image, ImageType):
        image = Image.open(image)
    exif = image.info.get('exif')
    exif = piexif.load(exif) if exif else dict()
    return parse_time(exif), parse_location(exif)
