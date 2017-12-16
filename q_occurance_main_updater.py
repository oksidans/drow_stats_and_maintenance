import mysql.connector
import os
import sys
from connections import connect_db
import decimal
from queries import fq_1_query, fq_2_query, fq_3_query, fq_4_query, fq_5_query, fq_6_query, fq_7_query, fq_8_query, fq_9_query, sq_10_query,sq_11_query, sq_12_query, sq_13_query, sq_14_query, sq_15_query, sq_16_query, sq_17_query, sq_18_query, tq_19_query, tq_20_query, tq_21_query, tq_22_query, tq_23_query, tq_24_query, tq_25_query, tq_26_query, tq_27_query




#Get the data from the database quering first quadrant and counting total number of  occurance of the first number in quadrant - returns fq_1_total as integer
def count_q_1(total):
    total_fq_1 = fq_1_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_1_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_1_total in number:
        return fq_1_total

#Get the data from the database quering first quadrant and counting total number of  occurance of the 2 number in quadrant - returns fq_2_total as integer
def count_q_2(total):
    total_fq_2 = fq_2_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_2_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_2_total in number:
        return fq_2_total

#Get the data from the database quering first quadrant and counting total number of  occurance of the 3 number in quadrant - returns fq_3_total as integer
def count_q_3(total):
    total_fq_3 = fq_3_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_3_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_3_total in number:
        return fq_3_total

#Get the data from the database quering first quadrant and counting total number of  occurance of the 4 number in quadrant - returns fq_4_total as integer
def count_q_4(total):
    total_fq_4 = fq_4_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_4_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_4_total in number:
        return fq_4_total

#Get the data from the database quering first quadrant and counting total number of  occurance of the 5 number in quadrant - returns fq_5_total as integer
def count_q_5(total):
    total_fq_5 = fq_5_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_5_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_5_total in number:
        return fq_5_total

    #Get the data from the database quering first quadrant and counting total number of  occurance of the 6 number in quadrant - returns fq_6_total as integer
def count_q_6(total):
    total_fq_6 = fq_6_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_6_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_6_total in number:
        return fq_6_total

    #Get the data from the database quering first quadrant and counting total number of  occurance of the 7 number in quadrant - returns fq_7_total as integer
def count_q_7(total):
    total_fq_7 = fq_7_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_7_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_7_total in number:
        return fq_7_total


    #Get the data from the database quering first quadrant and counting total number of  occurance of the 8 number in quadrant - returns fq_8_total as integer
def count_q_8(total):
    total_fq_8 = fq_8_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_8_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_8_total in number:
        return fq_8_total
