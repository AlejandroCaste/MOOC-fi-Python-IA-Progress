# Write your solution here
def distinct_numbers  (my_list : list):
    a = set(my_list)
    a = sorted(a)
    return a

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]