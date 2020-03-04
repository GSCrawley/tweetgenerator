from flask import Flask
from histogram import histogram
from sample_by_frequency import sample_by_frequency
from MarkovChain import MarkovChain

app = Flask(__name__)

@app.route('/')
def generate_words():
    my_file = open("./frost.txt", "r")
    lines = my_file.readlines()
    words_list = []
    for line in lines:
        words = line.split()
        for word in words:
            words_list.append(word)
    # myhistogram = histogram()
    markovchain = MarkovChain(words_list)
    # sentence = ""

    # num_words = 10 
    # for i in range(num_words):
    #     word = sample_by_frequency(myhistogram)
    #     print(word)
    #     sentence += " " + word

    return markovchain.walk(10)

if __name__ == '__main__':
    app.run()

#./venv/bin/python3 app.py