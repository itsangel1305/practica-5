base = int(input("Ingrese la cantidad de asteriscos en la base del árbol: "))

altura = 1
while altura <= base:
    espacios = ' ' * (base - altura)
    asteriscos = '*' * (2 * altura - 1)
    print(espacios + asteriscos)
    altura += 1
