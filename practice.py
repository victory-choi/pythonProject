#랜덤함수

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # int로 감싸면 정수만

print(randrange(1,46)) # 1~ 46미만의 임의의값 생성

day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(day) + "로 선정되었습니다.")
# 여기서 str로 해야하는 이유는 print문내부에 쓰기위해서는 string으로 변경해야하니까!

#슬라이싱

jumin = "999301-1234567"
print("성별 : " + jumin[7])
print("년 : " + jumin[0:2]) #0번째부터 2직전까지가져와라
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지!
print("뒤 7자리 (뒤에서부터): " + jumin[-7:]) # 맨뒤첫자리가 -1임


#문자열 처리
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 파이썬있는 첫번째 값이 맞냐 확인
print(len(python)) # 파이썬 전체의 문자열 길이를 반환해줌
print(python.replace("Python" , "java")) # 원하는 문자 변환

index = python.index("n") # n 이라는 글자가 몇번째에 있는지
print(index)
index = python.index("n" , index + 1) # 앞에서 찾은 위치 다음부터 즉 6번째 위치부터 찾아라
print(index)

print(python.find("n")) #find 해서 자바를 찾으면 ? 변수에 포함되지 않는 경우는 -1
#print(python.index("java")) #index는 프로그램 종료
print(python.count("n")) # 몇번 동작하냐

# 문자열 포맷콤마를 이용하는 방법말고도 다양한 방법1
print("나는 %d 살입니다" % 20)
print(("나는 %s 를 좋아해요" % "파이썬")) # %s는 문자열(string)
print(("Apple 은 %c 로 시작해요" %"A")) # %c는 한글자만 (char)]
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간")) # 값을 두개를 넣고싶을떄? 괄호안에 넣고 순서대로

# 문자열 포맷콤마를 이용하는 방법말고도 다양한 방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간")) # 순서의 도치도 가능함.

# 문자열 포맷콤마를 이용하는 방법말고도 다양한 방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간")) # 중괄호속의 값을 포맷뒤에서 선언해도 가져다 쓸수있다.

# 문자열 포맷콤마를 이용하는 방법말고도 다양한 방법4(python 3.6이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출문자 (\n)
print("백문이 불여일견 \n백견이 불여일타")
# 저는 "나도코딩" 입니다 하고싶을떄?
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.") # 역슬래쉬 넣어서 문장내 따옴표 가능

# 탈출문자 (\r) 커서를 맨앞으로 이동
print("Red Apple \r Pine") #PineApple로 찍힘. \r의 후단을 맨앞으로 이동해서 Red를 대체함
# 탈출문자 (\b) 한개지우기
print("Redd \b Apple")
# 탈출문자 (\t) tab해서 띄워줌
print("Red\tApple")

# 리스트
# 지하철타는데 칸별로 10명, 20명 30명 가정
# subway1 = 10
# subway2 = 20
# subway3 = 30
subway = [10, 20, 30] # 리스트를 사용해서 비슷한걸 하나로 묶어준다.
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)

#활용 : 조세호가 몇번쨰칸에 타고있냐
print(subway.index("조세호")) # index 1번째 위치한다 나옴.
subway.append("하하") #맨뒤에 넣어줬네
print(subway)
# 정형돈을 유재석 / 조세호 사이에 넣어주기
subway.insert(1, "정형돈")
print(subway)
# 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
# 같은이름의 사람이 몇명있는지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
# 정렬도 가능
numbers_list = [1,5,7,8,1]
numbers_list.sort()
print(numbers_list)
# 뒤집기
numbers_list.reverse()
print(numbers_list)
# 지우기
numbers_list.clear()
print(numbers_list)

# 다양한 자료형 함께 사용
numbers_list = [1,23,4,5]
mix_list = ["조세호", 1, True]
print(mix_list)

numbers_list.extend(mix_list) # 합치기
print(numbers_list)

'''사전 단어에 대한 정의
'''

cabinet = {3:"유재석", 100 : "김태호"}
print(cabinet[3]) # 키값을 출력해주기
print(cabinet.get(3)) # 키값을 출력해주기
# print(cabinet[5]) # 대괄호는 프로그램종료
print(cabinet.get(5)) # get은 none 값 출력 후 계속 진행

