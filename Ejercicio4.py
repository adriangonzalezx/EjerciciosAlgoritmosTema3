def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente > 0:
        return base * potencia(base, exponente - 1)
    elif exponente < 0:
        return 1 / (base * potencia(base, -exponente - 1))

# Ejemplo de uso
base = 2
exponente = 3
print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")
