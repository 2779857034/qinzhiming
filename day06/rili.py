# shuru
x = 0 #用来统计整年的日期
year = 0
nyear,nmonth=eval(input("请输入年份，月份"))
#判断平年闰年
'''
if year%4==0 and year%400!=0 or year%400==0:
	year = 366
else:
	year = 365
'''
#计算输入的年份和1990年1月之间的整年数
for i in range(1990,nyear):
	if i%4==0 and i%400!=0 or i%400==0:
		year = 366
		x=year+x
	else:
		year = 365
		x=year+x
# print(x)
day = 0
#计算输入的年份从本年1月1日开始到现在的天数
if nyear%4==0 and nyear%100!=0 or nyear%400==0:
	month2 = 29
	for i in range(1,nmonth):
		if  i== 1 or i== 3 or i== 5 or i== 7 or i== 8 or i== 10 or i== 12 :
			day = day+31
		elif i == 4 or i== 6 or i== 9 or i== 11:
			day = day+30
		else:
			day = day+29
else:
	month2 = 28

	for i in range(1,nmonth):
		if  i== 1 or i== 3 or i== 5 or i== 7 or i== 8 or i== 10 or i== 12 :
			day = day+31
		elif i == 4 or i== 6 or i== 9 or i== 11:
			day = day+30
		else:
			day = day+28
# print(day)
# 计算输入的nmonth有多少天
if nyear%4==0 and nyear%100!=0 or nyear%400==0:
	if  nmonth== 1 or nmonth== 3 or nmonth== 5 or nmonth== 7 or nmonth== 8 or nmonth== 10 or nmonth== 12 :
		mday = 31
	elif nmonth == 4 or nmonth== 6 or nmonth== 9 or nmonth== 11:
		mday = 30
	else:
		mday = 29
else:
	if  nmonth== 1 or nmonth== 3 or nmonth== 5 or nmonth== 7 or nmonth== 8 or nmonth== 10 or nmonth== 12 :
		mday = 31
	elif nmonth == 4 or nmonth== 6 or nmonth== 9 or nmonth== 11:
		mday = 30
	else:
		mday = 28


# 计算当前日期到1990年1月1日总天数
dayall = x+day+1
m = dayall%7  # 星期几
# print("现在是星期{}".format(m))
titlesr = "{}月 {}".format(nmonth,nyear)
print(titlesr.center(20))
print("日 一 二 三 四 五 六")
for i in range(m):
	print("   ",end='')
for i in range(1,mday):
	print("{:>2}".format(i),end='\n'if (m+i)%7==0 else ' ')
print()
	




