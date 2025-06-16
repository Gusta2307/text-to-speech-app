from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        filename = request.form["filename"]
        language = 'es'
        tts = gTTS(text=text, lang=language, slow=False)
        filepath = f"{filename}.mp3"
        tts.save(filepath)
        return send_file(filepath, as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
