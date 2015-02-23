def main():
    i = 0
    n = 0
    while n < 1000:
        first = d(n)
        second = x(n)
        if first - second < 0:
            i += 1
        n += 1
    print (i)

def d(n):
    numbers = set(range(n, 1, -1))
    sum = 0
    while numbers:
        p = numbers.pop()
        sum += p
        numbers.difference_update(set(range(p*2, n+1, p)))
    return sum

def x(n):
    sum = 0
    if n % 2 == 0:
        for  i in range(n, 0, -2):
            sum += 1
    else:
        for i in range(n-1, 0, -2):
            sum += 1
    return sum

main()