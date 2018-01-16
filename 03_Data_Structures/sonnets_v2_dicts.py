# O(m)
import time

my_words = [elem.strip() for elem in open("./data/sonnet_words.txt", "r").readlines()]
word_list = [elem.strip() for elem in open("./data/sowpods.txt", "r").readlines()]
# Now, we are going to use dicts but not we don't care about the number of occurences of each word
word_dict = dict((elem, 1) for elem in word_list)

counter = 0

start = time.time()

for word in my_words:         # O(m)
    if word not in word_dict: # O(1), constant time
        print(word)
        counter += 1

stop = time.time()

print("Total new words: %d" % counter)
print("Time elapsed: %.1f seconds" % (stop - start))

