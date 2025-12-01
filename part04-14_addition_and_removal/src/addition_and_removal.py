# Write your solution here
my_list = []
print(f"The list is now {my_list}")
num = 1

while True:
    letra = input("a(d)d, (r)emove or e(x)it: ")
    if letra == "d":
        my_list.append(num)
        print(f"The list is now {my_list}")
        num += 1
    elif letra == "r":
        my_list.pop()
        print(f"The list is now {my_list}")
        num -= 1
    elif letra == "x":
        print("Bye!")
        break