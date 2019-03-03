from flask import Flask, render_template, request
import downloadImgurImages

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/gpa", methods=['GET', 'POST'])
def gpa():
    if request.method == "POST":
        imgurAlbum = request.form['imgur']
        folderName = downloadImgurImages.downloadImages(imgurAlbum)

        return render_template('generic.html')
    return render_template('generic.html')
if __name__ == "main":
    app.run(debug=True)
