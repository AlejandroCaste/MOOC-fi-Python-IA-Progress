# Copy here code of line function from previous exercise
def line (num, text):
    if text == "":
        text = "*"
    print(num * text[0])

def triangle(size):
    num = 1
    while size > 0:
        line(num, "#")
        num += 1
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