print(3 in cabinet) # True
print(5 in cabinet) # False

# 값 업데이트
cabinet2= {"a-3":"유재석", "e-100" : "김태호"}
print(cabinet2["a-3"])
cabinet["a-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

# 값 지우기
del cabinet[3]
print(cabinet)

# key 값들만 출력
print(cabinet.keys())

# value 만 출력
print(cabinet.values())

# key, value 쌍으로 출력 = items
print(cabinet.items())

# 싹지우기
cabinet.clear()
print(cabinet)





'''
튜플은 리스트와다르게 내용변경이나 추가를 할수는 없으나 속도가 리스트보다 빠름
변경되지 않는것들을 다룰때 사용함.
'''

menu = ("돈까스", "치돈")
print(menu[0])

name = "김종국"
age = 20
hobby = "코딩"

print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)



'''
세트 = 집합
중복이 안되고 순서가 없어
'''

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 출력(자바와 파이썬모두할수있는 개발자 출력해라)
print(java & python)
print(java.intersection(python))

# 합집합 출력 (자바 and 파이썬)
print(java | python)
print(java.union(python))

# 차집합 출력
print(java - python)
print(java.difference(python))

# 파이썬 할줄아는사람 늘어남
python.add("김태호")
print(python)

# 자바를 까먹었어요

java.remove("김태호")
print(java)


'''
자료구조의 변경
'''

menu = {"커피", "우유", "주스"}
print(menu)
print(menu, type(menu))

menu = list(menu) # 메뉴를 리스트로 감싸면 자료구조가 변경됨 (set -> list)
print(menu, type(menu))

menu = tuple(menu) # 메뉴를 리스트로 감싸면 자료구조가 변경됨 (list -> tuple)
print(menu, type(menu))


'''
if 분기처리
if 조건:
    실행 명령문
elif 는??

weather = "맑아요"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요없어요")

처음 if문을 실행하고 맞으면 실행하고 빠져나옴
elif를 이용해서 다음 조건을 한번더 확인하고 실행 후 빠져나옴
위에있는 모든조건이 안맞으면 else를 이용해서 조건외의 모든경우는 else를 한다.      

'''

weather = "비"
if weather == "비":
    print("우산을 챙기세요")

weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요")

# elif
weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")

# else

weather = "맑아요"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요없어요")
'''

# input 하면?
# 사용자의 입력을 받는 문장임. 물어보면? 이문장을 먼저 실행하고나서 사용자가 값을 입력하면 string형테로 weather라는 변수에 저장됨
# 실행을 하면 터미널에 비 / 미세먼지 / etc의 정보를 입력할수있도록 기다려줌 

weather = input("오늘날씨는 어때요?")
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요없어요")

# or를 이용해서 조건추가하기
weather = input("오늘날씨는 어때요?")
if weather == "비" or weather =="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요없어요")



temp = int(input("기온은 어떄요?"))
if 30 <= temp:
    print("너무 더워요 나가지 마세요")
elif 10<= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0<= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지마세요")
'''

'''
반복문 for

'''
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# for 문 기본
for waiting_num in [0,1,2,3,4]:
    print("대기번호: {0}".format(waiting_num))

# in range
for waiting_num in range(1,5): # 1,2,3,4
    print("대기번호: {0}".format(waiting_num))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었씁니다.".format(customer))
# 스타벅스에 리스트 정의하고
# customer라는 변수에다가 스타벅스를 0번부터 쭈루룩 호출하라!



'''
while

while (조건) 을 만족할때까지 반복하라
'''
# 스벅에서 5번 불렀는데 손님없으면 커피 버린다 정책

