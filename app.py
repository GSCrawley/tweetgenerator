from flask import Flask
from histogram import histogram
from sample_by_frequency import sample_by_frequency

app = Flask(__name__)

@app.route('/')
def generate_words():
    
    myhistogram = histogram()
    sentence = ""

    num_words = 10 
    for i in range(num_words):
        word = sample_by_frequency(myhistogram)
        print(word)
        sentence += " " + word

    return sentence

if __name__ == '__main__':
    app.run()

#./venv/bin/python3 app.py