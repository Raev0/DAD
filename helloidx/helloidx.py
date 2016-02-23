import os
import win32ui

CUR_DIR=os.path.dirname(os.path.abspath(__file__))

dlg = win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir(CUR_DIR)
dlg.DoModal()
FILENAME = dlg.GetFileName()
DESTNAME=FILENAME[:-4]+'_new.txt'
objnames=[]
fs=open(FILENAME,'r')

for line in fs.readlines():
    objnames.append(line.lstrip())

objnames.sort()
print(objnames)

fs2=open(DESTNAME,'wb')
fs2.writelines(objnames)

