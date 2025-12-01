# Write your solution here
list_word = []
index = 0
while True:
    word = input("Word: ")
    if word in list_word:       
        break
    else:
        list_word.append(word)  
        index += 1        

print(f"You typed in {index} different words")