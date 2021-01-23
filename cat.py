#
# CAT a file/files (display content of a file/files)
#
import sys


# Verify that exactly one command line parameter
if len(sys.argv) != 2:
    print("comma seperated filename/s must be provided as a command line parameter.")
    print("ex of usage: cat.py test.txt,toto.txt")
    quit()


filenames = sys.argv[1].split(",")
for file in filenames:
    try:
        f = open(file,"r")
        text = f.read()
        print(text)
        f.close()
    except:
        print("An error occurred while processing the file: {}".format(file))
        quit()    
