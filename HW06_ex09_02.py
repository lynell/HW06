#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports
def has_no_e(line):
    if "e" in line:
        return False
    else:
        return True

def percentage():
#I have used the words.txt file provided for HW05
    count = 0
    total = 0
    fin = open("words.txt","r")
    for line in fin:
        total = total + 1
        if "e" not in line:
            count = count + 1
            #print line
    print count
    print total
    print str((count/float(total))*100) + "%"

    
# Body


##############################################################################
def main():
    pass  # Call your function(s) here.
##    word = raw_input("Enter a word")
##    has_no_e(word)
    percentage()
if __name__ == '__main__':
    main()
