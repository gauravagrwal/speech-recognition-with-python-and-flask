from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ''
    if request.method == 'POST':
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audiofile = sr.AudioFile(file)
            with audiofile as source:
                data = recognizer.record(source)

            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)

    return render_template('index.html', transcript=transcript)

@app.route('/about')
def about():
    return 'By Gaurav Agrawal'