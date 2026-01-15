# exception
# 에러가 아닌 예외

# 종류
# SyntaxError, TypeError, NameError, IndexError, KeyError, ValueError, ZeroDivisionError ...

# 패턴
# 1. try: - 에러가 발생 할 가능성이 있는 코드
# 2. excpet 에러명: -발생시 수행코드, 여러개 가능
# 3. else: - try구문에서 에러 미발생시
# 4. finally: - 항상 실행

import random
a=[]
for i in range(10000):
    if int(random.random()*1000) == i:
        a.append('err')
    else:
        a.append(int(random.random()*1000))
try:
    for i,v in enumerate(a):
        print(i,':',v+1)
except TypeError:
    print(i,'!!', v)
else:
    print('No Exception')
finally:
    print('End')

# 아래와 같치 처리 가능
# except Exception as e:
#     print(e)

# raise