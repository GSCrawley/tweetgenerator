import sys as sys
from random import randint

if __name__ == "__main__":
    args = sys.argv

    words = args[1:]

for word in words:
    rand_words = randint(0, len(words) - 1)
    rand_item = words[rand_words]
    print(rand_item);
