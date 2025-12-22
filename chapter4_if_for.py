# if 기본 문법
a=100
b=20
if (a>b):
    print(a)
elif (b>a):
    print(b)
else:
    print(c)
#* 논리 연산자 and or not    
# 산술 > 관계 > 논리 순으로 수행
print(3+5>2+1)
print(3+5>3 and not 9+1==10)

# for : 기본 흐름
for i in range(1,10):   # for in <collection>
    print(i)
# iterables(문자,튜플,리스트,사전,집합) 은 for 사용가능
for i in "abcd":
    print(f'{i}')
d1=dict(
    name='khkpoo',
    year=20
)
# dictionary는 key만가져옴
for i in d1:
    print(i,d1[i])

# for : break와 continue
# break : 특정 값 만족 시 반복 종료
import random
a=[]
for i in range(0,100):
    a.append(int(random.random()*1000))
print(a)   
cnt=0 
for i in a:
    cnt+=1
    if i==34:
        print('-'*100)
        print(f'{cnt}th found')
        print('-'*100)
        break
# for-else 구문, break에 의해 조기 종료되지 않은 경우 else 구문 사용됨. break로 조기종료 시 else 구문 사용 안됨
else:
    print('Not found')
# continue : 특정 값 만족 시 스킵(무시)   
tmp=[]
for i in a:
    if i==34:
        continue
    tmp.append(i)
print(tmp)    
# reversed 함수
str="무바바보"
print(reversed(str))
print(list(reversed(str)),set(reversed(str)))