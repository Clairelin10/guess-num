import random

r = random.randint(1, 100)
while True:
	guess = input('1 ~ 100 猜一數字？ 請輸入數字: ')
	guess = int(guess)

	if guess == r:
	    print('終於猜對了！')
	    break
	else:
	    if guess > r:
	        print(guess, '比答案大喔！')    
	    else:
	    	print(guess, '比答案小唷！')