import subprocess as sp
import re
import time
from datetime import datetime, timedelta
from random import randint

def genRandomTime():
    hour = random.randint(0, 24)
    minute = random.randint(0, 60)
    second = random.randint(0, 60)
    return hour, minute, second

ls = sp.run("dir", shell = True, capture_output = True)
filelist = re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}  [0-9]{2}:[0-9]{2} .*? [0-9]+ (\S*)', ls.stdout.decode())
daydelta = 1

while 1:
    pickUpFrom = datetime(2020, 12, 5, genRandomTime())
    ls = sp.run("dir", shell = True, capture_output = True)
    newlist = re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}  [0-9]{2}:[0-9]{2} .*? [0-9]+ (\S*)', ls.stdout.decode())
    if newlist != filelist:
        sp.run('git add .', shell = True)
        sp.run(f'git commit --date "{str(pickUpFrom + timedelta(daydelta))}"  -m {str(list(set(newlist) - set(filelist)))}')
        sp.run('git push')
        print(f'Added, committed, and pushed file {str(list(set(newlist) - set(filelist)))} with commit datetime {str(pickUpFrom + timedelta(daydelta))}')
        daydelta += 1
    filelist = newlist
    time.sleep(7)


