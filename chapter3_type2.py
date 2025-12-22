# list []
# 순서가있음
# 중복, 수정, 삭제 가능
a=[]        # 선언방법 두가지
a=list()
b=[100,200,3000,'strt']
print(b[0:2])

# 주요함수
b=[5,2,3,1,4,5]
b.sort()    # 정렬
print(b)
b.reverse() # 역정렬
print(b)
print(b.index(1))   # 값이 존재하는 위치 확인
b.append(5)     # 마지막 위치 값 추가
b.insert(6,10)  # 특정 위치 값 추가
print(b)
del b[5]    # 삭제
b.remove(10)    # 삭제
print(b)    
print(b.pop())     # 마지막 값 꺼냄

# tuple ()
# 순서가있음
# 중복허용
# 수정 및 삭제는 안됨 (list와 다른 점)
c=('1',2,(3,4))
c1=1,2,3            # 튜플은 () 생략 가능
c2=1,               # ,인 경우 튜플로 인식
print(c1,type(c1))
print(c2,type(c2))
print(c.count('1'))   # 매칭되는 개수 반환
print(c.index(2))       # 매칭되는 위치(*첫) 반환
# *패킹과 언패킹
# 패킹
d1=('a','b','c','d')
# 언패킹
(x1,x2,x3,x4)=d1
print((x1,type(x1)))

# *dict {}
# 순서가 없음
# 키의 중복허용안함
# 수정 및 삭제 허용
e={'a':1,1:'b'}
e1={
    'Name':'Kangnam',
    'Age':5
}
e2=dict(
    name='abc',
    year=5
)
print(e['a'],e[1])
print(e1['Age'],e1['Name'])
print(e2['name'])
# 주요 함수 keys,values,items
# pop, popitem
# in, not in
print(e1.get('Name'))   # key값 미존재시 에러가 아닌 None으로 나와서 안정적임
print(e1.keys(),e1.values(),e1.items())
print('5' in e1)                            # key 값 기준으로 값이 존재하는지 체크

# sets
# 순서가 없음
# 중복 허용 안함
# 추가 및 삭제 가능
# 선언시 set + [] 사용하거나 {} 사용
a=set()
a=set([1,2,3,3])
b={1,2,3,3}
print(a,b,type(a),type(b),len(a))
# 주요함수
# 교집합 intersection(&)
# 합집합 union (|)
# 차집합 difference(-)
# 교집합 여부 isdisjoint *dis가 붙으므로 false가 나오면 교집합이 존재함을의미
# 부분집합 여부 issubset <> issuperset
a={1,2,3,4,5}
b={3,4,5,6,7}
print(a.intersection(b),a|b,b.difference(a))
print(a.isdisjoint(b),a.issubset(b),a.issuperset(b))
