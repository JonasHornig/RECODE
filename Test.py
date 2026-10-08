print("Hello World!")

def MySum(a,b):
    if a < 0 or b<0:
        raise ValueError("Negative numbers")
    return a+b

def TestMySum():
    assert MySum(2,5) == 7
    assert MySum(1,1) == 2
    assert MySum(-1,1) == 0