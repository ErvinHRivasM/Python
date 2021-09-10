"""
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:
"""
opcion = input("¿Cuanto pesos colombiano tienes?")

if opcion == 1:
    pesos = input("¿Cuanto pesos colombiano tienes?")
    pesos  = float(pesos)
    valor_dolar = 3846.40
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+dolares+" dolares")
elif opcion == 2:
    pesos = input("¿Cuanto pesos Argentinos tienes?")
    pesos  = float(pesos)
    valor_dolar = 98.10
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+dolares+" dolares")
elif opcion == 3:
    pesos = input("¿Cuanto pesos Mexicanos tienes?")
    pesos  = float(pesos)
    valor_dolar = 19.87
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+dolares+" dolares")
else:
    print("Elige una opción valida")