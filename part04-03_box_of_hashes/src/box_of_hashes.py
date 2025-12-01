# Copy here code of line function from previous exercise

def line (num, text):
    if text == "":
        text = "*"
    print(num * text[0])

# You should call function line here with proper parameters

def box_of_hashes (num):
    while num > 0:
        line(10, "#")
        num -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
