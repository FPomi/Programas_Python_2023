import sys

def fibonacciNoRecursivo(n: int) -> int:
    fibonacci = [0, 1]
  
    if (n >= 2):
        for posicion in range(2, n+1):
            fibonacci.append(fibonacci[posicion-1] + fibonacci[posicion-2])

    return fibonacci[n]


if __name__ == '__main__':
    x = int(input())
    print(fibonacciNoRecursivo(x))