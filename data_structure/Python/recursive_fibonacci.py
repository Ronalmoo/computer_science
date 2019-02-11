def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    n = 10
    for i in range(n, n + 1):
        print(fibonacci(i))
