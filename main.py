def fibonacci(p):
    a, b = 0, 1
    primos = []

    def primo(n):
        if n % 1 == 0 and n % n == 0 and not n % 2 == 0:
            return n
    while True:
        a, b = b, a+b
        if primo(a) is not None and primo(a) != 1:
            primos.append(a)

        if len(primos) == p:
            break
    return primos


print(fibonacci(5))
print(sum(fibonacci(5))/5)








