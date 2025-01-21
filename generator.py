import qrcode
import qrcode.constants

from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)
@app.route("/qrcode", methods=["GET", "POST"])
def qrcode():
    if request.method == "POST":
        """turns a string into a QR code"""
        qr = qrcode.QRCode(version=1,
                    error_correction= qrcode.constants.ERROR_CORRECT_L,
                    box_size=20,
                    border=2)
        qr.add_data("https://github.com/123shawoa/QR-code-generator")
        qr.make(fit = True)
    else:
        return render_template("code.html")

img = qr.make_image(fill_color = "black", back_color = "White")
img.save("advanced.png")