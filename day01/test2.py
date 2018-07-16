'''
weak = "星期一星期二星期三星期四星期五星期六星期日"
a=int(input("请输入数字"))
q=(a-1)*3
print(weak[q:q+3])
'''


a = input("请输入一串字符串")

i = 0
while i<len(a):
	if 97<=ord(a[i])<=122:    #判断
		d = ord(a[i])-32     #d/x 是取a[i]的值+-32 
		m= chr(d)			#m/n 是转换大小写
		print(m)
		i=i+1
	elif 65<=ord(a[i])<=90:
		x=ord(a[i])+32
		n=chr(x)
		print(n)
		i=i+1
