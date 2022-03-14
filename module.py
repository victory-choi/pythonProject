import theater_module
import theater_module as mv

theater_module.price(3) # 3명이서 영화볼떄
theater_module.price_mornig(4)
theater_module.price_soldier(5)

mv.price(1)

from theater_module import * # 모두 가져오기
price(3)

from theater_module import price, price_mornig # 일부만
price(2)
price_mornig()

