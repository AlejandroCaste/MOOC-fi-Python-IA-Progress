# Write your solution here
def longest_series_of_neighbours(lista):
    if not lista:
        return 0
    
    max_longitud = 1
    longitud_actual = 1
    
    for i in range(1, len(lista)):
        if abs(lista[i] - lista[i-1]) == 1:
            longitud_actual += 1
        else:
            longitud_actual = 1
            
        max_longitud = max(max_longitud, longitud_actual)
            
    return max_longitud