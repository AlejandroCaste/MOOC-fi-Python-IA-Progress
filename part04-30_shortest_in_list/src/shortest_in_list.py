# Write your solution here
def shortest(my_list: list):
    shortest_word = my_list[0]
    min_length = len(my_list[0]) 

    for word in my_list:
        current_length = len(word)

        if current_length < min_length:
            min_length = current_length 
            shortest_word = word       

    return shortest_word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result) 