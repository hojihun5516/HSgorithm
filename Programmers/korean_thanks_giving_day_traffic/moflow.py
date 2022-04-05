def make_start_time_end_time(time, during):
    during = during.replace("s","")
    hours, minutes, seconds = time.split(":")

    hours = float(hours) * 60 * 60 * 1000
    minutes = float(minutes) * 60 * 1000
    seconds = float(seconds) * 1000
    during = float(during) * 1000 - 1

    end_time = int(hours+minutes+seconds)
    start_time = int(end_time - during)
    
    return start_time, end_time
    
def count_request(requests, start_time, end_time):
    count=0
    for request in requests:
        if request[1] < start_time or request[0] > end_time:
            pass
        else:
            count+=1
    return count

def solution(lines):
    answer=[]
    requests = []
    for line in lines:
        day,time,during=line.split(" ")
        start_time, end_time = make_start_time_end_time(time, during)
        requests.append([start_time,end_time])
    
    for request in requests:
        answer.append(count_request(requests, request[0], request[0]+999))
        answer.append(count_request(requests, request[1], request[1]+999))
    answer = max(answer)
    return answer