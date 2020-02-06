
def histogram():
    word_histogram = {}
    with open('frost.txt','r') as f:
        for line in f:
            for word in line.split():
                single_word = word
                word_histogram[word] = word_histogram.get(word, 0) + 1
    return word_histogram        

#print(histogram())


