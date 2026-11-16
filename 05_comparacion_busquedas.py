# Programa 5: Comparación de búsquedas
# Actividad 3 - Ordenamiento y Búsqueda en Arreglos

import random

def busqueda_lineal_con_contador(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones

def busqueda_binaria_con_contador(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        if lista[medio] == objetivo:
            return medio, comparaciones
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, comparaciones

# Generar lista de 1000 números aleatorios ordenados
lista = sorted([random.randint(1, 10000) for _ in range(1000)])

# Elegir un número que SÍ esté en la lista (para comparar de forma justa)
objetivo = lista[random.randint(0, 999)]

print("=" * 60)
print("COMPARACIÓN DE BÚSQUEDA LINEAL vs BÚSQUEDA BINARIA")
print("=" * 60)
print(f"\nLista generada: 1000 números aleatorios ordenados (1-10000)")
print(f"Número a buscar: {objetivo}")
print("-" * 60)

# Búsqueda lineal
pos_lineal, comp_lineal = busqueda_lineal_con_contador(lista, objetivo)
print(f"\nBúsqueda LINEAL:")
print(f"  Posición encontrada: {pos_lineal}")
print(f"  Comparaciones realizadas: {comp_lineal}")

# Búsqueda binaria
pos_binaria, comp_binaria = busqueda_binaria_con_contador(lista, objetivo)
print(f"\nBúsqueda BINARIA:")
print(f"  Posición encontrada: {pos_binaria}")
print(f"  Comparaciones realizadas: {comp_binaria}")

print("\n" + "=" * 60)
print("RESULTADO:")
print(f"  La búsqueda binaria realizó {comp_lineal - comp_binaria} comparaciones menos")
print(f"  Eficiencia: {comp_lineal / comp_binaria:.1f}x más rápida (aprox.)")
print("=" * 60)

print("""
# EXPLICACIÓN:
# La búsqueda binaria es más eficiente porque divide el espacio de búsqueda
# a la mitad en cada comparación (complejidad O(log n)), mientras que la
# búsqueda lineal revisa elemento por elemento desde el inicio (complejidad O(n)).
# En una lista de 1000 elementos, la binaria hace máximo ~10 comparaciones,
# mientras que la lineal puede hacer hasta 1000.
""")
