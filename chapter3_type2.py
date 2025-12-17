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