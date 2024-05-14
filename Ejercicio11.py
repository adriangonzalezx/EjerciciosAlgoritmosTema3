def invertir_numero(numero, invertido=0):
    if numero < 10:
        return invertido * 10 + numero
    else:
        ultimo_digito = numero % 10
        nuevo_numero = numero // 10
        invertido = invertido * 10 + ultimo_digito
        return invertir_numero(nuevo_numero, invertido)

# Ejemplo de uso
numero = 12345
print(f"El número {numero} invertido es: {invertir_numero(numero)}")
