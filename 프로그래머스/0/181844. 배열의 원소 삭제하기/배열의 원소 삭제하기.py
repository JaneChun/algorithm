def solution(arr, delete_list):
    # return list(filter(lambda num: num not in delete_list, arr))
    return list(filter(lambda num: not num in delete_list, arr))