def anagrams(texto_uno, texto_dos):
    # 1. Crear listas de caracteres para ambas cadenas
    lista_uno = []
    for letter in texto_uno:
        lista_uno.append(letter)
    lista_dos = []
    for letter in texto_dos:
        lista_dos.append(letter)

    lista_uno.sort()
    lista_dos.sort()
    
    return lista_uno == lista_dos

if __name__ == "__main__":
    print(anagrams("tame", "meta"))  
    print(anagrams("tame", "mate"))  
    print(anagrams("team", "time"))  
