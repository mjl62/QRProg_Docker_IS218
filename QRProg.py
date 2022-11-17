import qrcode


def main():
    generate_qrcode("https://www.njit.edu/")


def generate_qrcode(url):
    qr = qrcode.QRCode(version=1, box_size=20, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    image_out = qr.make_image(fill='black', back_color='white')
    image_out.save("QRImage.png")


if __name__ == '__main__':
    main()
