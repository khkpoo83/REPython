# func : def, 정의 후 필요시 호출, 재사용
# 종류
# 1. 매개변수 필요없음
# 2. 매개변수 필요
# 3. 결과값 반환없음
# 4. 결과값 반환
# -----------------------------------
# 1. 매개변수 필요없음 + 3. 결과값 반환없음
def funcNoArg():
    print('Function 1 :')
funcNoArg()    
# 2. 매개변수 필요 + 3. 결과값 반환없음
def funcArg(a,b):
    print('function 2 :',a,b)
funcArg(10,'arg2')    
# 4. 결과값 반환
def funcArgReturn(a,b):
    if type(a) is int and type(b) is int:
        return(a+b)
    else :
        return("No")
print(funcArgReturn(1,2))
print(funcArgReturn('a','b'))

#* *args, **kwargs
# *args : 매개변수의 개수가 미정인 경우, 변수들을 "튜플형태"로 묶어서 보내고 받는다. 받는입장(펑션)에서는 위치(index)기반 언팩킹해서 사용
def arg_func1(*args):
    print(type(args))
    for k,v in enumerate(args):
        print(k,v)   
arg_func1('a',1,'b',2,(1,2,3))   
# **kwargs : "딕셔너리 형태"로 매개변수를 보내고 받는다. 호출 시 명시적으로 이름을 적어줌. 받는입장(펑션)에서는 인자명 기반 언팩킹해서 사용
def arg_func2(**kwargs):
    print(type(kwargs))
    for k in kwargs:
        print(k, kwargs[k])
arg_func2(a=1,b=2,c='c')

# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print('in func')
    func_in_func(num+100)
nested_func(100)    

#* lambda 메모리절약, 가독성 향상, 코드간결..
def func1(x,y):
    return x*y
func_name=func1
print(func_name(2,4))
# 동일 표현
a=lambda x,y:x*y
print(a(2,4))
# 함수를 인자로 할 떄
def func_final(a,b,func1):
    return (a+b+func1(1,2,4))
print(func_final(10,5,lambda x,y,z:x*y/z))
