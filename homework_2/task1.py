def fib(num):
    if num in [1,2]:
        return 1
    elif num == 0:
        return 0
    elif num < 0:
        return False
    return fib(num - 1) + fib(num - 2)


num = int(input('Введите число: '))
fibonacci = [fib(n) for n in range(num)]
print(fibonacci)