# Write your solution here
def most_common_character(my_string: str) -> str:
    counts = {}
    max_count = -1 
    most_common = "" 
    
    for character in my_string:
        counts[character] = counts.get(character, 0) + 1
        current_count = counts[character]
        if current_count > max_count:
            max_count = current_count
            most_common = character
            
    return most_common
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))