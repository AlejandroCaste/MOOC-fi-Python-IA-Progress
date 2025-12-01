# Write your solution here
x = int(input("Please type in a positive integer: "))
y = -x
for number in range(y, (x+1)):
    if number == 0:
        continue
    else:
        print(number)