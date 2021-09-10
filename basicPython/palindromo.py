#In this setion, we use concepts of slices, def, conditionals, python init point and function call

def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Esm palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()