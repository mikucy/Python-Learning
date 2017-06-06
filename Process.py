# This code print the process number
import os

print('Process (%s) start... ' % os.getppid())

pid = os.fork()
if pid == 0:
  print('I am child process (%s) and my parent process is %s.' % (os.getpid(), os.getppid()))
else:
  print('I (%s) just created a child process (%s).' % (os.getppid(), os.getpid()))
