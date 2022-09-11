from turtle import fillcolor
import qrcode
data = 'My first QR code'

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color='red', back_color='black')


img.save('/Users/unohayato/Documents/GitHub/python_QRcode/img/myqrcode1.png')


