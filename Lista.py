# Creación de una lista
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Imprime: [1, 2, 3, 4, 5]

# Acceso a elementos de la lista
print(my_list[0])   # Imprime: 1 (primer elemento)
print(my_list[-1])  # Imprime: 5 (último elemento)

# Modificación de elementos de la lista
my_list[0] = 10
print(my_list)      # Imprime: [10, 2, 3, 4, 5]

# Adición de elementos a la lista
my_list.append(6)
print(my_list)      # Imprime: [10, 2, 3, 4, 5, 6]

# Eliminación de elementos de la lista
my_list.remove(4)
print(my_list)      # Imprime: [10, 2, 3, 5, 6]

# Otras operaciones comunes
print(len(my_list))             # Imprime: 5 (longitud de la lista)
print(3 in my_list)             # Imprime: True (verifica si 3 está en la lista)
print(my_list.index(5))         # Imprime: 3 (índice del primer 5 encontrado)
my_list.reverse()
print(my_list)                  # Imprime: [6, 5, 3, 2, 10] (lista invertida)
