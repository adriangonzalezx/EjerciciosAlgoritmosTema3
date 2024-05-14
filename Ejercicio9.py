def logaritmo_entero(n, b):
    if n < b:
        return 0
    else:
        cociente = n // b
        return 1 + logaritmo_entero(cociente, b)

# Ejemplo de uso
n = 16
b = 2
print(f"El logaritmo entero de {n} en base {b} es: {logaritmo_entero(n, b)}")
