import qrcode

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "https://www.facebook.com/profile.php?id=100053161790685"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "purple", back_color = "white" )
img.save("testF_Pro.png")