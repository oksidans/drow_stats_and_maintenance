#Function that takes latest drow numbers and return sorted list of zeros and ones for second Q update
from get_latest_data import get_latest_combination



#Second Quadrant
def second_quadrant():
    data = get_latest_combination()
    sorted_data = data[0]
    broj_kola = data[1]
    second_quad = (sq_10, sq_11, sq_12, sq_13, sq_14, sq_15, sq_16, sq_17, sq_18) = (10, 11, 12, 13, 14, 15, 16, 17, 18)
    #print sorted_data
    if sq_10 in sorted_data:
        sq_10 = 1
    else:
        sq_10 = 0
    if sq_11 in sorted_data:
        sq_11 = 1
    else:
        sq_11 = 0
    if sq_12 in sorted_data:
        sq_12 = 1
    else:
        sq_12 = 0
    if sq_13 in sorted_data:
        sq_13 = 1
    else:
        sq_13 = 0
    if sq_14 in sorted_data:
        sq_14 = 1
    else:
        sq_14 = 0
    if sq_16 in sorted_data:
        sq_15 = 1
    else:
        sq_15 = 0
    if sq_16 in sorted_data:
        sq_16 = 1
    else:
        sq_16 = 0
    if sq_17 in sorted_data:
        sq_17 = 1
    else:
        sq_17 = 0
    if sq_18 in sorted_data:
        sq_18 = 1
    else:
        sq_18 = 0

    sq_list = [sq_10,sq_11, sq_12, sq_13, sq_14, sq_15, sq_16, sq_17, sq_18 ]
    sq_freq = sq_list.count(1)
    sq_list = [sq_10,sq_11, sq_12, sq_13, sq_14, sq_15, sq_16, sq_17, sq_18, broj_kola, sq_freq ]
    return sq_list


if __name__ == "__main__":
    second_quadrant()