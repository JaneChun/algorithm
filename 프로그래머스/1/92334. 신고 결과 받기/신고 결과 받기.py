def solution(id_list, report, k):
    report_dict = { name : { 'count': 0, 'reporter': [] } for name in id_list }
    
    for r in report:
        reporter, reportee = r.split(' ')
        
        # 한 번만 신고 가능
        if reporter not in report_dict[reportee]['reporter']:
            report_dict[reportee]['count'] += 1
            report_dict[reportee]['reporter'].append(reporter)
        
    # count가 k 이상인 항목만 남기는 새로운 딕셔너리 생성
    filtered_dict = { name: info['reporter'] for name, info in report_dict.items() if info['count'] >= k}
    
            
    name_dict = { name : 0 for name in id_list }
    for reporterArr in filtered_dict.values():
        for reporter in reporterArr:
            name_dict[reporter] += 1
            
    return list(name_dict.values())
