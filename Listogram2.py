from random import randint
from dictogram import histogram
from listogram import listogram

class Listogram:

    def __init__(self, word_list):
        '''Initializes the listogram properties'''

        self.word_list = word_list
       
        self.list_histogram = self.build_listogram()

        self.tokens = self.get_num_tokens()
        self.types = self.unique_words()

    def build_listogram(self): 
        '''Creates a histogram list of lists using the word_list property and returns it'''
        listogram = []
        for word in listogram:
            word = word.rstrip()
            result = get_index(word, listogram)
            if result == "nope didn't find it":
                listogram.append([word,1])
            else:
                listogram[result][1] += 1
    
        return listogram

    lines = open("frost.txt", "r").readlines()
    print(listogram(lines))
    
    def get_num_tokens(self):
        '''gets the number of tokens in the listogram'''
        tokens = 0
        for item in self.list_histogram:
            tokens += item[1]
        return tokens

    def get_index(self, word, listogram):
        '''searches in the list histogram parameter and returns the index of the inner list that contains the word if present'''
        result = 0
        for inner_list in listogram:
            if inner_list[0] == word:
                return result
            else:
                result += 1
                return "nope didn't find it"

    def frequency(self, word):
        '''returns the frequency or count of the given word in the list of lists histogram'''
        return self.list_histogram
        print(frequency(self.word_histogram, 'one'))
        
    def unique_words(self):
        '''returns the number of unique words in the list of lists histogram'''
        word_histogram = {}
        return len(self.list_histogram)
 
    def sample(self):
        '''Randomly samples from the list of list histogram based on the frequency, returns a word'''
        random_index = randint(0, self.tokens -1)
        start = 0
        for word, count in self.list_histogram.items:
            end = start + count
            if random_index >= start and random_index < end:
                return word
            else:
                start = end
            print(sample(self))

def print_listogram(word_list):
    '''Creates a list based histogram (listogram) and then prints out its properties and samples from it'''

    print()
    print('List of Lists Histogram:')
    print('word list: {}'.format(word_list))
# Create a dictogram and display its contents
    listogram = Listogram(word_list)
    print('listogram: {}'.format(listogram.list_histogram))
    print('{} tokens, {} types'.format(listogram.tokens, listogram.types))
    for word in word_list[-2:]:
        freq = listogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    

def print_dictogram_samples(listogram):
    '''Compares sampled frequency to observed frequency'''

    print('List of Lists Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [listogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist.list_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for item in listogram.list_histogram:
        word = item[0]
        count = item[1]
        # Calculate word's observed frequency
        observed_freq = count / listogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()

#print_dictogram_samples(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])

print_listogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])