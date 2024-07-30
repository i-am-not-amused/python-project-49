import random


def get_gcd(a: int, b: int):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return max(a, b)


def generate_gcd():
    num1, num2, gcd = 0, 0, 0
    while gcd < 2:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        gcd = get_gcd(num1, num2)
    return f"{num1} {num2}", gcd
