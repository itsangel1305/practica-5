num = int(input("Ingrese un número entero positivo: "))

cuenta_atras = [str(i) for i in range(num, -1, -1)]
resultado = ', '.join(cuenta_atras)

print(resultado)
