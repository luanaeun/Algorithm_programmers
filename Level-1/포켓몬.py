def solution(arr):
    n = len(arr)//2

    res = list(set(arr))        
    
    if n < len(res):
        return n
    else:
        return len(res)