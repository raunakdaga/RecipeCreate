from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/gpa")
def gpa():
    return render_template('generic.html')
if __name__ == "main":
    app.run(debug=True)
