from flask import Flask
from flask_restful import Api, Resource, reqparse
def appearance(intervals):
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    p = 0
    t = 0
    summ = 0
    while True:
        left_border = max([lesson[0], pupil[p], tutor[t]])
        right_border = min([lesson[1], pupil[p + 1], tutor[t + 1]])
        if(right_border - left_border >= 0):
            #print("GO!!!")
            summ += right_border - left_border
            if(pupil[p + 1] > tutor[t + 1]):
                t += 2
            elif pupil[p + 1] < tutor[t + 1]:
                p += 2
            else:
                t += 2
                p += 2
        else:
            if pupil[p + 1] < left_border:
                p += 2
            if tutor[t + 1] < left_border:
                t += 2
        if p == len(pupil) or t == len(tutor):
            break
    return summ
    
    pass
tests = [
   {'data': {'lesson': [3200, 6800],
             'pupil': [3340, 3389, 3390, 3395, 3396, 6472],
             'tutor': [3290, 3430, 3443, 6473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]
    
for i, test in enumerate(tests):
    test_answer = appearance(test['data'])
    message = "Error on test case " + str(i) + ", got " + str(test_answer) + ", expected " + str(test["answer"])
    assert test_answer == test['answer'], message
    
