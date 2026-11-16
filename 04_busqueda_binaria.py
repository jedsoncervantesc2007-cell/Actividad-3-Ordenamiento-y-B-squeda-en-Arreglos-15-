# Programa 4: Búsqueda binaria
# Actividad 3 - Ordenamiento y Búsqueda en Arreglos

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No encontrado

# Solicitar datos al usuario
cantidad = int(input("Ingrese la cantidad de elementos: "))
lista = []

print(f"Ingrese {cantidad} números:")
for i in range(cantidad):
    num = float(input(f"Número {i + 1}: "))
    lista.append(num)

# Ordenar la lista (se permite usar sort())
lista.sort()
print("\nLista ordenada:", lista)

objetivo = float(input("Ingrese el número a buscar: "))

posicion = busqueda_binaria(lista, objetivo)

if posicion != -1:
    print(f"El número {objetivo} se encuentra en la posición {posicion}")
else:
    print(f"El número {objetivo} NO se encuentra en la lista")
