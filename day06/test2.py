z = 0
l = 0
for i in range(100,1001):
	for n in range(2,i):
		if i%n==0:
			print(i)
			l=l+1
			break
		else:
			continue
	else:
		z=z+1
print(l)
print(z)
