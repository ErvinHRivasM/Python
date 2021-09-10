#In this section, we programing the searching of prime numbers

def is_prime(number):
    counter = 0
    for i in range(1,number+1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return True



def run():
   number = int(input("Write a number"))
   if is_prime(number):
       print("It's a Prime Number")
   else:
        print("It is not a Prime Number")




if __name__ == '__main__':
    run()