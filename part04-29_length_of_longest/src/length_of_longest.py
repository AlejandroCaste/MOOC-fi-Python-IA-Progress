# Write your solution here
def length_of_longest(my_list: list):
 
    max_length = 0 

    for word in my_list:
        current_length = len(word)

        if current_length > max_length:
            
            max_length = current_length

    return max_length


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