#Get the data from the database quering first quadrant and counting total number of  occurance of the 9 number in quadrant - returns fq_9_total as integer
def count_q_9(total):
    total_fq_9 = fq_9_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(fq_9_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for fq_9_total in number:
        return fq_9_total

#update first Q in main table update total number of occurance, positive weight and negative weight
def first_Q_main_update():
    connection = connect_db()
    cursor = connection.cursor()

    total_no_of_occurance = [count_q_1(fq_1_query), count_q_2(fq_2_query), count_q_3(fq_3_query), count_q_4(fq_4_query), count_q_5(fq_5_query), count_q_6(fq_6_query), count_q_7(fq_7_query), count_q_8(fq_8_query), count_q_9(fq_9_query)]
    
    positive_weight = [(count_q_1(fq_1_query)/float(19))*100,(count_q_2(fq_2_query)/float(19))*100,(count_q_3(fq_3_query)/float(19))*100,(count_q_4(fq_4_query)/float(19))*100,(count_q_5(fq_5_query)/float(19))*100,(count_q_6(fq_6_query)/float(19))*100,(count_q_7(fq_7_query)/float(19))*100,(count_q_8(fq_8_query)/float(19))*100,(count_q_9(fq_9_query)/float(19))*100]

    negative_weight = [(100 -(count_q_1(fq_1_query)/float(19))*100),(100 -(count_q_2(fq_2_query)/float(19))*100),(100 -(count_q_3(fq_3_query)/float(19))*100),(100 -(count_q_4(fq_4_query)/float(19))*100),(100 -(count_q_5(fq_5_query)/float(19))*100),(100 -(count_q_6(fq_6_query)/float(19))*100),(100 -(count_q_7(fq_7_query)/float(19))*100),(100 -(count_q_8(fq_8_query)/float(19))*100),(100 -(count_q_9(fq_9_query)/float(19))*100)]
       
    id = [1,2,3,4,5,6,7,8,9]


    for i in range(0,len(id),1):
        a = '(' + str(id[i]) + ',' + str(total_no_of_occurance[i]) + ',' + str(positive_weight[i]) + ',' + str(negative_weight[i]) + ')'
        b = ''
        c = ''
        d = ''
        if i < (len(id)-1):
            c = c + a + b + d
            #print c
        else:
            c += a + b
    
        print c
        update_cell = ("INSERT INTO main (id, total_no_of_occurance, positive_weight, negative_weight)"
                          "VALUES %s" % c +
                      "ON DUPLICATE KEY UPDATE "
                      "total_no_of_occurance=VALUES(total_no_of_occurance), "
                      "positive_weight=VALUES(positive_weight),"
                      "negative_weight=VALUES(negative_weight)"
                          ";")
        cursor.execute(update_cell)
          
        connection.commit()
    connection.close()


#SECOND QUADRANT - Update main table - populate total number of occurance, positive weight and negative weight 

#Get the data from the database quering second quadrant and counting total number of  occurance of the first number in quadrant - returns sq_10_total as integer
def count_sq_10(total):
    total_sq_10 = sq_10_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_10_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_10_total in number:
        return sq_10_total

#Get the data from the database quering second quadrant and counting total number of  occurance of the 2 number in quadrant - returns sq_11_total as integer
def count_sq_11(total):
    total_sq_11 = sq_11_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_11_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_11_total in number:
        return sq_11_total

#Get the data from the database quering second quadrant and counting total number of  occurance of the 3 number in quadrant - returns sq_12_total as integer
def count_sq_12(total):
    total_sq_12 = sq_12_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_12_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_12_total in number:
        return sq_12_total

#Get the data from the database quering second quadrant and counting total number of  occurance of the 4 number in quadrant - returns sq_13_total as integer
def count_sq_13(total):
    total_sq_13 = sq_13_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_13_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_13_total in number:
        return sq_13_total

#Get the data from the database quering second quadrant and counting total number of  occurance of the 5 number in quadrant - returns sq_14_total as integer
def count_sq_14(total):
    total_sq_14 = sq_14_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_14_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_14_total in number:
        return sq_14_total

    #Get the data from the database quering second quadrant and counting total number of  occurance of the 6 number in quadrant - returns sq_15_total as integer
def count_sq_15(total):
    total_sq_15 = sq_15_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_15_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_15_total in number:
        return sq_15_total

    #Get the data from the database quering second quadrant and counting total number of  occurance of the 7 number in quadrant - returns sq_16_total as integer
def count_sq_16(total):
    total_sq_16 = sq_16_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_16_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_16_total in number:
        return sq_16_total


    #Get the data from the database quering second quadrant and counting total number of  occurance of the 8 number in quadrant - returns sq_17_total as integer
def count_sq_17(total):
    total_sq_17 = sq_17_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_17_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_17_total in number:
        return sq_17_total
#Get the data from the database quering second quadrant and counting total number of  occurance of the 9 number in quadrant - returns sq_18_total as integer
def count_sq_18(total):
    total_sq_18 = sq_18_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(sq_18_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for sq_18_total in number:
        return sq_18_total

#update SECOND Q in main table update total number of occurance, positive weight and negative weight
def second_Q_main_update():
    connection = connect_db()
    cursor = connection.cursor()

    total_no_of_occurance = [count_sq_10(sq_10_query), count_sq_11(sq_11_query), count_sq_12(sq_12_query), count_sq_13(sq_13_query), count_sq_14(sq_14_query), count_sq_15(sq_15_query), count_sq_16(sq_16_query), count_sq_17(sq_17_query), count_sq_18(sq_18_query)]
    
    positive_weight = [(count_sq_10(sq_10_query)/float(19))*100,(count_sq_11(sq_11_query)/float(19))*100,(count_sq_12(sq_12_query)/float(19))*100,(count_sq_13(sq_13_query)/float(19))*100,(count_sq_14(sq_14_query)/float(19))*100,(count_sq_15(sq_15_query)/float(19))*100,(count_sq_16(sq_16_query)/float(19))*100,(count_sq_17(sq_17_query)/float(19))*100,(count_sq_18(sq_18_query)/float(19))*100]

    negative_weight = [(100 -(count_sq_10(sq_10_query)/float(19))*100),(100 -(count_sq_11(sq_11_query)/float(19))*100),(100 -(count_sq_12(sq_12_query)/float(19))*100),(100 -(count_sq_13(sq_13_query)/float(19))*100),(100 -(count_sq_14(sq_14_query)/float(19))*100),(100 -(count_sq_15(sq_15_query)/float(19))*100),(100 -(count_sq_16(sq_16_query)/float(19))*100),(100 -(count_sq_17(sq_17_query)/float(19))*100),(100 -(count_sq_18(sq_18_query)/float(19))*100)]
       
    id = [10, 11, 12, 13, 14, 15, 16, 17, 18]


    for i in range(0,len(id),1):
        a = '(' + str(id[i]) + ',' + str(total_no_of_occurance[i]) + ',' + str(positive_weight[i]) + ',' + str(negative_weight[i]) + ')'
        b = ''
        c = ''
        d = ''
        if i < (len(id)-1):
            c = c + a + b + d
            #print c
        else:
            c += a + b
    
        print c
        update_cell = ("INSERT INTO main (id, total_no_of_occurance, positive_weight, negative_weight)"
                          "VALUES %s" % c +
                      "ON DUPLICATE KEY UPDATE "
                      "total_no_of_occurance=VALUES(total_no_of_occurance), "
                      "positive_weight=VALUES(positive_weight),"
                      "negative_weight=VALUES(negative_weight)"
                          ";")
        cursor.execute(update_cell)
          
        connection.commit()
    connection.close()




#END OF UPDATING MAIN TABLE WITH SECOND Q


#THIRD QUADRANT - Update main table - populate total number of occurance, positive weight and negative weight 

#Get the data from the database quering third quadrant and counting total number of  occurance of the first number in quadrant - returns tq_19_total as integer
def count_tq_19(total):
    total_tq_19 = tq_19_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_19_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_19_total in number:
        return tq_19_total

#Get the data from the database quering third quadrant and counting total number of  occurance of the 2 number in quadrant - returns tq_20_total as integer
def count_tq_20(total):
    total_tq_20 = tq_20_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_20_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_20_total in number:
        return tq_20_total

#Get the data from the database quering third quadrant and counting total number of  occurance of the 3 number in quadrant - returns tq_21_total as integer
def count_tq_21(total):
    total_tq_21 = tq_21_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_21_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_21_total in number:
        return tq_21_total

#Get the data from the database quering third quadrant and counting total number of  occurance of the 4 number in quadrant - returns tq_22_total as integer
def count_tq_22(total):
    total_tq_22 = tq_22_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_22_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_22_total in number:
        return tq_22_total

#Get the data from the database quering third quadrant and counting total number of  occurance of the 5 number in quadrant - returns tq_23_total as integer
def count_tq_23(total):
    total_tq_23 = tq_23_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_23_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_23_total in number:
        return tq_23_total

    #Get the data from the database quering third quadrant and counting total number of  occurance of the 6 number in quadrant - returns tq_24_total as integer
def count_tq_24(total):
    total_tq_24 = tq_24_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_24_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_24_total in number:
        return tq_24_total

    #Get the data from the database quering third quadrant and counting total number of  occurance of the 7 number in quadrant - returns tq_25_total as integer
def count_tq_25(total):
    total_tq_25 = tq_25_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_25_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_25_total in number:
        return tq_25_total


    #Get the data from the database quering third quadrant and counting total number of  occurance of the 8 number in quadrant - returns tq_26_total as integer
def count_tq_26(total):
    total_tq_26 = tq_26_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_26_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_26_total in number:
        return tq_26_total

#Get the data from the database quering third quadrant and counting total number of  occurance of the 9 number in quadrant - returns tq_27_total as integer
def count_tq_27(total):
    total_tq_27 = tq_27_query
    connection = connect_db()
    cursor = connection.cursor()
    qr = cursor.execute(tq_27_query)
    number = cursor.fetchone()
    connection.commit()
    connection.close()
    for tq_27_total in number:
        return tq_27_total

#update THIRD Q in main table update total number of occurance, positive weight and negative weight
def third_Q_main_update():
    connection = connect_db()
    cursor = connection.cursor()

    total_no_of_occurance = [count_tq_19(tq_19_query), count_tq_20(tq_20_query), count_tq_21(tq_21_query), count_tq_22(tq_22_query), count_tq_23(tq_23_query), count_tq_24(tq_24_query), count_tq_25(tq_25_query), count_tq_26(tq_26_query), count_tq_27(tq_27_query)]
    
    positive_weight = [(count_tq_19(tq_19_query)/float(19))*100,(count_tq_20(tq_20_query)/float(19))*100,(count_tq_21(tq_21_query)/float(19))*100,(count_tq_22(tq_22_query)/float(19))*100,(count_tq_23(tq_23_query)/float(19))*100,(count_tq_24(tq_24_query)/float(19))*100,(count_tq_25(tq_25_query)/float(19))*100,(count_tq_26(tq_26_query)/float(19))*100,(count_tq_27(tq_27_query)/float(19))*100]

    negative_weight = [(100 -(count_tq_19(tq_19_query)/float(19))*100),(100 -(count_tq_20(tq_20_query)/float(19))*100),(100 -(count_tq_21(tq_21_query)/float(19))*100),(100 -(count_tq_22(tq_22_query)/float(19))*100),(100 -(count_tq_23(tq_23_query)/float(19))*100),(100 -(count_tq_24(tq_24_query)/float(19))*100),(100 -(count_tq_25(tq_25_query)/float(19))*100),(100 -(count_tq_26(tq_26_query)/float(19))*100),(100 -(count_tq_27(tq_27_query)/float(19))*100)]
       
    id = [19, 20, 21, 22, 23, 24, 25, 26, 27]


    for i in range(0,len(id),1):
        a = '(' + str(id[i]) + ',' + str(total_no_of_occurance[i]) + ',' + str(positive_weight[i]) + ',' + str(negative_weight[i]) + ')'
        b = ''
        c = ''
        d = ''
        if i < (len(id)-1):
            c = c + a + b + d
            #print c
        else:
            c += a + b
    
        print c
        update_cell = ("INSERT INTO main (id, total_no_of_occurance, positive_weight, negative_weight)"
                          "VALUES %s" % c +
                      "ON DUPLICATE KEY UPDATE "
                      "total_no_of_occurance=VALUES(total_no_of_occurance), "
                      "positive_weight=VALUES(positive_weight),"
                      "negative_weight=VALUES(negative_weight)"
                          ";")
        cursor.execute(update_cell)
          
        connection.commit()
    connection.close()

#END OF UPDATING MAIN TABLE WITH THIRD Q



def main():
    first_Q_main_update()
    second_Q_main_update()
    third_Q_main_update()
