from random import randint

text = 'one fish two fish red fish blue fish'
word_counts = {'one': 1, 'fish': 4, 'two': 1,
               'red': 1, 'blue': 1}
               
               
def sample_by_frequency(histogram):
      random_index = randint(0, sum(histogram.values()) -1)
      start = 0   
      for word, count in histogram.items():
        end = start + count
        if random_index >= start and random_index < end:
          return word
        else:
          start = end
          
print(sample_by_frequency(word_counts))