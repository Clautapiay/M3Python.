import sys 
def convertir(valor, conversiones):
    soles = valor * conversiones["Soles"]
    peso_argentino = valor * conversiones["Peso Argentino"]
    dolar_americano = valor * conversiones["Dólar Americano"]
    return soles, peso_argentino, dolar_americano

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python conversiones.py tasa_soles tasa_peso_argentino tasa_dolar_americano valor_en_pesos_chilenos")

    tasa_soles = float(sys.argv[1])
    tasa_peso_argentino = float(sys.argv[2])
    tasa_dolar_americano = float(sys.argv[3])
    valor_pesos_chilenos = float(sys.argv[4])

    conversiones = {"Soles": tasa_soles, "Peso Argentino": tasa_peso_argentino, "Dólar Americano": tasa_dolar_americano}

    valor_sol, valor_peso_argentino, valor_dolar_americano = convertir(valor_pesos_chilenos, conversiones)
    print(f"Los {valor_pesos_chilenos} pesos chilenos corresponden a:")
    print(f"{valor_sol} Soles")
    print(f"{valor_peso_argentino} Pesos Argentinos")
    print(f"{valor_dolar_americano} Dólares Americanos")