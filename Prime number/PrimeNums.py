# Author:    Mahdi Safarian
# Date:      04/20/20
# Subject:   Finde Prime Numbers.

import math

def is_prime(number):

    if number < 2 : 
        return False

    if number % 2 == 0 : 
        return number == 2

    root = (int)(math.sqrt(number))+1

    for i in range (3,root,2) : 
        if number % i == 0 : 
            return False

    return True
 
result = is_prime(int(input('enter number : ')))

if result :
    print('number is prime')
else :
    print('number is Not prime') 

