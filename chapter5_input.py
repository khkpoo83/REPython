# input
# 입력받은 값은 str유형임을 주의 (숫자 입력받을 시)
# a=input("Input Text >>\n")
# print(a*10)
# 무한 입력
while True:
    rst=input('Catch me : ')
    if rst== '123':
        break
# 예외처리
try:
    a=int(input('integer : '))
    print('result : {}'.format(a))
except ValueError:
    print("Err")