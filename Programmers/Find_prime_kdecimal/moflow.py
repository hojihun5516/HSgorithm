import math

def convert_code(n,k):
    converted = ""
    share = 1000001
    remainder = 0

    while k<share:
        share = n//k
        remainder = n%k
        converted = str(remainder) + converted
        n = share
    converted = str(n)+converted
    return converted


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    converted = convert_code(n,k)
    data_arr = converted.split('0')
    data_arr = list(filter(lambda x:x!="", data_arr))
    data_arr = list(map(lambda x:int(x), data_arr))
    data_arr = list(filter(lambda x:x!=1, data_arr))
    prime_data_arr = list(filter(lambda x:is_prime_num(x), data_arr))
    
    result = len(prime_data_arr)
    return result