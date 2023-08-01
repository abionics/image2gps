from image2gps import image2gps

time, location = image2gps('demo.jpg')
print(f'Image taken in {location} at {time}')

# Extract latitude and longitude
if location is not None:
    lat, lon = location
    print(f'Location: {lat:.6f}, {lon:.6f}')

# From PIL object
from PIL import Image

image = Image.open('demo.jpg')
time, location = image2gps(image)
print(f'Image taken in {location} at {time}')

# From pathlib object
from pathlib import Path

path = Path('demo.jpg')
time, location = image2gps(path)
print(f'Image taken in {location} at {time}')
