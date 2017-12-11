#Function that takes latest drow numbers and return sorted list of zeros and ones for third Q update
from get_latest_data import get_latest_combination

#Fourth Quadrant
def fourth_quadrant():
    data = get_latest_combination()
    sorted_data = data[0]
    broj_kola = data[1]
    fourth_quad = (ftq_28, ftq_29, ftq_30, ftq_31, ftq_32, ftq_33, ftq_34, ftq_35, ftq_36, ftq_37, ftq_38, ftq_39) = (28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
    #print sorted_data
    if ftq_28 in sorted_data:
        ftq_28 = 1
    else:
        ftq_28 = 0 
    if ftq_29 in sorted_data:
        ftq_29 = 1
    else:
        ftq_29 = 0
    if ftq_30 in sorted_data:
        ftq_30 = 1
    else:
        ftq_30 = 0
    if ftq_31 in sorted_data:
        ftq_31 = 1
    else:
        ftq_31 = 0
    if ftq_32 in sorted_data:
        ftq_32 = 1
    else:
        ftq_32 = 0
    if ftq_33 in sorted_data:
        ftq_33 = 1
    else:
        ftq_33 = 0
    if ftq_34 in sorted_data:
        ftq_34 = 1
    else:
        ftq_34 = 0   
    if ftq_35 in sorted_data:
        ftq_35 = 1
    else:
        ftq_35 = 0   
    if ftq_36 in sorted_data:
        ftq_36 = 1
    else:
        ftq_36 = 0   
    if ftq_37 in sorted_data:
        ftq_37 = 1
    else:
        ftq_37 = 0   
    if ftq_38 in sorted_data:
        ftq_38 = 1
    else:
        ftq_38 = 0   
    if ftq_39 in sorted_data:
        ftq_39 = 1
    else:
        ftq_39 = 0
    ftq_list = [ftq_28, ftq_29, ftq_30, ftq_31, ftq_32, ftq_33, ftq_34, ftq_35, ftq_36, ftq_37, ftq_38, ftq_39]       
    ftq_freq = ftq_list.count(1)
    ftq_list = [ftq_28, ftq_29, ftq_30, ftq_31, ftq_32, ftq_33, ftq_34, ftq_35, ftq_36, ftq_37, ftq_38, ftq_39, broj_kola, ftq_freq] 

    return ftq_list   