customer = "토르"
index = 5
while index >= 1:
    print("{}, 커피가 준비되었습니다. {}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# 토르라는 변수가 index번 만큼 반복되었을때를 가정한다.
# index가 1과 같거나 클때 0번의 customer를 호출 하고 index의 5를 호출한다.
# 그다음 index 변수를 -1씩 줄이고 계속 호출을 한다.
# 계속하다가 if 0이 되었을때 커피는 버린다는 문장을 호출한다.
'''

# 무한루프
customer = "아이언맨"
index = 1
while True:
    print("{}, 커피가 준비되었습니다. {}번 남았어요".format(customer, index))
    index += 1
'''

'''
또다른 케이스
customer = "토르"
person = "Unknown"
while person != customer :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
'''

# customer에 토르를 지정해놓고 person은 Unknwon 상태일떄
# person이 customer와 일치할때까지 계속물어봐줘 어떻게?
# customer변수님 커피가 준비되었습니다.라고
# 근데 여기서 비교를 할떄 person에다가 물어보는거야 이름이 어떻게 되세요라고?
# 그럼 내가 입력을 하면 while 문의 person에다가 대입을 할겠지 그리고 같지 않으면 무한반복한다.

'''
continue와 break
'''

absent = [2,5] #결석한 학생
for student in range(1,11):
    if student in absent:
        continue
    print("{0}, 책을 읽어라".format(student))

# 결석자가 2,5번인상황에서
# for문을 사용해서 1~10번까지의 학생이 있을때 반복해라
# if 절을 사용해서 만약 학생이 결석이라면?
# 계속반복해라 1,2번스킵,3, 4, 5번스킵, 6, 7...10까지
# 여기서 print를 하지않고 먼저 다시 반복문으로 돌아간다
# 순서를 정리하면 for문 > if문 > continue > 1~10번반복 > print이다.

absent = [2,5] #결석한 학생
no_book = [7] #책없음
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘수업 여기까지 {0}는 교무실로.".format(no_book))
        break
    print("{0}, 책을 읽어라".format(student))

# 결석자가 2,5번인상황과 책없는 7번상황이 있는경우
# for문을 사용해서 1~10번까지의 학생이 있을때 반복해라
# if 절을 사용해서 만약 학생이 결석인상황과 elif의 책이없는 두가지 상황을 정의했다.
# 계속반복해라 1,2번스킵,3, 4, 5번스킵, 6까지
# 여기서 print를 하지않고 먼저 다시 반복문으로 돌아간다
# 반복을 하다가 7번쨰에서 책이 없으므로 break를 해서 멈춘다.
# 순서를 정리하면 for문 > if문 > continue > 1~6번반복 > print > 7번반복 > break > print


'''
한줄 for문

'''

#출석번호가 1,2,3,4 까지 있는데 룰이바뀌어서 앞에 100을 붙이기로함 (101,102,103)

student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student] # i에다가 100을 더한 값을 넣을건데 student의 리스트에 있는 애들을 불러오면서 100을 더한값을 계속 list로 바꿔서 넣어라
print(student)


# 학생이름을 길이로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [len(i) for i in student] # i는 student에 리스트에 들어가있는값들을 조회하면서 그길이를 len로 조회해서 student에다가 다시 넣어줌
print(student)

# 학생이름을 대문자로 변환
student = ["iron man", "thor", "i am groot"]
student = [i.upper() for i in student]
print(student)

'''
함수
function

def 함수명(전달하려는값):
'''

def open_account():
    print("새로운 계좌가 생성되었습니다.") # 이 자체만으로는 아무것도 못한다. 실행은 함수명으로 해주어야함.

open_account()

def deposit(balance, money): # 입금함수
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금함수
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 불가능합니다. 잔액은 {0}원 입니다.".format(balance))

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 여러개의 값을 한번에 반환

balance = 0 # 잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commision, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commision, balance))

# 처음에는 balacne라는 변수에다가 0원을 넣었는데
# balance에는 deposit이라는 함수를 호출하면서 현재잔액인 0원과 1000원의 money를 넣어줌으로써 함수인 def deposit을 호출한다.
# 그렇다면 def deposit에서는 balance인 0원과 입금한 돈인 10000원을 받아서 더해주게되고 프린트를 해주고
# return을 통해서 반환을 해주는데 return을 통해서 반환한 값을 balance에다가 저장을 해주는거다
# 그리고나서 print를 통해서 balance를 불러보니 1000원

'''
기본값 설정

'''

def profile(name, age, main_lang):
    print("이름은 {0}, \t나이 : {1}\t 사용언어 : {2}"\
          .format(name, age, main_lang)) # 줄바꿈 처리는 역슬래쉬 엔터

