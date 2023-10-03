# If num divisible by 3, print fizz
# .............   by 5, print buzz
# ...............3 n 5 print fizz buzz

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print('Fizz', end=' ')
        if i % 5 == 0:
            print('Buzz', end=' ')
        if i % 3 != 0 and i % 5 != 0:
            print(i, end=' ')
    print()
