import argparse

def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

def product(x: int, y: int) -> int:
    return x * y

def quotient(x: int, y: int) -> int:
    return x // y

def to_power(x: int, y: int) -> int:
    result = 1 
    for i in range(y):
        result *= x
    return result


def main() -> int:
    parser = argparse.ArgumentParser(prog="Calculator", description="A basic integer calculator",)
    parser.add_argument('a', 'add')
    parser.add_argument('s', 'sub')
    parser.add_argument('m', 'mul')
    parser.add_argument('d', 'div')
    
    args = parser.parse_args()

   
    if args.add:
        return add(x, y)
 

    print("Hello from basic-calculator!")


