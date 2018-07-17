name = input ("请输入用户名")
for i in range(len(name)):
	o = ord(name[i])
	if 97<=o<=122 or 65<=o<=90 or 48<=o<=57 or o == 95:
		pass
	else:
		print("用户名错误")
		break


'''
for i in range(len(name))
	if name[i].isupper() or name[i].islower() or \
		name[i].isdigit() or ord(name[i]==95 ) :
'''
