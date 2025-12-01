# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    index_uno = len(my_list)
    if index < 0:
        break
    elif index > index_uno:
        print("Try again.")
        continue
    else:
        new_valor = int(input("New value: "))
        my_list[index] = new_valor
        print(my_list)