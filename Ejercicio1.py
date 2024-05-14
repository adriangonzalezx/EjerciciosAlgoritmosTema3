def fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor que 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso
num = 10
print(f"El valor en la sucesión de Fibonacci para {num} es: {fibonacci(num)}")
