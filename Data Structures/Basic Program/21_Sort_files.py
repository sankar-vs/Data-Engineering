'''
@Author: Sankar
@Date: 2021-04-08 08:10:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 08:30:09
@Title : Basic_Python-21
'''
'''
Write a Python program to sort files by date.
'''
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

# regular files, insert creation date
data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))