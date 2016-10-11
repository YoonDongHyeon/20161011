#<while 문>
# number =23
# running =True
# while running:
    #무한루프를 쓴다면 while 1을 쓸것이 아니라 while true의 구조가 되어야 한다.
    # guess =int(input('Enter an integer : '))
    #
    # if guess ==number:
    #     print('Congratulations, you are correct')
    #     running = False
        # break#이거를 쓰면 while에 대한 else문이 실행 안됨
    # elif guess < number:
    #     print('좀더 크다')
    # else:
    #     print('좀더 작다')
# else:
#     print('와일문 종료')
#else 구문 쓸수 있으나 사용하지 말아라 와일문이 종료되면 else가 무조건 실행
# print('Done')
#<For 문>

# for 문 쓰는법 FOR는 몇번 실행할지 결정되었을 때 사용
#for i in range(1, 10):
#1부터 10-1까지를 출력
    #arguement 가 하나일 경우는 0부터 시작해서 n개를 출력한다.
#for i in range(10):
# for i in range(2,20,2):
#순서대로 하나씩 가져온다. 2가져오고, 4가져오고, 6가져오고... 하나씩
#2부터 19까지의 짝수를 출력 세번째 선언은 공차를 의미한다.
#print(list(range(1,5)))
#리스트로서 한줄로 1부터 5-1까지 출력
# x = "SKKU"
# for i in x:
#     print(i)
    #문자의 출력
# x = ["SKKU", "University"]
# for i in x:
#     print(i)
    #x가 리스트라면 속성1 skku하나 2인 university를 차례대로 출력
#구구단 출력
# for i in range(1,10):
# for i in range(2,10,2): 를 쓰면 짝수의 단만 출력
#     for j in range(1,10):
#         print('{} * {} = {}'.format(i,j,i*j))
#     else:
#         print('-'*50)
#<몇단 부터 몇단까지 단수를 출력하는 것>
# a=int(input('몇단부터 :'))
# b=int(input('몇단까지 :'))
# for i in range(a,b+1):
#     for j in range(1,10):
#          print('{} * {} = {}'.format(i,j,i*j))
#     else:
#          print('-'*50)
#continue break 를 통해서 loop를 제어할 수 있다.
# continue는 다시 앞의 루프로 돌아가게 하는 기능
#break는 loop를 끝내게 하는 기능.
#function 문법
#say hello라는 함수를 정해주면 다음에는 함수명만 써주면 사용이 가능하다.
# def say_hello():
#     print('Hello World')
# say_hello()
# def my_func(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
# print my_func(1,3)
# print my_func(3.1)

# def my_func(a,b):
#     temp =0
#     if a>=b:
#         temp = a
#     else:
#         temp = b
#     return temp
# print (my_func(1,3))
#지역변수
#함수는 코드의 앞부분에서 지정해주는 것이 좋다.
 # x=50
# def func(x):
#     print('x is',x)
#     x=2
#     x를 2로 바꾼것일까? 아니다. 이 x는 함수내에서만 작용하는 local 변수이다.
#     웬만하면 그냥 다른 변수로 선언을 해주자 헷갈릴 수 있으니
    # print('Changed local x to',x)
#
# func(x)
# x는 50이다 여전히
# print('x is still',x)
#  global 은 쓰지마라
# x = 50

# def func():
#     global x
#     print('x is',x)
#     x=2
#     print('Changed local x to',x)
#
# func()
# print('x is still',x)
# def say(message, times=1):
#     print(message * times)
# say('Hello')
# say('World',5)
#그냥 헬로만 쓰면 times는 1이므로 그냥 한번출력, 월드랑 5로 times를 넣어주면 times에 5가 들어감
# def sme_fuction():
#     pass#아무일도 하지마라
# a = [1, 2, 3, 4]
# a = ["a", "b"]
# a = [1, "b"]
# print (a[0])
#리스트는 이렇게 출력
#1번 인덱스부터 끝까지는 다음과 같다.
# print(a[1:])
#1번부터 1번인덱스까지 출력은 다음과 같다.
# print(a[1:2])
#얘도 1부터 2-1까지 즉, n-1까지 번수 인덱스를 출력하게 한다.
# print(a[-1])
#끝에서부터 셀 때는 -1부터 위의 경우는 4를 출력한다.
# print(len(a))
#리스트의 길이는 안에 있는 원소의 갯수
# print(sorted(a))
#sorted는 리스트를 정렬을 시킨다.
# a=["a","b"]
# b=[1,"1"]
# print (a+b)
# for i in a:
    # print(repr(i))
    #repr은 속성이 숫자인지 문자인지 구별해서 출력해준다.
# c = list()
# c = []

# c.append("a")
# append는 리스트에 그 값을 넣는다는 의미
# print(c)
# a = [1, 3, 2, 4, 5]
# b = [i+1 for i in a]
# 리스트 b는 a의 리스트 속성에 각각 1을 더한 리스트이다. 아래것과 같은 의미
# t = []
# for i in a:
#     t.append(i+1)
# print(b)
# print(t)
# a = [1, 3, 2, 4, 5]
# b = a
# b[0] = 2
#
# print(a)
# print(b)
#얕은 카피.이렇게 하면 b랑 a랑 둘다 첫번째 성분이 2로 바뀜 이거는 파이썬의 특징.
# a = [1, 3, 2, 4, 5]
# b = a[:]
# b[0] = 2
#
# print(a)
# print(b)
#a[:] 이렇게 하면 같은 공간에 저장되어있는 것이 아니라, 아예 값을 가져와서 다른 곳에 저장공간을 확보한다는 의미
# a = (1, 3, 2, 4, 5)
# 이거는 튜플의 형태 append를 쓰지 못한다.
#그러나 print(a[1])로 주소로 불러오는 거는 가능
# print(type(a))
# Dictionary
# a = {'a':1, 'b':2}

# print(a['a'])
#이름으로 값을 불러온다. 리스트는 순서대로 그 위치를 따지지만 이거는 이름만 따짐.
# a = {'a':1, 'b':2}
# print(a.keys())
#이름값
# print(a.values())
#이름에 지정된 실제 값
# a = {'a':1, 'b':2}
# key = a.keys()
# for i in key:
#     print('{} : {}'.format(i, a[i]))