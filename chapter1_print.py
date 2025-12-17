# print Usage
# 1. seperator, end
print('hello')
print('h','e','l','l','o',sep='_')
print('h','e','l','l','o',sep='',end='!')

# 2. format
print( '%s,%d,%f' % ('one',2,3.0))
print('%10s'%('one')[0:])
print('{0},{2},{1}'.format('one',3.0,2))
print('{:1.3f}'.format(3.141592))
print('{var1}'.format(var1='test'))

# 3. fstring
v1='test'
print('var1={v1}')          # v1 문자로 인식
print('var1=',v1,sep='')    # 결과 동일
print(f'var1={v1}')

# 숫자 구분자
a=100000000
print(f'a={a:,}')

# ^가운데정렬
# <왼쪽정렬
# >오른쪽정렬
b=1
print(f'b={b:A^10}')
print(f'b={b:B<10}')
print(f'b={b:C>10}')