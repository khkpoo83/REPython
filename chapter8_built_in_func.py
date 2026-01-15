# Built-in Func
print(abs(-3))  # 절대값

# 요소의 참 값을 검사 : all, any
print(all((1,2,3)))
print(all([1,2,3,'']))      # False
print(all([1,2,3,False]))   # False
print(any([1,2,3,False]))   # True

# 아스키 문자 변환 : chr, ord
print(chr(70))
print(ord('F'))

# !enumulate : index+iterable한 객체 생성
for i, name in enumerate(['first','second']):
    print(i,name)

# !filter : 반복가능한 객체 요소(iterable)를 지정한 함수 조건에 맞는 값 추출 
# !!단 참/거짓을 평가할수있어야함
def test(a):
    return a>0

def test_int(a):
    if abs(a)>0:
        return a
    else:
        return 0
print(list(filter(test,[0,1,-1]))) # [1]
print(list(filter(test_int,[0,1,-1]))) # [1,-1]
# !lambda로 표현 (lambda if 문 문법확인)
print(list(filter(lambda x:x>0,[0,1,-1])))
print(list(filter(lambda x:x if abs(x)>0 else 0,[0,1,-1])))

# !map : 반복가능한 객체 요소(iterable)를 지정한 함수 실행 후 결과 추출
# !!filter와 달리 참/거짓 여부를 판단 후 거르지 않고 결과만을 반환
def test_int2(a):
    if abs(a)>0:
        return a
    else:
        return False
print(list(map(test_int2,[0,1,-1]))) # [1,-1]

# id : 객체의 주소
# len : 요소의 길이
# type : 타입 확인
# zip : iterable의 요소를 묶어서반환, 짝이 없으면 누락됨
print(list(zip([6,-1,3,5,0,2],[1,2,3],[2,3,4,5])))
# max, min
a="PythonStudy"
print(min(a),max(a))
# pow : 제곱 **
# range : 반복 가능한 객체반환
# round : qksdhffla
# !sorted : iterable을 정렬 후 반환
print(sorted([6,-1,3,5,0,2],reverse=True))
# sum : iterable을 합
