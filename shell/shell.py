import sys        # command line arguments
import time
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program


#enter in bash in format: python3 shell.py [ufile1] [ufile2]

ufile1 = sys.argv[1]
ufile2 = sys.argv[2]

print(ufile1)
print(ufile2)


pid = os.getpid()


forker = os.fork()

if forker < 0:

        os.write(2, ("fork failed, returning %d\n" % forker).encode())
        sys.exit(1)

elif forker == 0:                   # child

        os.write(1, ("I am child.  Name==%s  Parent's pid=%d\n" % (ufile2, pid)).encode())

else:                           # parent (forked ok)

        os.write(1, ("I am parent.  Name=%s  Child's pid=%d\n" % (ufile1, forker)).encode())
