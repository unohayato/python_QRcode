from unittest import result
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/Users/unohayato/Documents/GitHub/python_QRcode/img/myqrcode.png')

result = decode(img)

print(result)