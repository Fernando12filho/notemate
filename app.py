from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv
import os
from logic.generator import transcribe_audio, generate_quiz, generate_summary

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Ensure uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    if 'audio' not in request.files:
        print("No audio file part in the request.")
        return redirect(url_for('index'))
    
    audio_file = request.files['audio']
    if audio_file.filename == '':
        print("No audio file selected.")
        return redirect(url_for('index'))
    
    # Save audio file
    filename = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
    audio_file.save(filename)

    # Transcribe audio using Whisper
    transcription = transcribe_audio(filename)

    # Generate summary and quiz using OpenAI
    summary = generate_summary(transcription)
    quiz = generate_quiz(transcription)

    # Pass results to template
    return render_template('results.html', 
                            transcript=transcription,
                            summary=summary,
                            quiz=quiz
                        )
    
@app.route("/class_view", methods=["GET"])
def class_view():
    return render_template("class.html")

@app.route("/results", methods=["GET"])
def results():
    return render_template("results.html")
if __name__ == "__main__":
    app.run(debug=True)

