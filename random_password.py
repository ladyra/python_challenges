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
    # generate a random password
    password = random.choice(words) + random.choice(words)
    # close the file
    f.close()
except:
    print("An error occurred while processing the file.")
    quit()

# print out the generated password
print(password)
