# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
# La función vuelve a recibir la palabra que la plataforma le pasa
# REQUISITO 1: Definir la función que comprueba si es palíndromo
# Esta función solo se encarga de la lógica de True/False.
def palindromes(string: str):
    # Comprueba si la cadena es igual a su inversa
    reverse_string = string[::-1]
    
    if string == reverse_string:
        return True
    else:
        return False

# ----------------------------------------------------------------

# REQUISITO 2 y 3: Programa Principal Interactivo (Fuera del if __name__)
while True:
    # Pedir la entrada al usuario (REQUISITO INTERACTIVO)
    word = input("Please type in a palindrome: ")
    
    # Usar la función para comprobar la palabra ingresada
    if palindromes(word):
        # Si la función devuelve True
        print(f"{word} is a palindrome!")
        break # Salir del bucle
    else:
        # Si la función devuelve False
        print("that wasn't a palindrome")