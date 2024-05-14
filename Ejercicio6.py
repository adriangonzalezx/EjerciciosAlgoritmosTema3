def invertir_secuencia(secuencia):
    if len(secuencia) <= 1:
        return secuencia
    else:
        return secuencia[-1] + invertir_secuencia(secuencia[:-1])

# Ejemplo de uso
cadena = "Hola Mundo"
print("La secuencia invertida es:", invertir_secuencia(cadena))
