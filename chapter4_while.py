# while
t1=[1,2,3,4,5]
# while t1:       # for 문처럼 요소의 반복이 아니므로 이런식의 사용은 XXX
#     print(t1)
while True:
    if not t1:
        break
    
while t1:
    print(t1.pop())
print(t1)    