import scrabble

vowels = "aeiou"

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

number_of_words = 0

for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)
        number_of_words += 1

print("\nTotal number of words with all vowels: {:,}\n".format(number_of_words))
