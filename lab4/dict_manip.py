dict1 = {
	"one" : 1,
	"two" : 2,
	"three" : 3,
	"dour" : 1,
}

dict2 = {
	"one" : 2,
	"two" : 4,
	"three" : 6,
}

for key in dict1.keys():
    if (dict2.get(key)):
    	dict1[key] += dict2[key]

print(dict1)