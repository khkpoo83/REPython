# Variables
# 선언
a=100
b=c=d=200   # 동시선언

# 변수의 할당과 메모리 포인터
# 같은 값일 경우 동일 메모리를 참조하며, 값 변경 시 메모리 위치 변경
a1=100
b1=a1
print(f'a1={a1} | {id(a1)}{'\n'}b1={b1} | {id(b1)}{'\n'}Result={id(a1)== id(b1)}{'\n'}')
a1=200
print(f'a1={a1} | {id(a1)}{'\n'}b1={b1} | {id(b1)}{'\n'}Result={id(a1)== id(b1)}')

# 변수선언 대소문자 규칙
# numberOfCollege : Method (카멜)
# NumberOfCollege : class (파스칼)
# number_of_college : Variable (스네이크)