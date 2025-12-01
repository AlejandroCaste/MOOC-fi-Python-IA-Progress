# Write your solution here
def no_vowels (my_string: str):
    new_string = []
    vocals = ["a", "e", "i", "o", "u"]
    normalized_string = my_string.lower()

    for letra in my_string:
        if letra in vocals:
            continue
        else:
            new_string.append(letra)
    return "".join(new_string)

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))