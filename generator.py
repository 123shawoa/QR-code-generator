import qrcode

img = qrcode.make("Hello")
img.save("mycode.png")
