import itertools

def make_arr(expression):
    arr = []
    temp_num = ""
    for i in range(len(expression)):
        if expression[i].isdigit():
            temp_num+=expression[i]
        else:
            arr.append(temp_num)
            temp_num=""
            arr.append(expression[i])
    arr.append(temp_num)
    return arr

def calc(mapping, arrs):
    arr = arrs[:]
    for m in mapping:
        stack = []
        while len(arr)!=0:
            temp = arr.pop(0)
            if temp == m:
                before_data = stack.pop()
                calc_expression = eval(before_data+temp+arr.pop(0))
                stack.append(str(calc_expression))
            else:
                stack.append(temp)
        arr = stack
    return abs(int(arr[0]))

def solution(expression):
    # 수식은 세개
    mappings = ['+','*','-']
    mappings = list(itertools.permutations(mappings))
    expression = make_arr(expression)
    answer = []
    for mapping in mappings:
        answer.append(calc(mapping, expression))
    return max(answer)