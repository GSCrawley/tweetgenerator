word_histogram = {}
with open('frost.txt','r') as f:
    for line in f:
        for word in line.split():
            single_word = word
            word_histogram[word] = word_histogram.get(word, 0) + 1

def frequency(word, histogram):
    return histogram[word]
print(frequency("orchard", word_histogram))


