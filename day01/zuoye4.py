s = input("请输入字符串")
q=0
x=0
s=s.lower()
z=[]
for i in range(0,len(s)):
	z.append(s[i])
a=len(s)
while q<a:
	if ord(s[q])==32:
		x=1
		print("1")
	elif x==1:
		z[q]= z[q].upper()
		print("2")
		x=0
	elif 97<=ord(s[0])<=122:
		z[0]=z[0].upper()
	q=q+1
print("".join(z))


 
