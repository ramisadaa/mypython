
import os
import time
import sys

os.system ('cls')
i = 0 
while i<=30 :
    i+=1
    bar = "█" * i + " " * (30 - i)
    #sys.stdout.write(f"\r[{bar}] ")
    sys.stdout.write (f"\r{bar}")
    time.sleep(.2)
