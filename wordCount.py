import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

# set input and output files
if len(sys.argv) is not 3:

        print("Correct usage: wordCount.py <input text file> <output file>")

            exit()
            
outputFname = sys.argv[1]
inputFname = sys.argv[2]

#check for files
if not os.path.exists(inputFname):

        print ("text file input %s doesn't exist! Exiting" % textFname)

            exit()
