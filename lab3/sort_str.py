def num_counter(line):
	count = 0
	for ch in line:
		if (ch.isnumeric()):
			count += 1
	return count


def alpha_counter(line):
	count = 0
	for ch in line:
		if (ch.isalpha()):
			count += 1
	return count


def sym_counter(line):
	count = 0
	for ch in line:
		if (not ch.isalnum()):
			count += 1
	return count

line = input("Input the string: ")

i = 0
d = len(line)
while i < d:
	if (line[i].isupper()):
		line = line[:i] + line[i + 1:] + line[i]
		d -= 1
		i -= 1
	else:
		i += 1

print("num chars: " + str(num_counter(line)))
print("alphabetic char: " + str(alpha_counter(line)))
print("symbols: " + str(sym_counter(line)))
    