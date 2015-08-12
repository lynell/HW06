#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports
def uses_only(word, letters):
    for i in word:
        if i not in letters:
            return False
        else:
            return True
    



# Body


##############################################################################
def main():
    pass  # Call your function(s) here.
    f = open("words.txt","r")
    count = 0
    for line in f:
        if uses_only(line,"acefhlo"):
            count += 1
    print "The number of words that only contain acefhlo are:  " + str(count)
if __name__ == '__main__':
    main()