profile("유재석", 20, "파이썬")
profile("김태호", 10, "자바")

# 만약 같은학교 같은학년 같은반 같은수업을 듣는사람이라면?
# 나이, 언어는 같고 이름만 다르겠지? 이때 기본값을 쓴다.


def profile(name, age = 17, main_lang = "python"):
    print("이름은 {0}, \t나이 : {1}\t 사용언어 : {2}"\
          .format(name, age, main_lang)) # 줄바꿈 처리는 역슬래쉬 엔터

profile("유재석")
profile("김태호")


'''
키워드 값

순서 맘대로 바꿀수있는거.
'''

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="파이썬", age = 20)
profile(name = "김태호", age = 25, main_lang="파이썬")




'''
가변인자를 이용한 함수호출

'''

'''
end = " ") 하면 줄바꿈 안되고 하나의 줄에 출력됨
[적용 안했을떄]
이름 : 유재석 	 나이 : 20 	 
python java C C++
[적용 했을떄]
이름 : 유재석 	 나이 : 20 	  python java C C++
'''

def profile(name, age, lang1, lang2, lang3, lang4):
    print("이름 : {0} \t 나이 : {1} \t ".format(name, age), end = " ")
    print(lang1, lang2, lang3, lang4)

profile("유재석", 20, "python", "java", "C", "C++")
profile("김태호", 25, "kotlin", "swift", "", "")

# 갑자기 언어가 늘거나 언어가 적다면? 함수를 바꾸거나, 빈값을 매번적어줘야한다.

def profile(name, age, *language):
    print("이름 : {0} \t 나이 : {1} \t ".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "python", "java", "C", "C++","JS")
profile("김태호", 25, "kotlin", "swift")


'''
지역변수와 전역변수

- 지역변수 : 함수내에서만 쓸수있는것만 함수가 호출될때만들어졌다가 끝나면 사라지는거
- 전역변수 : 모든공간에서 쓸수있는거
'''

gun = 10
'''

def checkpoint(soldiers):
    gun = gun - soldiers # 이 gun은 checkpoint 함수내에서 만들어진 gun이다. 그런데 초기화가 안되서 쓸수가 없다는거야.. 이게 지역변수다.
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0} 입니다.".format(gun))
'''

def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0} 입니다.".format(gun))

'''
전체 총 : 10
[함수 내] 남은 총 : 18
남은 총 : 10 입니다.
이렇게 나오는데, 이말은 밖에있는 gun이 아닌 함수내부의 20에서 soldiers의 2를 뺸값이라는거지

'''

def checkpoint(soldiers):
    global gun # 전역공간에 있는 gun이라는 변수를 checkpoint 함수내부에서 쓰겠다. 코드관리가 어려워지므로 자주쓰지는 말고 파라미터로 받는걸 우선적으로 해보자
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_return(gun, soldiers): # gun 정보를 첫번째전달값으로 받고, 경계근무를 soldiers로 받아
    gun = gun - soldiers # 총 gun을 gun - soldiers로 받아
    print("[함수 내] 남은 총 : {0}".format(gun)) # 여기까지는 지역변수로 받기 떄문에 밖에있는 gun이 바뀌지않지만
    return gun # return을 해줌으로써 바뀐 값을 외부로 던질수있고, 밖에서는 gun이라는 변수에 함수에서 계산되고 반환되는 값을 받아서 다시 저장할수 있음.

'''
외부에서 gun이라는 변수를 정의를 하고 체크포인트 함수를 호출하는데
604번줄을 호출할때 외부의 gun = 10 를 바로 def checkpoint_return(gun, soldiers): 함수로 넘겨서
gun = checkpoint_return(gun, 2)를 바로 계산을 합니다잉
변경된값을 return을 해주는데
이걸 함수호출해주는곳에서 받으면?
8이라는 값이 들어가겠죠잉
'''

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
#checkpoint(2)
print("남은 총 : {0} 입니다.".format(gun))

'''
표준 입출력 할차례
'''
import sys

