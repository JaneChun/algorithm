import math

def solution(fees, records):
    answer = []
    [base_time, base_fee, per_time, per_fee] = fees
    
    car_dict = {}
    
    for record in records:
        [time, car_num, action] = record.split(' ')
        car_dict.setdefault(car_num, []).append([time, action]) # car_num 키가 car_dict에 없을 경우 []를 기본값으로 추가하고 이후 append를 사용해 값을 추가한다.
        
    # 출차 안한 경우 추가
    for car_num, record_array in car_dict.items():
        if len(record_array) % 2 != 0:
            record_array.append(['23:59', 'OUT'])
        
        # 총 주차 시간 계산
        total_time = 0
        for i in range(0, len(record_array), 2):
            [[in_time, _], [out_time, _]] = record_array[i:i + 2]
            
            in_time = transform_to_min(in_time)
            out_time = transform_to_min(out_time)
            
            total_time += (out_time - in_time)
        
        total_fee = calculate_total_fee(base_time, base_fee, per_time, per_fee, total_time)
        answer.append([car_num, total_fee])
    
    sorted_answer = sorted(answer, key=lambda x: x[0])
    return [val for _, val in sorted_answer]

def transform_to_min(HHMMstr):
    [h, m] = HHMMstr.split(':')
    return int(h) * 60 + int(m)

def calculate_total_fee(base_time, base_fee, per_time, per_fee, total_time):
    charged_time = max(0, total_time - base_time)
    return base_fee + math.ceil(charged_time / per_time) * per_fee