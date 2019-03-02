from flask import Flask, render_template, request, send_from_directory
import os

# os.chdir(r'C:\Users\rauna\Documents\GitHub\ResumeGenerator')
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/", methods=['GET', 'POST'])
def home():
    if(request.method == 'POST'):
        return render_template('index.html')
    else:
        return render_template('index.html')

#@app.route("/static/<path:path>")
 #def static(path):
#    return send_from_directory('static', path)

if __name__ == "main":
    app.run(debug=True)
