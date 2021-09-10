#In this setion, we use concepts of bucles, constant variable, python point entry, counter how control variable
#and mathematics term how 

def run():
    LIMIT = 1000

    counter = 0
    potency_2 =2**counter
    while potency_2 < LIMIT:
        print("2 elevado a "+str(counter)+" es igual a: "+str(potency_2))
        counter = counter + 1
        #counter += 1 
        # other wave of write it#
        potency_2 = 2**counter



if __name__ == '__main__':
    run()