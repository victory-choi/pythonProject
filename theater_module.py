'''
자동차를 이용하다가 타이어나 범퍼만 고장나면 타이어나 범퍼만 교체하면 되겠지?

'''
# 일반 가격정보

def price(people):
    print("{0} 명 가격은 {1} 원 입니다.".format(people, people*10000))

def price_mornig(people):
    print("{0} 명 조조할인된 가격은 {1} 원 입니다.".format(people, people*6000))

def price_soldier(people):
    print("{0} 명 군인할인된 가격은 {1} 원 입니다.".format(people, people * 4000))