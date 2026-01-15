# file
# r:read w:write, a:append, t:text mode, b:binary mode
# 상대경로 ../ ./
f=open('./resource/it_news.txt','r',encoding='UTF-8')
print(f.encoding)
print(f.mode)
print(f.name)
f.close()

# with문 !!! close 필요없음
with open('./resource/it_news.txt','rt',encoding='UTF-8') as ff:
    print(ff.read(20))
    print(ff.read(20))  # 커서 형태로 위치를 기억하므로 다음을 출력
    ff.seek(0,0)        # 0 위치로 이동
    print(ff.read(20))  # 최초부터 출력

# read(n Byte) : 전체 읽음
# readline : 한줄단위로 읽기
# readlines : ! 전체 읽음. 줄을 구분하여 리스트 형태로
with open('./resource/it_news.txt','rt', encoding='UTF-8') as f:
    for ln in f.readlines():
        print(ln)

# Write
# writelines : 리스트를 파일에 저장
with open('./resource/content0.txt','wt') as f:
    f.write('Hello World2\n')
# append
with open('./resource/content0.txt','at') as f:
    f.write('append line\n')
# write line
data1=['ab\n','bc\n','cd\n']
with open ('./resource/content1.txt','wt') as f:
    f.writelines(data1)

# csv
# read
import csv
with open('./resource/test2.csv','rt',encoding='UTF-8') as f:
    # print('__iter__' in dir(rs))  # iterable 형태
    rs=csv.reader(f,delimiter='|')
    # rs=csv.reader(f.readlines())
    # print(list(rs))

    # header 정보 스킵용도, 
    next(rs)
    for r in rs:
        print('-'.join(r))

with open ('./resource/test1.csv','rt',encoding='UTF-8') as f:
    rs=csv.DictReader(f)
    # rs=csv.DictReader(f.readlines())
    for i in rs:
        for k,v in i.items():
            print(k,v)
        print('-'*100)
# Write
data1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]
with open('./resource/write1.csv','w',encoding='utf-8',newline='') as f:
    wt=csv.writer(f)
    # print(dir(wt))
    for r in data1:
        wt.writerow(r) 
        print(r)

with open('./resource/write2.csv','wt',encoding='UTF-8',newline='') as f:
    header=['first','second','third']
    wt=csv.DictWriter(f,fieldnames=header)
    wt.writeheader()
    for r in data1:
        wt.writerow({header[0]:r[0],header[1]:r[1],header[2]:r[2]})