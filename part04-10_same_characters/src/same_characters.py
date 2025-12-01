# Write your solution here
def same_chars(text, x, y):
    n = len(text)
    # 1) validar índices: si alguno está fuera, devolvemos False
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    # 2) ya es seguro indexar
    return text[x] == text[y]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))