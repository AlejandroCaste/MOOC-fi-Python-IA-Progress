# Write your solution here
def list_sum(list1: list, list2: list):
    index = 0
    list_sum = []
    while index < len(list1):
        x = list1[index] + list2[index]
        list_sum.append(x)
        index += 1
    return list_sum
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]