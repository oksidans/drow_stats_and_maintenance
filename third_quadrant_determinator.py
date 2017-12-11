#Function that takes latest drow numbers and return sorted list of zeros and ones for third Q update
from get_latest_data import get_latest_combination




#Third Quadrant
def third_quadrant():
    data = get_latest_combination()
    sorted_data = data[0]
    broj_kola = data[1]
    third_quad = (tq_19, tq_20, tq_21, tq_22, tq_23, tq_24, tq_25, tq_26, tq_27) = (19, 20, 21, 22, 23, 24, 25, 26, 27)
    
    if tq_19 in sorted_data:
        tq_19 = 1
    else:
        tq_19 = 0
    if tq_20 in sorted_data:
        tq_20 = 1
    else:
        tq_20 = 0
    if tq_21 in sorted_data:
        tq_21 = 1
    else:
        tq_21 = 0
    if tq_22 in sorted_data:
        tq_22 = 1
    else:
        tq_22 = 0
    if tq_23 in sorted_data:
        tq_23 = 1
    else:
        tq_23 = 0
    if tq_24 in sorted_data:
        tq_24 = 1
    else:
        tq_24 = 0
    if tq_25 in sorted_data:
        tq_25 = 1
    else:
        tq_25 = 0
    if tq_26 in sorted_data:
        tq_26 = 1
    else:
        tq_26 = 0
    if tq_27 in sorted_data:
        tq_27 = 1
    else:
        tq_27 = 0
    tq_list = [tq_19, tq_20, tq_21, tq_22, tq_23, tq_24, tq_25, tq_26, tq_27]
    tq_freq = tq_list.count(1)
    tq_list =  [tq_19, tq_20, tq_21, tq_22, tq_23, tq_24, tq_25, tq_26, tq_27, broj_kola, tq_freq]      
    return tq_list  