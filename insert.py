import mysql.connector
import os
import sys
from Tkinter import *
import datetime

def connect_db():
    # Mysql connector za bazu
    connection = mysql.connector.connect(user='root', password='123456',
                                         host = 'localhost',
                                         database='lottery_application')
    return connection

class Application(Frame):
    """ GUI application which can reveal the secret of longevity. """ 
    def __init__(self, master):
        """ Initialize the frame. """
        try:
            super(Application, self).__init__(master)
        except:      
            Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label
        self.inst_lbl = Label(self, text = "Loto Izvlacenje:")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create label for password      
        self.pw_lbl = Label(self, text = "Brojevi: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
        self.kolo_lbl = Label(self, text = "Broj kola:")
        self.kolo_lbl.grid(row = 3, column = 0, sticky = W)


        # create entry widget to enter drowing numbers - 7 in total
        self.first_number = Entry(self)
        self.first_number.grid(row = 1, column = 1, sticky = W )
        self.second_number = Entry(self)
        self.second_number.grid(row = 1, column = 2, sticky = W )
        self.third_number = Entry(self)
        self.third_number.grid(row = 1, column = 3, sticky = W )
        self.forth_number = Entry(self)
        self.forth_number.grid(row = 1, column = 4, sticky = W )
        self.fifth_number = Entry(self)
        self.fifth_number.grid(row = 1, column = 5, sticky = W )
        self.sixth_number = Entry(self)
        self.sixth_number.grid(row = 1, column = 6, sticky = W )
        self.seventh_number = Entry(self)
        self.seventh_number.grid(row = 1, column = 7, sticky = W )

        #Create widget to enter the number of drows
        self.kolo_ent = Entry(self)
        self.kolo_ent.grid(row = 3, column=1, sticky=W)    
        self.first_number_ent = Entry(self)
  
        # create submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.insert_into_database)
        self.submit_bttn.grid(row = 8, column = 6, sticky = W)


    def reveal(self):
        """ Display message. """
        number_1 = self.first_number.get()
        number_2 = self.second_number.get()
        number_3 = self.third_number.get()
        number_4 = self.forth_number.get()
        number_5 = self.fifth_number.get()
        number_6 = self.sixth_number.get()
        number_7 = self.seventh_number.get()
        broj_kola = self.kolo_ent.get()

        message = "Uneti su brojevi:" + number_1 + "-" + number_2 + "-" + number_3 + "-" + number_4 + "-" + number_5 + "-" + number_6 + "-" + number_7 + "Broj Kola:" + broj_kola
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

    def insert_into_database(self):
         i = datetime.datetime.now()
         drowing_date = i.strftime('%Y-%m-%d')
         #drowing_date = ((i.year, i.month, i.day) )
         list_of_numbers = [drowing_date,self.kolo_ent.get(), self.first_number.get(), self.second_number.get(), self.third_number.get(), self.forth_number.get(), self.sixth_number.get(), self.seventh_number.get()] 
         number_1 = self.first_number.get()
         number_2 = self.second_number.get()
         number_3 = self.third_number.get()
         number_4 = self.forth_number.get()
         number_5 = self.fifth_number.get()
         number_6 = self.sixth_number.get()
         number_7 = self.seventh_number.get()
         broj_kola = self.kolo_ent.get()
        
         connection = connect_db()
         cursor = connection.cursor()
         numbers_insert_query = '''INSERT into drow(drow_number, drow_date, fisrt_number, second_number, third_number, fourth_number, fifth_number, sixth_number, seveth_number) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
         number_query_list = [broj_kola,drowing_date, number_1, number_2, number_3, number_4, number_5, number_6, number_7] 
         cursor.execute(numbers_insert_query, number_query_list) 
         connection.commit()
         connection.close()
         print list_of_numbers 
        
         
    def date_and_time(self):
        date = datetime.date        
        print date

    def close_window(root):
        root.destroy()


if __name__ == "__main__":
# main
    root = Tk()
    root.title("Loto Entry Application")
    root.geometry("1200x250")
    app = Application(root)
    root.mainloop()
 

