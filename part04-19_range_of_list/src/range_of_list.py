# Write your solution here
def range_of_list(my_list: list):
    maxim = max(my_list)
    minim = min(my_list)
    range = maxim - minim
    return(range)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)