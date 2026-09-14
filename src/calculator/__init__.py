import argparse
from os import wait


def main() -> None:
    parser = argparse.ArgumentParser(prog="Calculator", description="A basic integer calculator",)
    parser.add_argument('-a', '--add', action="store_true")
    parser.add_argument('-s', '--sub', action="store_true")
    parser.add_argument('-m', '--mul')
    parser.add_argument('-d', '--div')
    parser.add_argument('x', type=int, help="The first number you want to use in your calculation")
    parser.add_argument('y', type=int, help="The second number you want to use in your calculation")
    
    args = parser.parse_args()

   


    print("Hello from basic-calculator!")
    def add(x: int, y: int) -> int:
        return args.x + args.y

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

    if args.add:
        ans = add(args.x, args.y)
        print(str(ans))
        print(args)
    
    if args.sub:
        ans = subtract(args.x, args.y)
        print(str(ans))



