a = eval(input("请输入pm2.5的值"))
if a>75:
	print("重度污染，不宜出行")
elif 35<a<=75:
	print("空气良好，适当户外出行")
else:
	print("赶紧出来嗨")
