import sys        # command line arguments
import time
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program



inputuser = raw_input("Hello! Please provide two file names. \n")

print("Accepted names %s!" % inputuser)

inputuser = inputuser.split( )

print("Seperating files...")

ufile1 = inputuser[0]
ufile2 = inputuser[1]

print("Successfully seperated %s and %s!" % (ufile1, ufile2))

pid = os.getpid()


forker = os.fork()

if forker < 0:

        os.write(2, ("fork failed, returning %d\n" % forker).encode())
        sys.exit(1)

elif forker == 0:                   # child

        os.write(1, ("I am child.  Name==%s  Parent's pid=%d\n" % (ufile2, pid)).encode())

else:                           # parent (forked ok)

        os.write(1, ("I am parent.  Name=%s  Child's pid=%d\n" % (ufile1, forker)).encode())
