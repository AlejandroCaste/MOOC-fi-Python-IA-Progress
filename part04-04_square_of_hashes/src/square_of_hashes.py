# Copy here code of line function from previous exercise
def line (num, text):
    if text == "":
        text = "*"
    print(num * text[0])

def square_of_hashes(num):
    # You should call function line here with proper parameters
    size = num
    while size > 0:
        line(num, "#")
        size -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
