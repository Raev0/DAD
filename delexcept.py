import os
from shutil import rmtree
from time import sleep

SUFIX_NOT_DEL= '.stl'
presentpath=os.path.dirname(os.path.abspath(__file__));

print (presentpath)


for root,subfolders,files in os.walk(presentpath):
    for file in files:
        if os.path.splitext(file)[1] != SUFIX_NOT_DEL and os.path.basename(file)!=os.path.basename(__file__):
            os.remove(file)

    for subfolder in subfolders:
        rmtree(subfolder)

