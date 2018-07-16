a = input("请输入字符串")
i = 0
d = 0
x = 0
s = 0
while i<len(a):
	if a[i].isupper():
		d=d+1
		i=i+1
	elif a[i].islower():
		x=x+1
		i=i+1
	elif a[i].isdigit():
		s=s+1
		i=i+1
print("大写字符有{}个，小写字符有{}个，数字有{}个。".format(d,x,s))
