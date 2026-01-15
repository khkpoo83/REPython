# external func
# sys, pickle, shutil, temfile, time, random..

# sys
import sys
print(sys.argv) # arg 
#sys.exit() # 강제종료
print(sys.path) # 패키지 위치

# pickle
# 객체를 쓰는 용도
print('pickle','-'*100)
import pickle 
# pickle로 쓰기
file1=open('test.obj','wb')
data={1:'data1',2:'data2',3:'data3'}
pickle.dump(data,file1)
file1.close()
# pickle로 읽기
file2=open('test.obj','rb')
# print(pickle.load(file2))
data2=pickle.load(file2)
print(data2)
file2.close()

# os
# mkdir, rmdir, rename 환경변수 디렉토리 및 파일 처리
import os
for i in os.environ:
    print(i,':',os.environ[i])
print(os.getcwd())

# time
import time
# 시간 표현
print(time.time())
print(time.ctime())
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# sleep 용도
# time.sleep(1)

# random
import random
# 0~1사이 임의값
print(random.random())
print(random.randint(1,46))
print(random.randrange(1,46))
# 섞기 (shuffle)
data1=[1,2,3,4,5]
for i in range(0,10):
    random.shuffle(data1)
    print(data1)
# 뽑기 (choice)
data1.sort()
for i in range(0,10):
    print(random.choice(data1))

# webbrowser
import webbrowser as wb
wb.open(url='https://naver.com')