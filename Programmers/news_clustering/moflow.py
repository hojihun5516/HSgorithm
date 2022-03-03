import collections

def check_english(data):
    if (65 <= ord(data) and 90 >= ord(data))\
    or (97 <= ord(data) and 122 >= ord(data)):
        return True
    return False

def split_data(data):
    result = []
    for i in range(len(data)-1):
        if check_english(data[i]) and check_english(data[i+1]):
            result.append(data[i].upper()+data[i+1].upper())
    return result

def solution(str1, str2):
    data1 = split_data(str1)
    data2 = split_data(str2)
    data1=collections.Counter(data1)
    data2=collections.Counter(data2)
    bottom = 0
    up = 0
    for k,v in data1.items():
        data2_v = 0
        if k in data2:
            up+=min(v, data2[k])
            data2_v = data2[k]
        bottom+=max(v, data2_v)
    
    data2_least = data2.keys() - data1.keys()
    if data2_least:
        for d2 in data2_least:
            bottom+=data2[d2]
    
    if bottom==0:
        return 65536
    if up ==0:
        return 0
    
    answer = up/bottom
    if answer == 0:
        return 65536
    else:
        return int(answer*65536)