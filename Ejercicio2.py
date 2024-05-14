def suma_entre_cero_y_n(n):
    if n <= 0:
        return 0
    else:
        return n + suma_entre_cero_y_n(n - 1)

# Ejemplo de uso
numero = 5
print(f"La suma de todos los números enteros entre cero y {numero} es: {suma_entre_cero_y_n(numero)}")
