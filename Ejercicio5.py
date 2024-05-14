def romano_a_decimal(romano, valores_romanos={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}):
    if len(romano) == 0:
        return 0
    elif len(romano) == 1:
        return valores_romanos[romano[0]]
    else:
        if valores_romanos[romano[0]] < valores_romanos[romano[1]]:
            return -valores_romanos[romano[0]] + romano_a_decimal(romano[1:])
        else:
            return valores_romanos[romano[0]] + romano_a_decimal(romano[1:])

# Ejemplo de uso
numero_romano = "XIV"
print(f"El número romano {numero_romano} es igual a {romano_a_decimal(numero_romano)} en decimal.")
