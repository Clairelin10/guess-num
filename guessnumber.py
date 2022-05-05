import random

start = input('請決定終極密碼戰數字範圍，開始值: ')
end = input('請決定終極密碼戰數字範圍，結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	guess = input('請猜數字: ')
	guess = int(guess)

	if guess == r:
	    print('終於猜對了！')
	    print('這是你猜的第', count, '次')
	    break
	else:
	    if guess > r:
	        print(guess, '比答案大喔！')    
	    else:
	    	print(guess, '比答案小唷！')
	print('這是你猜的第', count, '次')