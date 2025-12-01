# Write your solution here

def mean(my_list: list):
    sum_of_elements = sum(my_list)
    number_of_elements = len(my_list)
    if number_of_elements == 0:
        return 0 
    else:
        return sum_of_elements / number_of_elements

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)