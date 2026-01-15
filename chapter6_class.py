# class
# 암기
class Animal:
    # Class 속성(변수) !!공유목적
    category='Dog'
    # 초기화 !!개별목적, 옵션임
    def __init__(self,*kwarg):
        self.name=kwarg[0]
        self.year=kwarg[1]
        print('Created')
    # 소멸자, 옵션
    def __del__(self):
        print('deleted')
a=Animal('ab',18)
print(a.name,a.year)

# 클래스 변수는 직접 접근 가능(Class명으로)
# 반면 Instance 변수(Self) 는 객체를 통한 접근만 가능
# print(Animal.category,Animal.name)  # X
print(a.category,a.name)            # O
print('{} is {}'.format(a.name,a.year))
print(f'{a.name} is {a.year}')

# self의 이해
# self란 객체 그자체(인스턴스변수)로 암묵적으로 사용됨
# self가 존재하면 인스턴스 변수,함수
class Self1:
    # class 메소드
    def func1():
        print('no self')
    def func2(self):
        print('self')
a=Self1()
# a.func1() # X class 메소드. 변수와 마찬가지로 self가없어서 class로만 접근가능
a.func2()
Self1.func1()
Self1.func2(a)  # 명시적으로 객체넣어줘서 호출 가능

