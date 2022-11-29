
numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)
print("* - "*10)
print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
print("* - "*10)
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist2 = [x for x in fruits if "a" in x]

print(newlist2)