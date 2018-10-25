# encoding:utf-8
from __future__ import division

answer2 = {'a':[1,2],'b':[2,3],'c':[3,4,5],'d':[4,5,6],'e':[6]}
answer3 = {'a':[1,2],'b':[2,3],'c':[3,4,5],'d':[5,6]}
answer4 = {'a':[6],'b':[2,3],'c':[4,5],'d':[1]}
answer6 = {'a':[5,6],'b':[1],'c':[2,3],'d':[4]}
answer7 = {'a':[1],'b':[2],'c':[3],'d':[4],'e':[5],'f':[6]}
answer8 = {'a':[1],'b':[2],'c':[3],'d':[4],'e':[5],'f':[6],'g':[6]}

def average(number_list):
    sum = 0
    for i in number_list:
        sum = sum + i
    avg = int(sum/len(number_list))
    return avg

def willingnessCalculation(A2,A3,A8):
    MA8 = average(answer8[A8])
    if average(answer2[A2]) > MA8:
        MA2 = min(answer2[A2])
    elif average(answer2[A2]) < MA8:
        MA2 = max(answer2[A2])
    else:
        MA2 = average(answer2[A2])
    if average(answer3[A3]) > MA8:
        MA3 = min(answer3[A3])
    elif average(answer3[A3]) < MA8:
        MA3 = max(answer3[A3])
    else:
        MA3 = average(answer3[A3])
    premutation = str(MA2)+str(MA3)+str(MA8)
    fp_rule = FiftyPercent(MA2,MA3,MA8)
    ra_rule = average([MA2,MA3,MA8])
    minimun = min(fp_rule,ra_rule)
    fincrp = willingnessFinalCRP(MA8,minimun)
    q2q3gap,q3q8gap,q2q8gap = gap(MA2,MA3,MA8)
    contradiction = ContradictionFlag(q2q3gap,q3q8gap,q2q8gap)
    q2color,q3color,q8color = displayColor(MA2,MA3,MA8)
    list_all = [MA2,MA3,MA8,premutation,fp_rule,ra_rule,minimun,fincrp,q2q3gap,q3q8gap,q2q8gap,contradiction,q2color,q3color,q8color]
    print list_all
    dict = {}
    dict['Q2'] = MA2
    dict['Q3'] = MA3
    dict['Q8'] = MA8
    dict['MappingPermutation'] = premutation
    dict['50%rule'] = fp_rule
    dict['RounddownAverageRule'] = ra_rule
    dict['Minimum(50%RounddownAverage)'] = minimun
    dict['FinalCRP'] = fincrp
    dict['Q2Q3Gap'] = q2q3gap
    dict['Q3Q8Gap'] = q3q8gap
    dict['Q2Q8Gap'] = q2q8gap
    dict['ContradictionFlag'] = contradiction
    dict['q2color'] = q2color
    dict['q3color'] = q3color
    dict['q8color'] = q8color
    result = dict
    return result

def FiftyPercent(MA2,MA3,MA8):
    answers_point = [MA2,MA3,MA8]
    y = 5
    while True:
        over_number = list(filter(lambda x:x>y,answers_point))
        over_count = len(over_number)
        if over_count > 1:
            fp_rule = y + 1
            break
        else:
            y -= 1
    return fp_rule

def willingnessFinalCRP(MA8,minimun):
    if MA8 == 1:
        fincrp = 1
    else:
        fincrp = minimun
    return fincrp

def gap(MA2,MA3,MA8):
    q2q3gap = max(MA2,MA3)-min(MA2,MA3)
    q3q8gap = max(MA3,MA8)-min(MA3,MA8)
    q2q8gap = max(MA2,MA8)-min(MA2,MA8)
    return q2q3gap,q3q8gap,q2q8gap

def ContradictionFlag(q2q3gap,q3q8gap,q2q8gap):
    if max(q2q3gap,q3q8gap,q2q8gap) > 1:
        contradiction = 1
    else:
        contradiction = 0
    return contradiction

def capacityCalculation(A4,A6,A7):
    MA7 = average(answer7[A7])
    if average(answer4[A4]) > MA7:
        MA4 = min(answer4[A4])
    else:
        MA4 = max(answer4[A4])
    if average(answer6[A6]) > MA7:
        MA6 = min(answer6[A6])
    else:
        MA6 = max(answer6[A6])
    premutation = str(MA4)+str(MA6)+str(MA7)
    fp_rule = FiftyPercent(MA4,MA6,MA7)
    ra_rule = average([MA4,MA6,MA7])
    minimun = min(fp_rule,ra_rule)
    finalcrp = minimun
    q4q6gap,q6q7gap,q4q7gap = gap(MA4,MA6,MA7)
    contradiction = ContradictionFlag(q4q6gap,q6q7gap,q4q7gap)
    q4color,q6color,q7color = displayColor(MA4,MA6,MA7)
    list_all = [MA4,MA6,MA7,premutation,fp_rule,ra_rule,minimun,finalcrp,q4q6gap,q6q7gap,q4q7gap,contradiction,q4color,q6color,q7color]
    print list_all
    dict = {}
    dict['Q4'] = MA4
    dict['Q6'] = MA6
    dict['Q7'] = MA7
    dict['MappingPermutation'] = premutation
    dict['50%rule'] = fp_rule
    dict['RounddownAverageRule'] = ra_rule
    dict['Minimum(50%RounddownAverage)'] = minimun
    dict['FinalCRP'] = finalcrp
    dict['Q4Q6Gap'] = q4q6gap
    dict['Q6Q7Gap'] = q6q7gap
    dict['Q4Q7Gap'] = q4q7gap
    dict['ContradictionFlag'] = contradiction
    dict['q2color'] = q4color
    dict['q3color'] = q6color
    dict['q8color'] = q7color
    result = dict
    return result


def displayColor(MA2,MA3,MA8):
    if min(MA2,MA3,MA8) == MA2 and (max(MA2,MA3,MA8)-min(MA2,MA3,MA8))> 1 :
        q2color = 'green'
    elif max(MA2,MA3,MA8) == MA2 and (max(MA2,MA3,MA8)-min(MA2,MA3,MA8)) > 1:
        q2color = 'red'
    else:
        q2color = 'black'
    if min(MA2,MA3,MA8) == MA3 and (max(MA2,MA3,MA8)-min(MA2,MA3,MA8))> 1 :
        q3color = 'green'
    elif max(MA2,MA3,MA8) == MA3 and (max(MA2,MA3,MA8)-min(MA2,MA3,MA8)) > 1:
        q3color = 'red'
    else:
        q3color = 'black'
    if min(MA2,MA3,MA8) == MA8 and (max(MA2,MA3,MA8)-min(MA2,MA3,MA8))> 1 :
        q8color = 'green'
    elif max(MA2,MA3,MA8) == MA8 and (max(MA2,MA3,MA8)-min(MA2,MA3,MA8)) > 1:
        q8color = 'red'
    else:
        q8color = 'black'
    return q2color,q3color,q8color

# willingnessCalculation('a','c','a')
# capacityCalculation('a','c','a')




