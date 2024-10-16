line = input("input the string: ")
vowel = 0
consonant = 0

for ch in line:
	if ((ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u')):
		vowel += 1
	else:
		consonant += 1

print("The vowel chars: " + str(vowel))
print("The consonant chars: " + str(consonant))