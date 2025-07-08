import os 
import sys
import time
i = 0
while i<=50 :

    bar = "█" * i 
    percent = (i)*2
    
    sys.stdout.write (f"\r{bar} {percent}%")
    i+=1
    time.sleep(.1)