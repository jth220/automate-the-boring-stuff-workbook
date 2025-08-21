def average(n):
    if not n:
        raise Exception("Can't be an empty list")
    return sum(n) / len(n)

