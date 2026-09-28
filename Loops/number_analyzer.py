
num = input("Give a positive integer: ")
num = int(num)

sum = 0

for i in range(1, num + 1, 1):
    print(i)
    sum += i

print(sum);