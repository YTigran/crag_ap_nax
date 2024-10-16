cort1 = (1, 2, 3, 4, 5)
cort2 = (6, 7, 8)

cort3 = (cort2[len(cort2) - 1], *cort1[1:len(cort1)], *cort2[0: len(cort2) - 1], cort1[0])

print(cort3)