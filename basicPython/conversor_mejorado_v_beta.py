def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuanto pesos colombiano tienes?")
    pesos  = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+dolares+" dolares")

menu = """
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:
"""
opcion = input(menu)

if opcion == 1:
    conversor("Colombianos", 3846.40)
elif opcion == 2:
    conversor("Colombianos", 98.36)
elif opcion == 3:
    conversor("Colombianos", 16.92)
else:
    print("Elige una opción valida")