import math

def tables_needed(people, seats):
    return math.ceil(people / seats)

def welcome(name):
    return f"Welcome to PLP, {name}!"

if __name__ == "__main__":
    print(tables_needed(10, 4))
    print(tables_needed(20, 6))
    print(welcome("Adelai"))