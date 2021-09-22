# Python code
# Use print("messages...") to debug your solution.

class A():
    def test(self):
        print("A")
    
    def __init__(self):
        self.test()
        

class B(A):
    def __init__(self):
        self.test()




# Python code
# Use print("messages...") to debug your solution.

def average(table):
    # Your code goes here
    value = 0
    counter = 0
    for i in table:
        value =  value + i
        counter += 1

    value = value/counter

    return value




# Python code
# Use print("messages...") to debug your solution.

def is_bool(i, j):
    # Your code goes here
    if i == 1 or j ==1 or ((i+j) == 1):
        return True
    return False


