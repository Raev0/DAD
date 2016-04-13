
import os
import sys
import datetime
import time

i=datetime.datetime.now()
year='%d' %i.year
month='%d' %i.month
day='%d' %i.day



#root=r'D:\WP\CE\'

foldername=year+'_'+month+'_'+day
### find the day above and plus 1 as foldername(no more)


### generate the folder (check if exits)


if os.path.exists(foldername):
    print(foldername+' is exited')
else:
    os.mkdir(foldername)

    
##indication
print('today is '+foldername)
#print(root)


print(os.getcwd()+'\\'+foldername)
os.system('explorer.exe %s' %os.getcwd()+'\\'+foldername)

#os.system('pause')

for i in range(1,3):
    time.sleep(5)

#os.system("pause")
#Exit()

os._exit()
