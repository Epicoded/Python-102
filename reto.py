#if __name__ == '__main__':
#    x = int(input())
#    y = int(input())
#    z = int(input())
#    n = int(input())

#print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])

x=1
y=1
z=2
n=3
print(range(x+1))
print(range(y+1))
print(range(z+1))
print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n])

#ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10

#print(ListOfThreeMultiples)