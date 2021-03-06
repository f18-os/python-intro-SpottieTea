#! /usr/bin/env python3
import sys        # command line arguments
import time
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

inputuser = "none"

while inputuser != "exit":
        oPrompt = "tell>"
        if 'PS1' in os.environ:
                oPrompt = os.environ['PS1']
                
        try:

                inputuser = input(oPrompt)
        except EOFError:
               sys.exit(1) 
         
        
        
        type(inputuser)

        check = inputuser.split()

        if 'cd' in check:
                os.chdir(check[1])
                continue

        pid = os.getpid()

        forker = os.fork()

        if forker < 0:

                sys.exit(1)

        elif forker == 0:                   # child
                
                args = inputuser.split()
                #& means background; THIS WORKS, TALK TO DAVID
                if '&' in args:
                        args.remove('&')
                elif '>' in args:
                        args.remove('>')
                        os.close(1)                 # redirect child's stdout
                        sys.stdout = open(args[2], "w")
                        os.set_inheritable(1, True)

                #if the path is given, we don't need to loop to find the program; set path instantly
                if '/' in args[0]:
                        program = args[0]
                        os.execve(program,args,os.environ)
                else:
                        for dir in re.split(":", os.environ['PATH']): # try each directory in the path
                                program = "%s/%s" % (dir, args[0])
                                try:
                                        os.execve(program, args, os.environ) # try to exec program
                                except FileNotFoundError:             # ...expected
                                        pass                              # ...fail quietly

                
                sys.exit(1)
        else:
                if '&' not in check: #if & isn't there, the shell should wait.
                        wait = os.wait()
                                
sys.exit(1)
