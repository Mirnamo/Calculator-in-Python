#what I need in the api
"""
1. reset function to set the calculator to zero
2. add function
3. round up function
4. trig function (in scientific version)
5. division function
6. multiplication function
7. pow function 
8. root function
9. substraction function
9. remainder function (in scientific version)
10. log function (in scientific version)
11. ln function (in scienctific version)
12. abs function (in scientific function)

"""

import math


# def reset():
#     return 0.0

def add(num1, num2):
    return num1 + num2

def roundup(num):
    return round(num)

#trig functions
def sin(x):
    return math.sin(x)
    
def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def inverse_sin(x):
    if not x > -1 and x < 1:
        raise ValueError("Math error")
    return math.asin(x)

def inverse_cos(x):
    if not x > -1 and x < 1:
        raise ValueError("Math error")
    return math.acos(x)

def inverse_tan(x):
    if not x > -1 and x < 1:
        raise ValueError("Math error")
    return math.atan(x)

def sec(x):
    return 1/cos(x)

def cosc(x):
    return 1/sin(x)

def cotg(x):
    return 1/tan(x)

#division function
def division(numerator, denominator):
    if denominator == 0:
        raise ValueError("Math error")
    return numerator/denominator

#multiplication
def multiplication(num1, num2):
    return num1 * num2

def pow(num, power):
    if power == 0:
        return 1
    if num == 0:
        return 0
    if power < 0:
        power = power*-1
        result = 1
        while power > 0:
            result *= num
            power -=1
        return 1/result
    else:
        result = 1
        while power > 0:
            result *= num
            power -=1
        return result
    


#root function
def root(num, root_power):
    if root_power == 0:
        raise ValueError("Math error")
    if num < 0 and abs(root_power) % 2 == 0:
        raise ValueError("Math error")
    
    if root_power < 0:
        root_power = root_power*-1
        power = 1/root_power
        return 1.0/(num**power)
    
    power = 1/root_power

    return num ** power

#substraction
def substraction(num1, num2):

    return num1 - num2

#absolute function
def absolute(num):
    if(num < 0):
        return num * -1
    else:
        return num

#remainder function
def remainder(num, mod):
    return num % mod

#log function, set base by default 10 if user didn't put any
def log(num, base = 10):
    #check domain of base
    if base < 1 and num <= 0:
        raise ValueError("Math error")
    #log 1 is 0 
    if num == 1:
        return 0.0
    #calculate log normally
    if base == num:
        return 1.0
    
    result = 0

    while num >= base:
        result += 1
        num /= base

    fractional_part = 0
    increment = 1 / base
    while num < 1:
        fractional_part += increment
        num *= base

    result += fractional_part

    return result

def ln(num):

    base = math.e

    return log(num, base)