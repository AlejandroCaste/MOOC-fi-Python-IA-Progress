# Write your solution here
def all_the_longest(my_list: list) -> list:

    if not my_list:
        return [] 
        
    max_length = len(my_list[0]) 
    
    for word in my_list:
        current_length = len(word)
        

        if current_length > max_length:
            max_length = current_length
            
    longest_words = [] 
    
    for word in my_list:
        if len(word) == max_length:
            longest_words.append(word)
            
    return longest_words

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) 
