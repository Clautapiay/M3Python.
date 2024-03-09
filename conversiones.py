import sys

# Considere las siguientes tasas de conversión de Peso Chileno:
# Sol peruano: 0.0046 
# Peso Argentino: 0.093 
# Dólar Americano: 0.00013

def convertir_a_peso_chileno(soles):
    tasa_cambio = 0.0046
    cantidad_pesos_chilenos = soles * tasa_cambio
    return cantidad_pesos_chilenos

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python conversion_moneda.py cantidad_soles")
        sys.exit(1)

    soles = float(sys.argv[1])
    cantidad_pesos_chilenos = convertir_a_peso_chileno(soles)
    print(f"{soles} soles peruanos equivale a aproximadamente {cantidad_pesos_chilenos} pesos chilenos")
