
def unique_words():
    word_histogram = {}
    with open('frost.txt','r') as f:
        for line in f:
            for word in line.split():
                single_word = word
                word_histogram[word] = word_histogram.get(word, 0) + 1
                unique_words = 0
        for word in word_histogram.keys():
            if word_histogram[word] == 1:
                unique_words += 1   
        return(unique_words)                
print(unique_words())