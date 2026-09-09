def main() -> None:
    print("Hello from basic-calculator!")

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
