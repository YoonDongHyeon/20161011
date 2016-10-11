#<while 문>
number =23
running =True
while running:
    guess =int(input('Enter an integer : '))

    if guess ==number:
        print('Congratulations, you are correct')
        #running = False
        break#이거를 쓰면 while에 대한 else문이 실행 안됨
    elif guess < number:
        print('좀더 크다')
    else:
        print('좀더 작다')
else:
    print('와일문 종료')
#else 구문 쓸수 있으나 사용하지 말아라 와일문이 종료되면 else가 무조건 실행
print('Done')
