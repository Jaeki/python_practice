def f2(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return f2(n//2) +1
	else:
		return f2(3*n+1) + 1

def f6(lst):
	if type(lst) != list or lst ==[]:
		return lst
	elif type(lst[0]) != list:
		return [lst[0]] + f6(lst[1:])
	else:
		return f6(lst[0]) + f6(lst[1:])

def f4(lst):
	if lst == []:
		return 
	if lst[0] % 2 == 1:
		print(lst[0] * 3)
		return f4(lst[1:])
	else: return f4(lst[1:])

def f8(s):
	k = len(s) - 1
	if s == "":
		return True
	if s[0] != s[k]:
		return False
	else:
		return f8(s[1:k])
	return True


def f10(list):
	
	if list == []:
		return 0
	else:
		return f10(list[1:])  + 1

def f12(n):
	if n == 0:
		return
	else:
		print(n)
		f12(n-1)

def f14(list):
	if list == []:
		return None
	if list[0] % 2 == 1:
		return list[0]
	else:
		return f14(list[1:])

def f16(lst):

	if lst ==[]:
		return lst
	if lst[0] % 2== 1:
		return [lst[0]] + f16(lst[1:])
	else:
		return f16(lst[1:])

def f18(a,b):
	if a> b:
		if a % b == 0:
			return b
		else:
			a = a % b
			return f18(a, b)
	else:
		if b % a == 0:
			return a
		else:
			b = b % a
			return f18(a, b)