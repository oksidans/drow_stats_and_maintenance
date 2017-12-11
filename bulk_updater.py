import mysql.connector
import os
import sys
from first_quadrant_determinator import first_quadrant
from second_quadrant_determinator import second_quadrant
from third_quadrant_determinator import third_quadrant
from fourth_quadrant_determinator import fourth_quadrant
from connections import connect_db


def first_q_update():
    """update the first quadrant by inserting automaticly current drow data into first quadrant"""
    fq_list = first_quadrant()
    connection = connect_db()
    cursor = connection.cursor()
    first_q_query = (""" INSERT INTO first_quadrant(fq_1, fq_2, fq_3, fq_4, fq_5, fq_6, fq_7, fq_8, fq_9, kolo, fq_freq) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)""")
    first_q_query_list = fq_list
    cursor.execute(first_q_query, fq_list)
    connection.commit()
    connection.close()
    #print fq_list


   

def second_q_update():
    """update the second quadrant by inserting automaticly current drow data into second quadrant"""
    sq_list = second_quadrant()
    connection = connect_db()
    cursor = connection.cursor()
    second_q_query = (""" INSERT INTO second_quadrant(sq_10, sq_11, sq_12, sq_13, sq_14, sq_15, sq_16, sq_17, sq_18, kolo, sq_freq) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)""")
    second_q_query_list = sq_list
    cursor.execute(second_q_query, second_q_query_list)
    connection.commit()
    connection.close()
    #print sq_list
    

def third_q_update():
    """update the third quadrant by inserting automaticly current drow data into third quadrant"""
    tq_list = third_quadrant()
    connection = connect_db()
    cursor = connection.cursor()
    third_q_query = (""" INSERT INTO third_quadrant(tq_19, tq_20, tq_21, tq_22, tq_23, tq_24, tq_25, tq_26, tq_27, kolo, tq_freq) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)""")
    third_q_query_list = tq_list
    cursor.execute(third_q_query, third_q_query_list)
    connection.commit()
    connection.close()
    #print tq_list


def fourth_q_update():
    """update the fourth quadrant by inserting automaticly current drow data into third quadrant"""
    ftq_list  = fourth_quadrant()
    connection = connect_db()
    cursor = connection.cursor()
    fourth_q_query = (""" INSERT INTO forth_quadrant(ftq_28, ftq_29, ftq_30, ftq_31, ftq_32, ftq_33, ftq_34, ftq_35, ftq_36, ftq_37, ftq_38, ftq_39, kolo, ftq_freq) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s)""")
    fourth_q_query_list = ftq_list
    cursor.execute(fourth_q_query, fourth_q_query_list)
    connection.commit()
    connection.close()
    #print ftq_list
    

def main_update():
    """Update the main statistics table"""
    pass
    




def update_all():
    first_q_update()
    second_q_update()
    third_q_update()
    fourth_q_update()
    main_update()




if __name__ == "__main__":
    update_all()