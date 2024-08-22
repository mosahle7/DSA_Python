
def sameEles(arr):
    m = max(arr)
    twos, ones = 0, 0
    
    for num in arr:
        d = m - num
        twos += d // 2
        ones += d % 2
    
    # Adjust the twos and ones if possible to minimize generations
    if twos > ones + 1:
        adjust = (twos - ones) // 2
        ones += adjust * 2
        twos -= adjust
    
    elif ones > twos + 1:
        adjust = (ones - twos) // 2
        twos += adjust
        ones -= adjust * 2
    
    # Calculate the minimum number of generations
    generations = 0
    
    while twos > 0 or ones > 0:
        generations += 1
        if generations % 2 == 1:  # Odd generation
            if ones > 0:
                ones -= 1
        else:  # Even generation
            if twos > 0:
                twos -= 1
    
    return generations
