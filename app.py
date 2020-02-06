from flask import Flask
from histogram import word_histogram

app = Flask(__name__)

@app.route('/')
def generate_words():
    lines = get_lines("./frost.txt")
    myhistogram = word_histogram(lines)
    sentence = ""

    num_words = 10 
    for i in range(num_words):
        word = sample_by_frequency(myhistogram)
        sentence += " " + word

    return sentence

if __name__ == '__main__':
    app.run()

#./venv/bin/python3 app.py