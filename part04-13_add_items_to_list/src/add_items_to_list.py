# Write your solution here

vueltas = int(input("How many items: "))
item_vuelta = 1
my_list = []
while vueltas > 0:
    item = int(input(f"Item {item_vuelta}: "))
    item_vuelta += 1
    vueltas -= 1
    my_list.append(item)
        
print(my_list)