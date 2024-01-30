saldo = 0

while True:
    operacion = input("Ingrese la operación (D para depósito, R para retiro): ")
    
    if not operacion:
        break
    
    monto = float(input("Ingrese el monto: "))
    
    if operacion == 'D':
        saldo += monto
    elif operacion == 'R':
        saldo -= monto

print(f"Saldo final: {saldo}")
