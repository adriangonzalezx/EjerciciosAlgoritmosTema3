def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        cociente = n // 2
        residuo = n % 2
        return decimal_a_binario(cociente) + str(residuo)

# Ejemplo de uso
numero_decimal = 19
print(f"El número decimal {numero_decimal} en sistema binario es: {decimal_a_binario(numero_decimal)}")
