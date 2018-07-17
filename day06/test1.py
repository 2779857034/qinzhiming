num = eval(input("请输入一个整型数"))
save = num
newnum = 0

while num:
	newnum = (num%10)+newnum*10
	num = num // 10
if newnum == save:
	print("是")
else:
	print("不是")

