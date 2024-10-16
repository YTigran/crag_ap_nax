def is_prime (a):
	if (a == 1 or a < 0):
		return False
	if (a % 2 == 0 and a != 2):
		return False
	for i in range(3, a // 2, 2):
		if (a % i == 0):
			return False
	return True

a = int(input("Input the number: "))

print("The prime numbers: ")
for i in range(a):
	if (is_prime(i)):
		print(i, end=' ')
print()
