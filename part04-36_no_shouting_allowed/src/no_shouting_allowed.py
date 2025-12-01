# Write your solution here
def no_shouting(my_list: list):
    index = 0
    list_length = len(my_list)
    new_list = []
    while index < list_length: 
        
        current_word = my_list[index]
        if not current_word.isupper():
            new_list.append(current_word)
        index += 1
        
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list) 
  