s1 = input("请输入字符串")
s2 = input("请再输入一个字符串")
i=0
if len(s1)>len(s2):
	a = len(s2)
elif len(s1)<len(s2):
	a = len(s1)
else:
	a=len(s1)
while i<a:
	z1 = ord(s1[i])
	z2 = ord(s2[i])
	if z1>z2 :
		print("{}大于{}".format(s1,s2))
		break
	elif z1<z2:
		print("{}小于{}".format(s1,s2))
		break
	elif i==a-1:
		if len(s1)>len(s2):
			print("字符串{}大".format(s1))
		elif len(s1)<len(s2):
			print("字符串{}大".format(s2))
		else:
			print("字符串相等")
	i=i+1
'''
#如果不一样长但较短的字符串和长字符串前面相同 或者两字符串相等
if len(s1)>len(s2):
	print("1长")
elif len(s2)>len(s1):
	print("2长")
else:
	print("相同")
'''
