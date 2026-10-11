meyveler = ["elma", "muz", "çilek"]

it = iter(meyveler)

print(next(it))
print(next(it))

meyveler = ["elma", "muz", "çilek"]

it = iter(meyveler)

print(next(it))
print(next(it))
print(next(it))
#print(next(it))  # StopIteration hatası verir

sayilar = [1, 2, 3] 
def sayilar():
    yield 1
    yield 2
    yield 3
it = sayilar()
print(next(it))
print(next(it))
print(next(it))

def say():
    for i in range(5):
        yield i

it = say()

print(next(it))
print(next(it))

