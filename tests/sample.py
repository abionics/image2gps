from image2gps import image2gps

time, coords = image2gps('demo.jpg')
print(f'Image taken in {coords} at {time}')

# Extract latitude and longitude
if coords is not None:
    lat, lon = coords
    print(f'Coordinates: {lat:.6f}, {lon:.6f}')

# From PIL object
from PIL import Image

image = Image.open('demo.jpg')
time, coords = image2gps(image)
print(f'Image taken in {coords} at {time}')

# From pathlib object
from pathlib import Path

path = Path('demo.jpg')
time, coords = image2gps(path)
print(f'Image taken in {coords} at {time}')
