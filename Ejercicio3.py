def producto(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + producto(a, b - 1)
    elif b < 0:
        return -producto(a, -b)

# Ejemplo de uso
num1 = 5
num2 = -3
print(f"El producto de {num1} y {num2} es: {producto(num1, num2)}")
