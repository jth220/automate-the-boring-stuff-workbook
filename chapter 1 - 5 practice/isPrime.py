import math

def is_prime(n):
    if n <= 1:
        return False
    
    limit = (math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    
    return True


print((is_prime(54)))