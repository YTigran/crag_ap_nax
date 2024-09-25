def num_sum(a):
	res = 0
	while(a != 0):
		res += a % 10
		a = int(a / 10)
	return res

a = int(input("Input the number: "))

print("The res is", num_sum(a))