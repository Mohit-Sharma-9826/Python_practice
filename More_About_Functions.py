def sum(*args):   # Here args is created as a tuple of numbers passed as arguements.
    sum = 0
    for n in args:
        sum += n
    return sum

print(sum(20, 51, 64, 78, 56))


def calculate(n, **kwargs):  #Here kwargs is keyword arguements created as dictionary of arguements.
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=10, multiply=20)