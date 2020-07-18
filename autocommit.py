import subprocess
import os
import sys
import re
import time
from datetime import datetime, timedelta

ls = subprocess.run("dir", shell = True, capture_output = True)
filelist = re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}  [0-9]{2}:[0-9]{2} .*? [0-9]+ (\S*)', ls.stdout.decode())
daydelta = 1

while 1:
    ls = subprocess.run("dir", shell = True, capture_output = True)
    newlist = re.findall(r'[0-9]{2}/[0-9]{2}/[0-9]{4}  [0-9]{2}:[0-9]{2} .*? [0-9]+ (\S*)', ls.stdout.decode())
    if newlist != filelist:
        subprocess.run('git add .', shell = True)
        subprocess.run(f'git commit --date "{str(datetime.now() + timedelta(daydelta))}"  -m {str(list(set(newlist) - set(filelist)))}')
        print(f'Added and committed file {str(list(set(newlist) - set(filelist)))} with commit datetime {str(datetime.now() + timedelta(daydelta))}')
        daydelta += 1
    filelist = newlist
    time.sleep(10)


