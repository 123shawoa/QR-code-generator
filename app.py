import qrcode
import qrcode.constants

from flask import Flask, flash, redirect, render_template, request, send_file,url_for
import os
app = Flask(__name__)
app.secret_key = 'key'
@app.route("/")

def home():
    return render_template("homepage.html")
@app.route("/qrs", methods=["GET", "POST"])
def qrs():
    if request.method == "POST":
        """turns a string into a QR code"""
        data = request.form.get("data")
        if not data:
            flash("Please enter some data to create a QR code")
            return redirect(url_for('qrs'))
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
        cool = "advanced.png"
        img.save(cool)
        
        return send_file(cool, as_attachment=True)
    else:
        return render_template("code.html")
if __name__ == '__main__':
    app.run(debug=True)

