'''
신규여행사 프로젝트를 담당하게 되었을떄
태국 + 베트남 여행
'''

import travel.thailand # 클래스나 함수는 직접 임포트 금
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel import *
# import travel.vietnam
# 이렇게 하면 안된다. 왜냐? 개발자가 travel 이라는 것에서 공개범위를 설정해줘야한다.
# packgae 안에 포함된것에서 import 되길 원하는것만 공개를 하고 원하지 않는건 비공개로 할수있다.
# __all__ = ["vietnam"] 을 통해서 명시적으로 해줘야함. 따라서 thailand는 명시가 안되어있으니 당연히 thailand.ThailandPackge()는 안돼
trip_to = vietnam.VietnamPackage()
trip_to.detail()

'''
패키기, 모듈 위치 파악
현재작성중인 동일한 경로에 있었다. 근데 어느위치에 있는지 확인할방법을 모를때

'''


import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(vietnam))





