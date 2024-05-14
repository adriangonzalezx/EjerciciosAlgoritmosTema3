def calcular_serie(n):
    if n == 1:
        return 1
    else:
        return 1/n + calcular_serie(n - 1)

# Ejemplo de uso
n = 5
print(f"El valor de la serie para n = {n} es: {calcular_serie(n)}")
