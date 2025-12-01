# Write your solution here

def greatest_number (a , b, c):
    if a > b and a > c or a == b and a == c or a > b and a == c or a == b and a > c:
        return a
    elif b > a and b > c or b == a and b == c or b > a and b == c or a == b and b > c:
        return b
    elif c > b and c > a or c == b and a == c or c > b and a == c or c == b and c > a:
        return c
    
 
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)