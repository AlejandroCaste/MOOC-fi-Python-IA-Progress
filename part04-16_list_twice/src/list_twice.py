# Write your solution here
my_list = []
while True:
    num = int(input("New item: "))
    my_list.append(num)
    if num == 0:
        print("Bye!")
        break
    else:
        print(f"The list now: {my_list}")
        new_list = sorted(my_list)
        print(f"The list in order: {new_list}")
