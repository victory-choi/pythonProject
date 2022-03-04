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
print(python.index("java")) #index는 프로그램 종료
print(python.count("n")) # 몇번 동작하냐
# 4-4강 볼차례 여기서 그만
