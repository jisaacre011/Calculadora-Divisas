def exchange_money(budget, exchange_rate):
    """
    Convierte una cantidad de dinero (budget) usando la tasa de cambio dada.
    """
    return budget * exchange_rate


def main():
    print("=== Calculadora de Divisas ===\n")
    
    # Tasas aproximadas (USD a moneda local)
    tasas = {
        "USD": 1.00,   # Dólar estadounidense (base)
        "JPY": 157.0,   # Japón - yenes
        "MXN": 17.55,   # México - pesos mexicanos
        "EUR": 0.859,   # Alemania/Europa - euros
        "COP": 3745,    # Colombia - pesos colombianos
        "DOP": 60.0,    # República Dominicana - pesos dominicanos
        "CNY": 6.90,    # China - yuanes
        "ARS": 1200,    # Argentina - pesos argentinos
        "UAH": 42.0,    # Ucrania - grivnas
    }
    
    print("Monedas disponibles:")
    for moneda in tasas:
        print(f"  - {moneda}")
    
    # Seleccionar moneda de origen
    while True:
        moneda_origen = input("\n¿De qué moneda partes? → ").upper()
        if moneda_origen in tasas:
            break
        print("Moneda no reconocida. Intenta de nuevo.")
    
    # Seleccionar moneda de destino
    while True:
        moneda_destino = input("¿A qué moneda quieres convertir? → ").upper()
        if moneda_destino in tasas:
            break
        print("Moneda no reconocida. Intenta de nuevo.")
    
    # Cantidad a cambiar
    try:
        cantidad = float(input(f"¿Cuántos {moneda_origen} quieres cambiar? → "))
    except ValueError:
        print("Ingresa un número válido.")
        return
    
    # Calcular conversión
    if moneda_origen == "USD":
        tasa = tasas[moneda_destino]
        resultado = exchange_money(cantidad, tasa)
        print(f"\n{ cantidad:,.2f} {moneda_origen} = {resultado:,.2f} {moneda_destino}")
    
    elif moneda_destino == "USD":
        tasa = 1 / tasas[moneda_origen]
        resultado = exchange_money(cantidad, tasa)
        print(f"\n{ cantidad:,.2f} {moneda_origen} = {resultado:,.2f} USD")
    
    else:
        cantidad_en_usd = cantidad / tasas[moneda_origen]
        resultado = cantidad_en_usd * tasas[moneda_destino]
        print(f"\n{ cantidad:,.2f} {moneda_origen} = {resultado:,.2f} {moneda_destino}")


if __name__ == "__main__":
    main()