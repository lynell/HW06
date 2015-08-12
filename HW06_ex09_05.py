#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports
def uses_all(word, string):
    for i in string:
        if i not in word:
            return False
        else:
            return True
# Body


##############################################################################
def main():
    pass  # Call your function(s) here.
    f = open("words.txt", "r")
    count = 0
    for line in f:
        if uses_all(line, "aeiou"):
            count += 1
    print "Number of words :" + str(count)
if __name__ == '__main__':
    main()
