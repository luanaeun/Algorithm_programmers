def solution(a, b):
    month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_list = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    total_day = sum(month_list[:a-1]) + b
    result = day_list[total_day % 7]

    return result

print(solution(5, 24))