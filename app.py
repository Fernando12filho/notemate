from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv
import os
from logic.generator import generate_site_content

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    if 'audio' not in request.files:
        return redirect(url_for('index'))
    
    audio_file = request.files['audio']
    if audio_file.filename == '':
        return redirect(url_for('index'))
    
    if request.method == "POST":
        # data = {
        #     "business_name": request.form["business_name"],
        #     "location": request.form["location"],
        #     "industry": request.form["industry"],
        #     "services": request.form["services"],
        #     "tone": request.form["tone"]
        # }
        # results = generate_site_content(data)
        # return render_template("results.html", results=results, data=data)
        return "<pre>Feature not implemented yet.</pre>"

if __name__ == "__main__":
    app.run(debug=True)
