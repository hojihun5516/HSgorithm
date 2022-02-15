def check_shop(melody):
    if "A#" in melody:
        melody = melody.replace("A#", "H")
    if "C#" in melody:
        melody = melody.replace("C#", "I")
    if "D#" in melody:
        melody = melody.replace("D#", "J")
    if "F#" in melody:
        melody = melody.replace("F#", "K")
    if "G#" in melody:
        melody = melody.replace("G#", "L")
    return melody
    
def during_time(start_time, end_time):
    start_hour, start_minutes=start_time.split(":")
    end_hour, end_minutes=end_time.split(":")
    calc_start = int(start_hour) * 60 + int(start_minutes)
    calc_end = int(end_hour) * 60 + int(end_minutes)
    return calc_end - calc_start

def solution(m, musicinfos):
    m = check_shop(m)
    data = []
    for mu in musicinfos:
        temp = {}
        splited_data = mu.split(",")
        temp['start_time']=splited_data[0]
        temp['end_time']=splited_data[1]
        temp['title']=splited_data[2]
        temp['melody']=check_shop(splited_data[3])
        temp['during_time']=during_time(temp['start_time'], temp['end_time'])
        if temp['during_time'] < len(temp['melody']):
            temp['melody']=temp['melody'][:temp['during_time']]
        else:
            temp['melody']*=(temp['during_time']//len(temp['melody']) + 2)
        data.append(temp)
    answer = []
    answer.extend(list(filter(lambda x: m in x['melody'], data)))
    
    if len(answer) == 0:
        return "(None)"
    elif len(answer) == 1:
        return answer[0]['title']
    during_time_max=max(list(map(lambda x: x['during_time'], answer)))
    
    return list(filter(lambda x: x['during_time']==during_time_max, answer))[0]['title'] 
        
        