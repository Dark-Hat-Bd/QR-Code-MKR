from flask import Flask, send_file, request, render_template
import os
import qrcode

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['data']
        print(title)
        img = qrcode.make(title)
        try:
            os.remove("image.png")
        except:
            pass
        finally:
            img.save('image.png')
    return render_template('index.html')


@app.route("/download", methods=['GET', 'POST'])
def download_file():
    p = "image.png"
    return send_file(p, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)