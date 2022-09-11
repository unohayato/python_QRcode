import qrcode
data = 'My first QR code'

img = qrcode.make(data)

img.save('/Users/unohayato/Documents/GitHub/python_QRcode/img/myqrcode.png')


