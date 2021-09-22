import sys
import math
from contextlib import redirect_stdout


def translate(text):
    word = ""
    counter = 0
    lista = ["a", "e", "i", "o", "u"]

    for i in text:
        if counter == 0 and (i in lista):
            word= word + "av" + i
            counter = 1
        else:
             word= word +i
             counter = 0
    return word


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    text = input()
    with redirect_stdout(sys.stderr):
        javanais = translate(text)
    print(javanais)


if __name__ == "__main__":
    main()
