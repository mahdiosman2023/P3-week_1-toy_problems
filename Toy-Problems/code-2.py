def two_positives(a, b, c):
    positives = 0

    if a > 0:
        positives += 1

    if b > 0:
        positives += 1

    if c > 0:
        positives += 1

    return positives == 2


print(two_positives(2, 4, -3))

print(two_positives(-4, 6, 8))

print(two_positives(-3, -2, 1))

print(two_positives(4, -6, 9))

print(two_positives(-4, 6, 0))

print(two_positives(4, 6, 10))

print(two_positives(-14, -3, -4))
