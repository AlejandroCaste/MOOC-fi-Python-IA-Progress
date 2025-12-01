# Write your solution here
def line (num, text):
    if text == "":
        text = "*"
    print(num * text[0])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")