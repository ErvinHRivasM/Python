#In this section, we programing a simple game
from os import times
import random

def run():
   number = random.randint(1,100)
   typed_number = int(input("Write a number between a 1 and 100"))
   while typed_number != number:
       if typed_number < number:
           print("Search a bigger number")
       else:
           print("Search a lower number")
       typed_number = int(input("Write other number"))
   print("You are Winner!!!")




if __name__ == '__main__':
    run()