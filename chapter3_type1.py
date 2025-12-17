# python 주요 자료형
# int : 정수
# float : 실수
# complex : 복소수
# bool : 불린 
# str : 문자열 (시퀀스)
# tuple : 튜플 (시퀀스) ()
# list : 리스트 (시퀀스) []
# set : 집합 {}
# dict : 사전 {}
#------------------------------------------------------------
# 숫자형 주요 함수
# // 몫
# % 나머지
# abs(x) 절대값
# pow(x,y) 제곱,x**y
# a,b=divmod(x,y) 몫과 나머지
# ceil 등 숫자 함수는 math 모듈 참고

# 숫자형 형변환
# int와 float 연산 시 float (int가 float으로 자동형변환)
#------------------------------------------------------------
# Escape 및 특수문자, Raw String
escape='i\'m a boy'
print(escape)
raw_str=r'd:\games'
print(raw_str)

# 멀티라인, 줄바꿈 시 역슬래시(\)사용
multi_str=\
'''
abc 
    rdf
'''
print(multi_str)

# 문자열 연산 **자주쓰임
str1='abc'
str2='def'
print(str1*3)
print(str1+str2)
print('bc' in str1)
print('A' not in str1)

# 문자형 주요 함수
# sorted, split, replace
print(str1.capitalize())    # 첫 글자 대문자
print(str1.endswith('c'))   # 마지막 문자 확인
print(str1.replace('b','Z'))    # 변경 후 저장하진 않음
print(sorted(str1,reverse=True))
print(escape.split(' '))

# 문자형 슬라이싱
src="abc def"
print(src[0:2]) # 두번째 숫자는 개수가 아님 (미만)
print(src[4:])
print(src[::2]) # 세번째 인자는 건너띄기 단위
print(src[-3:]) # 마지막 배열번호는 -1
print(src[-1::-1])

# 아스키
print(ord('z'))
print(chr(122))



#------------------------------------------------------------