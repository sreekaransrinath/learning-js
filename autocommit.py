import subprocess as sp
import os
import sys
import re
import time
from datetime import datetime, timedelta

ls = sp.run("dir", shell = True, capture_output = True)
filelist = re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}  [0-9]{2}:[0-9]{2} .*? [0-9]+ (\S*)', ls.stdout.decode())
daydelta = 1

while 1:
    ls = sp.run("dir", shell = True, capture_output = True)
    newlist = re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}  [0-9]{2}:[0-9]{2} .*? [0-9]+ (\S*)', ls.stdout.decode())
    if newlist != filelist:
        sp.run('git add .', shell = True)
        sp.run(f'git commit --date "{str(datetime(2020, 8, 23, 13, 9, 18, 442081) + timedelta(daydelta))}"  -m {str(list(set(newlist) - set(filelist)))}')
        sp.run('git push')
        print(f'Added, committed, and pushed file {str(list(set(newlist) - set(filelist)))} with commit datetime {str(datetime.now() + timedelta(daydelta))}')
        daydelta += 1
    filelist = newlist
    time.sleep(1)