# print("python", "java", file = sys.stdout)
# print("python", "java", file = sys.stderr) # 에러는 표준에러 로깅해서 에러처리

# print("python", "java") # 띄워쓰기됨
# print("python" + "java") # 붙어서 나옴
# print("python", "java", sep = ", ") # python, java
# print("python", "java", "JS", sep = " vs ") # python, java
# print("python", "java", sep = ", " , end = " ? ") # end 문장의 끝부분을 물음표로 바꿔달라
# print("무엇이 더 재밋을까요?")

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, scores in scores.items(): #  scores.items 하면 key(subject)와 value(scores) 페어로 나오잖아
    # print(subject, scores)
    print(subject.ljust(8), str(scores).rjust(4), sep = ":") # ljust(left) 왼쪽으로 정렬을 하는데 8칸의 공간을 확보한상태에서 정렬해라

#001, 002로 채워보자
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill은 3크기만큼의 공간을 확보하고 값이 없는건 0으로 채워달라는거야

# answer = input("아무값이나 입력하세요") # input을 통해서 사용자가 입력을 하게되면 항상 문자열형태로 저장이 된다.
# print("입력하신 값은 " + answer + "입니다")


'''
다양한 출력 form
'''

# 빈자리는 빈공간으로 두고 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print(("{0: >10}").format(500))

# 양수일떈 +로 표시, 음수일떈 -로 표시
print(("{0: >+10}").format(500))
print(("{0: >+10}").format(-500))

# 왼쪽정렬하고, 빈칸을 _로 채움
print(("{0:_<+10}").format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000))

# 3자리마다 콤마를 찍어주기, +,_ 붙이기
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))

# 3자리마다 콤마를 찍어주기, +,_ 붙이기, 자릿수 확보하기, 빈자리는 ^로 채우기
print("{0:^<+30,}".format(1000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정자릿수까지만출력
print("{0:.2f}".format(5/3))

'''
파일 입출력
아래공식대로라면 score.txt가 생김.
'''
# 파일쓰기
# score_file = open("scroe.txt", "w", encoding="utf8")
# print("수학 : 0 ", file = score_file)
# print("영어 : 50", file = score_file)
# print("코딩 : 100", file = score_file)
# score_file.close()

# 파일 위에 더쓰기
# score_file = open("scroe.txt", "a", encoding="utf8") # a 옵션은 append 의 뒤에 계속 이어서 쓰고싶어!
# score_file.write("\n국사 : 80")
# score_file.write("\n과학 : 80") # write를 통해서 쓸때는 줄바꿈 처리해야됨

# 모든 내용 불러오기
# score_file = open("scroe.txt", "r", encoding="utf8") # r 옵션은 read 옵션
# print(score_file.read())
# score_file.close()

# 한줄한줄불러와서 처리하고싶어
# score_file = open("scroe.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽는걸 하는데, 한줄 읽고 커서는 다음줄로 이동함.
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# 몇줄인지 알수 없을떄 읽어오기(총몇출인지 모르니까 while문으로 가져온다)
# score_file = open("scroe.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 리스트에 값을 다 넣어서 처리하기
# score_file = open("scroe.txt", "r", encoding="utf8")
# lines = score_file.readlines() # lins"s"를 통해서 모든라인을 가져와서 list 형태로 저장해준다
# for line in lines:
#     print(line, end="")
# score_file.close()


'''
pickle
프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장.
피클을 이용해서 데이터를 가져와서 코드에서 또 쓸수있게
변수에 저장해서 쓸수있게끔
'''

import pickle

# # 피클파일에 넣어주기
# profile_file = open("profile.pickle", "wb") # w= write, b = binary(항상타입정의해줘야됨), 인코딩설정 필요없음
# profile = {"이름 : 박명수", "나이 : 30", "취미 : 농구"}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 덤프해줘서 저장해라
# profile_file.close()

# 피클파일에서 가져오기
profile_file = open("profile.pickle", "rb") # r= read, b = binary(항상타입정의해줘야됨), 인코딩설정 필요없음
profile = pickle.load(profile_file) # 파일에 있는 정보는 profile에 불러와라
print(profile)
profile_file.close()

'''
with.... 건너뛰자일단
'''










