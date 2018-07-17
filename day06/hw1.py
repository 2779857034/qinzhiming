import random 
a = random.randint(0,10)


for i in range(0,3):
	try:	
		x = int(input("请输入一个数"))
	except ValueError:
		print("数字！！数字")
		continue
	if a==x:
		print("厉害了，500万属于你")
		break
	elif a>x:
		print("小了")
	else:
		print("大了")
else:
	print("机会用光了呢")
print(a)
