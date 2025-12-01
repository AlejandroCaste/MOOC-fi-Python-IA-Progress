# Write your solution here
while True:
    editor = input("Editor = ")
    e = editor.lower()
    if "visual studio code" == e:    
        print("an excellent choice!")
        break
    elif editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")