#
# Generate a random password from file by concatinating 2 words
# filename provided as a command line parameter.
#
import sys
import random

# verify that exactly one command line parameter (in addition to the .py file) was provided
if len(sys.argv) != 2:
    print("Filename must be provided as a command line parameter.")
    quit()


try:
    filename = sys.argv[1]
    # open the file for reading
    f = open(filename,"r")
    words = f.read().split()
    while 1:
        # generate a random password
        word1 = random.choice(words).title()
        word2 = random.choice(words).title()
        password = word1 + word2
        # check password strength
        if len(word1) >= 3 and len(word2) >= 3 and 8 < len(password):
            # print out the generated password
            print(password)
            break
    # close the file
    f.close()
except:
    print("An error occurred while processing the file.")
    quit()
