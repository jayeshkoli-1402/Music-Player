from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


SONG_FOLDER = "static/songs"

@app.route("/")
def index(): 
    songs = []
    for song in os.listdir(SONG_FOLDER):
        if song.endswith("mp3"):
            songs.append(song)


   
    return render_template("index.html", songs=songs)

@app.route("/play/<filename>")
def play(filename):
    return send_from_directory(SONG_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
