# Package
# Module을 모아 둔 폴더와 같은개념
# 그림과 같이 패키지(폴더) > 패키지(폴더) > 모듈(파일) 로구성된 경우 예제
import package1.subpackage1.module1
import package1.subpackage2.module2

package1.subpackage1.module1.mod1_func1()
package1.subpackage1.module1.mod1_func2()
package1.subpackage2.module2.mod2_func1()
package1.subpackage2.module2.mod2_func2()
print('-'*50)

# 너무 길기 때문에!
from package1.subpackage1 import module1 
from package1.subpackage2 import module2 as md

module1.mod1_func1()
md.mod2_func2()
print('-'*50)

# 특정 모듈이 아니라 전체 가져올 때 * 사용 가능
# 단 이 경우 패키지 내 __init__ 파일 만들고 외부 접근 가능한 모듈명을 적어줘야함
#  패키지 내 모듈 명 나열. (__init__.py) >> __all__=['module1']
from package1.subpackage1 import *
module1.mod1_func1()