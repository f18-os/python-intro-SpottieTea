import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

# set input and output files
if len(sys.argv) is not 3:

        print("Correct usage: wordCount.py <input text file> <output file>")

        exit()
            
inputFname = sys.argv[1]
outputFname = sys.argv[2]

#check for files
if not os.path.exists(inputFname):

        print ("text file input %s doesn't exist! Exiting" % inputFname)

        exit()

#dictionaries
master = {}

#open input file
with open(inputFname, 'r') as inputFile:
        for line in inputFile:
                #clear newline characters
                line = line.strip()
                #get each word on file
                for word in line.split():
                        if word not in master:
                                master.append(word)
