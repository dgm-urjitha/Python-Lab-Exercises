# !/usr/bin/python3

# Import tkinter library
# Load data into Entry from text file
#

import tkinter as tk
from tkinter import ttk, messagebox
import locale
from tkinter import *
from tkinter import font


# Create an instance of tkinter window
FILENAME2="student.txt"
kCounter = 1
student=[[]]

class InfoRetrieve(ttk.Frame):
   def __init__(self, parent):
      
      ttk.Frame.__init__(self, parent, padding="100 100 100 100")
      self.parent = parent

      my_font1=('Verdana', 18, 'bold')
      ttk.Label(self, text="Name: ", background="lightgreen", font=my_font1).grid(
            column=0, row=0, sticky=tk.E)
      ttk.Label(self, text="Email: ", background="lightgreen", font=my_font1).grid(
            column=0, row=1, sticky=tk.E)
      ttk.Label(self, text="Phone: ", background="lightgreen", font=my_font1).grid(
            column=0, row=2, sticky=tk.E)
      
      #ttk.Label.configure(self, font=('courier', 50))
      
      
      student = read_students()
      
      #self.pack()
      # Define string variables for text entry fields
     
      
      self.eachstudentName = tk.StringVar()
      self.eachstudentEmail = tk.StringVar()
      self.eachstudentPhone = tk.StringVar()
     
      self.pack()
      #
      #Load first record      
      #
   
      #self.eachstudent = student[1][0]
      ttk.Entry(self, width=20,  textvariable=self.eachstudentName, font=my_font1).grid(column=1, row=0)
      ttk.Entry(self, width=20,  textvariable=self.eachstudentEmail, font=my_font1).grid(column=1, row=1)
      ttk.Entry(self, width=20,  textvariable=self.eachstudentPhone, font=my_font1).grid(column=1, row=2)
      
      
      ttk.Button(self, text="next student>>>", command=self.Next_Student) \
            .grid(column=2, row=0, padx=5)
      ttk.Button(self,   text=" Load ",  command=self.first_Student) \
            .grid(column=0, row=10, padx=3)
      ttk.Button(self,   text=" Clear ",  command=self.clear) \
            .grid(column=1, row=10, padx=3)

      ttk.Button(self,   text=" Add ",  command=self.add_Student) \
            .grid(column=2, row=10, padx=3)

   def clear(self):
      
      self.eachstudentName.set("")
      self.eachstudentEmail.set("")
      self.eachstudentPhone.set("")
      

   def first_Student(self):
      global kCounter
      
      self.eachstudentName.set(student[1][0])
      self.eachstudentEmail.set(student[1][1])
      self.eachstudentPhone.set(student[1][2])

   def add_Student(self):
      global kCounter
      newstudent =[]
   
      
      sname= self.eachstudentName.get()
      email = self.eachstudentEmail.get()
      phone = self.eachstudentPhone.get()
      newstudent.append(sname)
      newstudent.append(email)
      newstudent.append(phone)
      print(newstudent)
      student.append(newstudent)
      return student
      
      
      

      
   def Next_Student(self):
      global kCounter
      kCounter += 1
      self.eachstudentName.set(student[kCounter][0])
      self.eachstudentEmail.set(student[kCounter][1])
      self.eachstudentPhone.set(student[kCounter][2])
   
      
def read_students():
   global student
   
   
   with open(FILENAME2) as file:
      
      for line in file:         
         line = line.replace("\n", "")
         line = line.split("|")
         #onestudent.append(line)
         student.append(line)
         #kounter +=1        
   return student
 

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Student Information")
    InfoRetrieve(root)
    root.mainloop()

