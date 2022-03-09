'''사이트별로 비밀번호를 만들어주는 프로그램을 작성하세요
ex)http://naver.com
규칙1 : http://부분은 제외해라
규칙2 : 처음 만나는 점(.) 이후 부분은 제외해라
규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 e갯수 + !로 구성해라
'''


site = "http://naver.com"
my_str = site.replace("http://", "") # 규칙1
my_str = my_str[:5] # 규칙2
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(pw)



'''
당신의 학교에서는 파이썬 코딩대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했어요
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됩니다.
추첨 프로그램을 작성하세요

1. 편의상 댓글은 20명작성하고 아이디도 1~20으로 고정한다.
2. 댓글 내용과 상관없이 무작위 추첨하되 중복이 불가능하다
3. random 모듈의 shuffle과 sample을 활용한다.
# first = [1,2,3,4,5]
# print(first)
# shuffle(first)
# print(first)
# print(sample(first, 1))
'''

from random import *

comment = range(1, 21)
# print(type(comment)) range 함수임을 확인
comment = list(comment) # range -> list 함수로 변경해주고
shuffle(comment) # 섞어
print(comment) # 프린트해 사실 프린트는 필요없을것 같긴한데

'''
id = range(1, 20)
# print(type(id)) range 함수임을 확인
id = list(id) # # range -> list 함수로 변경해주고
shuffle(id) # 섞어
print(id) # 프린트해 사실 프린트는 필요없을것 같긴한데
생각해보니, 코멘트를 단사람 = id 갯수이기 때문에 이건 의미가 없지.
'''

winners = sample(comment,4)
# 변수지정을 해주자 어떻게?
# winners에다가 sample로 지정해주는데, comment 단 사람들의 id를 랜덤으로 샘플링하되 4개를 list함수로
print(winners)


# print("-- 당첨자 발표 -- \n 치킨 당첨자 : , \n 커피 당첨자 : , \n -- 축하합니다 --")
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {} ".format(winners[0]))
print("커피 당첨자 : {} ".format(winners[1:4]))
print("-- 축하합니다 --")


'''
퀴즈
당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있으 때 , 총 탑승 승객 수를 구하는 프로그램을 작성하세요

1. 승객별 은행 소요시간은 5~50분사이의 난수
2. 당신은 소요시간 5~ 15분사이의 승객만 매칭해야됨.
'''

from random import *

cnt = 0 # 총 탑승승객수
for i in range(1,51):
    time = randrange(5, 51)# 5분 ~ 50분 소요시간
    if 5<= time < 16: # # 5분 ~ 15분손님 이니 탑승 승객수 증가
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else:
        print("[X] {0}번째 손님 (소요시간 : {1}분".format(i, time))

print("총 탑승 승객 {}분".format(cnt))


'''
표준 체중을 구하는 프로그램을 작성하세요

* 표준체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

1. 표준 체중은 별도의 함수내에서 계산한다.
* 함수명 : std_weight
* 전달값 : 키(height), 성별(gender)

2. 표준체중은 소수점 둘째자리까지 표시한다.

출력예
키 175cm 남자의 표준체중은 67.38kg 입니다.

'''

def std_weight(height, gender): # 키는 m단위(실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height /100 , gender),2) # round를 통해서 소수점 2번째까지 노출해줘
print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height, gender, weight))



'''
당신은 회사에서 매주 1회 작성해야하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 - 
부서 : 
이름 : 
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하세요

1. 파일명은 '1주차.txt', '2주차.txt', ...... 와 같이 만듭니다. 

'''

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 :")



