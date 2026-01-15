# Module
# 함수,변수,클래스 등 파이선 모듈등을 모아놓은 파일
# 모듈이 모이면 패키지

# 해당 경로에 존재할 때 import 가능(리스트에 출력)
# 자세한 경로는 sys의 path를 확인하며 임의 추가시 sys.path.append로 임의 경로추가하면 가능
import sys
print('-'*10,"Before ")
for i in sys.path:
    print(i)
print('-'*10,"Before ")
sys.path.append("f:/book")
print('-'*10,"after ")
for i in sys.path:
    print(i)
print('-'*10,"after ")

import chapter5_func
# !!py파일을 모듈화 할 경우, 외부 호출 시 불필요한 출력 등 자체 호출과의 분할을 위해 아래와 같이사용
if __name__=="__main__":
    print("Local")
