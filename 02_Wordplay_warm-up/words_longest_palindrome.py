import scrabble

def is_palindrome(word):
    return word == word[::-1]

count_palindromes = 0
longest = ""

for word in scrabble.wordlist:
    if is_palindrome(word):
        count_palindromes += 1
        if len(word) > len(longest):
            longest = word

print("\nTotal number of palindromes: {:d}".format(count_palindromes))
print("The longest palindrome is: {:s}\n".format(longest))

