from superduper import list

first = "qwertyuiop"
second = "asdfghjkl"
third = "zxcvbnm"
num1 = int(input("1 > "))
num2  = int(input("2 > "))
num3 = int(input("3 > "))

for i in list:
	fiserd = [0, 0, 0]
	for t in i:
		t = t.lower()
		if t in first:
			fiserd[0] += 1
		elif t in second:
			fiserd[1] += 1
		elif t in third:
			fiserd[2] += 1
	if fiserd[0] == num1 and fiserd[1] == num2 and fiserd[2] == num3:
		print(fiserd, i)
