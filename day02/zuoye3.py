a = eval(input("请输入购买的价格"))
b = 0
if 50<=a<=100:
	b=a-a*0.1
	print("您有10%的折扣")
elif a>100:
	b=a-a*0.2
	print("您有20%的折扣")
else:
	b=a
print("最终花费{}".format(b))
