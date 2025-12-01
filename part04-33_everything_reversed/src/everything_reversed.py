# Write your solution here
def everything_reversed(my_list: list) -> list:
    new_list = []
    i = len(my_list) - 1
    while i >= 0:
        item = my_list[i]
        reversed_item = item[::-1]
        new_list.append(reversed_item)
        i = i - 1
    return new_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)