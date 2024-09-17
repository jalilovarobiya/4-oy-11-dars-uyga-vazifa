dict1 = dict()

for i in range(1, 6):
    dict1[i] = int(input("qiymat kiriting: "))

print(dict1)

for i in range(1, 4):
    max_qiymat = 0
    max_key = 0
    for key in dict1.keys():
        if max_qiymat < dict1[key]:
            max_qiymat = dict1[key]
            max_key = key
    print(max_key, end=" ")
    dict1.pop(max_key)
print()
