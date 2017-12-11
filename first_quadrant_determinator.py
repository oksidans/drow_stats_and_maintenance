#Function takes latest drow numbers and return sorted list of zeros and ones for first Q update
from get_latest_data import get_latest_combination
import sys

#First Quadrant

get_latest_combination()

def first_quadrant():
    data = get_latest_combination()
    #If there is no data in the database breaking the script and force program to exit // to be fixed later
    if data == None:
        print "No data - Breaking the script"
        sys.exit()
    else:    
    # Breaking the tuple to get drow number and combination
        sorted_data = data[0]
        broj_kola = data[1]
    #Converting the data into quadrant to get zeros and ones
    first_quad = (fq_1, fq_2, fq_3, fq_4, fq_5, fq_6, fq_7, fq_8, fq_9) = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    if fq_1 in sorted_data:
       fq_1   = 1
    else:
        fq_1 = 0
    if fq_2 in sorted_data:
       fq_2 = 1
    else:
        fq_2 = 0
    if fq_3 in sorted_data:
        fq_3 = 1
    else:
        fq_3 = 0
    if fq_4 in sorted_data:
        fq_4 = 1
    else:
        fq_4 = 0
    if fq_5 in sorted_data:
        fq_5 = 1
    else:
        fq_5 = 0
    if fq_6 in sorted_data:
        fq_6 = 1
    else:
        fq_6 = 0
    if fq_7 in sorted_data:
        fq_7 = 1
    else:
        fq_7 = 0
    if fq_8 in sorted_data:
        fq_8 = 1
    else:
        fq_8 = 0
    if fq_9 in sorted_data:
        fq_9 = 1
    else:
        fq_9 = 0              
    fq_list = [fq_1, fq_2, fq_3, fq_4, fq_5, fq_6, fq_7, fq_8, fq_9]
    fq_freq = fq_list.count(1)
    fq_list = (fq_1, fq_2, fq_3, fq_4, fq_5, fq_6, fq_7, fq_8, fq_9, broj_kola, fq_freq)
    return fq_list



if __name__ == "__main__":
    first_quadrant()
