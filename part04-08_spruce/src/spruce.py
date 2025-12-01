# Write your solution here
def spruce (x):
    print ("a spruce!")
    y = x
    media = x - 1
    medio = " " * media
    simbolo = "*"
    while x > 0:
        print(f"{medio}{simbolo}")
        simbolo = simbolo + "**"
        media -= 1
        medio = " " * media
        x -= 1
    print(" " * (y - 1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)