num1,num2 = eval(input("请输入两个整型数"))
if num1>num2:
	print("{}大于{}".format(num1,num2))
elif num1<num2:
	print("{}大于{}".format(num2,num1))
else:
	print("两数相等")
