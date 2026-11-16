# Programa 2: Ordenamiento burbuja descendente
# Actividad 3 - Ordenamiento y Búsqueda en Arreglos

def bubble_sort_desc(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:  # Cambio de > a < para descendente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Solicitar datos al usuario
cantidad = int(input("Ingrese la cantidad de elementos: "))
lista = []

print(f"Ingrese {cantidad} números:")
for i in range(cantidad):
    num = float(input(f"Número {i + 1}: "))
    lista.append(num)

print("\nLista original:", lista)

lista_ordenada = bubble_sort_desc(lista.copy())
print("Lista ordenada (descendente):", lista_ordenada)
