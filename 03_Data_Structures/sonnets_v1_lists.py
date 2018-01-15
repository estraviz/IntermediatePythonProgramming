# O(m*n)
import time

my_words = [elem.strip() for elem in open("sonnet_words.txt", "r").readlines()]
word_list = [elem.strip() for elem in open("sowpods.txt", "r").readlines()]

counter = 0

start = time.time()

for word in my_words:         # O(m)
    if word not in word_list: # O(n)
        print(word)
        counter += 1

stop = time.time()

print("Total new words: %d" % counter)
print("Time elapsed: %.1f seconds" % (stop - start))

