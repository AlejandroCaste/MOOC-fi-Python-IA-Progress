# Write your solution here
def calcular_nota(puntos_examen, ejercicios_completados):
    puntos_ejercicio = ejercicios_completados // 10
    puntuacion_total = puntos_examen + puntos_ejercicio
    nota = 0

    if puntos_examen < 10:
        nota = 0
    elif puntuacion_total <= 14:
        nota = 0
    elif puntuacion_total <= 17:
        nota = 1
    elif puntuacion_total <= 20:
        nota = 2
    elif puntuacion_total <= 23:
        nota = 3
    elif puntuacion_total <= 27:
        nota = 4
    else:
        nota = 5
        
    return puntuacion_total, nota

def recopilar_estadisticas():
    puntuaciones_totales = []
    distribucion_notas = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0} 

    while True:
        try:
            linea_entrada = input("Exam points and exercises completed: ")
            
            if not linea_entrada:
                break
            
            datos = list(map(int, linea_entrada.split()))
            
            if len(datos) == 2:
                puntos_examen, ejercicios_hechos = datos[0], datos[1]
                
                p_total, nota_final = calcular_nota(puntos_examen, ejercicios_hechos)
                
                puntuaciones_totales.append(p_total)
                distribucion_notas[nota_final] += 1
            
        except EOFError:
            break 
            
        except ValueError:
            continue 

    return puntuaciones_totales, distribucion_notas

def mostrar_estadisticas(puntos, distribucion):
    num_estudiantes = len(puntos)
    
    if num_estudiantes == 0:
        return

    promedio = sum(puntos) / num_estudiantes
    
    suspendidos = distribucion[0]
    aprobados = num_estudiantes - suspendidos
    porcentaje_aprobados = (aprobados / num_estudiantes) * 100
    

    print("\nStatistics:")
    print(f"Points average: {promedio:.1f}")
    print(f"Pass percentage: {porcentaje_aprobados:.1f}")

def imprimir_distribucion(distribucion):
    print("Grade distribution:")
    for nota in range(5, -1, -1):
        cantidad = distribucion[nota]
        estrellas = "*" * cantidad
        print(f"{nota}: {estrellas}")


puntos_totales, conteo_notas = recopilar_estadisticas()

if puntos_totales:
    mostrar_estadisticas(puntos_totales, conteo_notas)
    imprimir_distribucion(conteo_notas)