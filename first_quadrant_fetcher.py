#Fetch the data from the first quadrant to make statisc calculations
import mysql.connector
import os
import sys
from connections import connect_db

def get_fisrt_quadrant_data():
    connection = connect_db()
    cursor = connection.cursor()
    #cursor.execute("select fq_1, fq_2, fq_3, fq_4, fq_5, fq_6, fq_7, fq_8, fq_9, fq_freq, id, count(id), count(kolo) from first_quadrant")
    cursor.execute("select fq_1, fq_2, fq_3, fq_4, fq_5, fq_6, fq_7, fq_8, fq_9, fq_freq from first_quadrant")
    numbers = cursor.fetchall()
    connection.close()
    #print numbers
    return numbers


def get_first_q_counts():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("select count(id), count(kolo) from first_quadrant")
    counts = cursor.fetchall()
    connection.close()
    return counts



if __name__ == "__main__":
    get_fisrt_quadrant_data()
    get_first_q_counts()