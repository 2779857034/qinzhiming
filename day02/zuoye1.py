sg,tz = eval(input("请输入身高和体重"))
sg = sg / 100
bmi = tz/(sg*sg)
if bmi<18.5:
	print("体重过轻")
elif 18.5<=bmi<=23.9:
	print("正常")
elif 24<=bmi<=27:
	print("过重")
elif 28<=bmi<=32:
	print("肥胖")
elif bmi>32:
	print("非常肥胖")
