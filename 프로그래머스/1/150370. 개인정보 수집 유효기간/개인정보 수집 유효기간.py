import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    
    # datetime.datetime.strptime(date_string, format)
    # : 문자열을 지정된 형식에 맞게 datetime 객체로 변환
    today = datetime.datetime.strptime(today, '%Y.%m.%d')
    
    for index, privacy in enumerate(privacies):
        start_date, term = privacy.split(' ')
        start_date = datetime.datetime.strptime(start_date, '%Y.%m.%d')
        
        month = findTerm(term, terms)
        
        end_date = start_date + relativedelta(months = month)
        
        if end_date <= today:
            answer.append(index + 1)
    
    return answer

def findTerm(term, terms):
    for item in terms:
        [_term, num] = item.split(' ')
        if _term == term:
            return int(num)

        
    
