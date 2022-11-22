import qrcode
from flask import flask


app = flask("/")


@app.route("/")
def generate_qrcode():
    qr = qrcode.QRCode(version=1, box_size=20, border=2)
    qr.add_data("https://www.njit.edu/")
    qr.make(fit=True)
    image_out = qr.make_image(fill='black', back_color='white')
    image_out.save("QRImage.png")
    return image_out.get_image()
