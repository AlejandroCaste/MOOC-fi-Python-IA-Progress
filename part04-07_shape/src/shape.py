# Copy here code of line function from previous exercise and use it in your solution
def line (num, text):
    if text == "":
        text = "*"
    print(num * text[0])

def shape (num_x , text_x , num_y , text_y):
    num = 1
    while num_x > 0:
        line(num , text_x[0])
        num += 1
        num_x -= 1
    num -= 1
    while num_y > 0: 
        line (num , text_y)
        num_y -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")