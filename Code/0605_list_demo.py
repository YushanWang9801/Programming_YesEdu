list1 = []

list2 = [1,3,4,5,6,]

print(list2[-2])

print("list 2 length: ")
print(len(list2))

list2.append(7)
print(list2)
print()

list2.pop(0)
print(list2)
print()


list2 = [1,3,4,5,6,4]
list2.remove(4)
print(list2)
print()

for i in range(len(list2)):
    print(list2[i])
print()

for i in list2:
    print(i)

for idx, i in enumerate(list2):
    print((idx, i))