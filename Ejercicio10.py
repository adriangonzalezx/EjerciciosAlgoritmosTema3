def contar_digitos(numero):
    if abs(numero) < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

# Ejemplo de uso
numero = 12345
print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")
