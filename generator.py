import qrcode
import qrcode.constants

from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)
@app.route("/qrcode", methods=["GET", "POST"])
def qrcode():
    if request.method == "POST":
        """turns a string into a QR code"""
        data = request.form.get("data")
        if not data:
            flash("Please enter some data to create a QR code")
        color = request.form.get("color")
        if not color:
            color = "black"
        qr = qrcode.QRCode(version=1,
                    error_correction= qrcode.constants.ERROR_CORRECT_L,
                    box_size=20,
                    border=2)
        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image(fill_color = color, back_color = "White")
        img.save("advanced.png")
    else:
        return render_template("code.html")

