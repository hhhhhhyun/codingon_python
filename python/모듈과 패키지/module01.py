#모듈 만들고 불러오기 방법1
import calc_module #컨트롤 누르고 클릭하기
print()

#모듈 불러오기 방법2
print(calc_module.add(1,2))
print(calc_module.sub(1,2))
print(calc_module.mul(1,2))
print(calc_module.div(1,2))
#calc_module.add() 안됨
print()

#모듈 불러오기 방법3
import calc_module as cm #이름을 cm으로 줄인 것
print(cm.add(1,2))
print()

#표준 모듈 - math 모듈
#sprt(n) : = 루트

import math #컨트롤 누르고 클릭하면 보임

from math import floor, ceil
print(math.floor(3.141592)) # 내림: 3, 컨트롤 누르고 floor클릭해보기
print(math.ceil(3.141592)) # 올림: 4, 컨트롤 누르고 ceil 클릭해보기
