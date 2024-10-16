dict1 = {
	"one" : 1,
	"two" : 2,
	"three" : 3,
}

dict2 = {
	"one" : 1,
	"two" : 2,
	"three" : 3,
}

for val in dict1.get():
    dict2.update(val[0]) += dict1.get(val[0])

print(dict2)