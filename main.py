import os
import time
path = 'D:/CEStore/FN0S'
path1 = 'C:/Users/Administrator/Desktop/TEST'
count=0
b=0
set1=set()
File1=open('D:文件名称（去除后缀）.txt',mode='w')
File2=open('D:文件后缀.txt',mode='w')
File3=open('D:文件名称（带后缀）.txt',mode='w')
for root, dirs, files in os.walk(path):
   for m1 in files:
      count+=1
print('共计%s个文件' % count)
start = time.perf_counter()
for root, dirs, files in os.walk(path):
       for m1 in files:
          File1.write(os.path.splitext(m1)[0]+'\n')
          File3.write(m1 + '\n')
          b+=1
          print('已执行文件个数：%s' % b)
          print('进度:{:.0%} ' .format(b/count))
          set1.add(os.path.splitext(m1)[1])
for i in set1:
   File2.write( i.replace(".","")+',')
File1.close()
File2.close()
File3.close()
