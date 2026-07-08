def ChkPrime(Number):
    if Number <= 1:
        return False
    
    if Number == 2:
        return True
    
    if Number % 2 == 0:
        return False
    
    for i in range(2, Number):
        if Number % i == 0:
            return False
    
    return True