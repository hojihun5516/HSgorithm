def calc_time_to_minutes(data):
    hours, minutes = data.split(":")
    
    minutes= int(minutes) + int(hours)*60
    return minutes

def solution(fees, records):
    default_minutes = fees[0]
    default_price = fees[1]
    over_minutes = fees[2]
    over_price = fees[3]

    in_cars = {}
    out_cars = {}
    total_time = {}
    total_fee = {}
    
    for record in records:
        re = record.split(" ")
        if re[2] == "IN":
            if in_cars.get(re[1]):
                in_cars[re[1]].append(re[0])
            else:
                in_cars[re[1]] = [re[0]]
        else:
            if out_cars.get(re[1]):
                out_cars[re[1]].append(re[0])
            else:
                out_cars[re[1]] = [re[0]]
    # 갯수 안맞는거 맞춰줌
    for in_car_number, time in in_cars.items():
        if not out_cars.get(in_car_number):
            out_cars[in_car_number]=["23:59"]
        if len(out_cars[in_car_number]) != len(time):
            out_cars[in_car_number].append("23:59")
    # 비용계산
    for k,v in in_cars.items():
        for i,in_time in enumerate(v):
            calc_time = calc_time_to_minutes(out_cars[k][i]) - calc_time_to_minutes(in_time)
            if total_time.get(k):
                total_time[k]+=calc_time
            else:
                total_time[k]=calc_time
    
    for car_number,time in total_time.items():
        if time <= default_minutes:
            total_fee[car_number] = default_price
        else:
            spend_time = time - default_minutes
            fee = default_price
            fee += ((spend_time // over_minutes) * over_price)
            if spend_time % over_minutes !=0:
                fee+=over_price
            total_fee[car_number] = fee
    total_fee = sorted(total_fee.items())
    answer = [fee[1] for fee in total_fee]
    return answer

    
    
    