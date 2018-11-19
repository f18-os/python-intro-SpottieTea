#! /usr/bin/env python3
import sys        # command line arguments
import time
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

inputuser = "none none"

while inputuser != "exit":

        inputuser = input("$> ")
        type(inputuser)

        pid = os.getpid()

        forker = os.fork()

        if forker < 0:

                sys.exit(1)

        elif forker == 0:                   # child
                
                args = inputuser.split()

                for dir in re.split(":", os.environ['PATH']): # try each directory in the path
                        program = "%s/%s" % (dir, args[0])
                        try:
                                os.execve(program, args, os.environ) # try to exec program
                        except FileNotFoundError:             # ...expected
                                pass                              # ...fail quietly

                
                sys.exit(1)
        else:
                wait = os.wait()
                                
sys.exit(1)
