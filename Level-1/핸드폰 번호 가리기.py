def hide_number(number):
    return (len(number)-4)*'*' + number[-4:]
    
print("결과 : " + hide_number('01012345555'))
