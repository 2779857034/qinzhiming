import time
i = 0
a = '##'
b = '--'
s = 0
while i<=10:
	a1= a*i
	b1= b*(10-i)
	s = i*10 
	print("当前进度:%5d%%"%s,end='   ')
	print("")
	print(a1,end='')
	print(b1)
	time.sleep(0.1)
	i=i+1



