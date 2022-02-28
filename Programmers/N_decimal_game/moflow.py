def replace_over_10_jinsoo(data):
    return str(data).replace("10","A").replace("11","B").replace("12","C")\
    .replace("13","D").replace("14","E").replace("15","F")
    
def make_jinsoo(n,number):
    result = "" 
    while number >= n:
        rest = number%n
        number = number//n
        if n > 10 :
            rest = replace_over_10_jinsoo(rest)
        result = str(rest) + result
    if n>10:
        number = replace_over_10_jinsoo(number)
    result = str(number) + result
    return result

def make_string(n,t,count):
    datas = ""
    for i in range(count):
        data = make_jinsoo(n,i)
        datas+=data
    return datas        

def get_one_turn(text, m, p):
    return text[p], text[m:]
    
def solution(n, t, m, p):
# n은진수, t는 출력 개수, m은 게임하는 인원, p는 내 차례
    result = ""
    p-=1
    total_string = make_string(n,t,t*m)    
    while len(result) < t:
        output, total_string = get_one_turn(total_string, m, p)
        result+=output
    return result