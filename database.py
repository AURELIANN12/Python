from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter



from mysql.connector import Error

try:
    conn = mysql.connector.connect(user='root', password='Election@123',
                                   host='localhost', database='sakila',
                                   auth_plugin='mysql_native_password')
    if conn.is_connected():
        print('Connected to MySQL database')

except Error as e:
    print(e)



class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Custome Management System")
        self.root.geometry("1550x800+0+0")

#  ==================variable=============
        self.Member_var=StringVar()
        self.Passport_Number_var=StringVar()
        self.Name_var=StringVar()
        self.Country_var=StringVar()
        self.Adress_var=StringVar()
        self.Phone_Number_var=StringVar()
        self.Gender_var=StringVar()
        self.Insurance_var=StringVar()
        self.Destination_Country_var=StringVar()
        self.Destination_City_var=StringVar()
        self.Departure_Date_var=StringVar()
        self.Arivall_Date_var=StringVar()
        self.Status_Payment_var=StringVar()
        self.Travel_Method_var=StringVar()



        lbtitlte = Label(root, text="CUSTOMER MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbtitlte.pack(side=TOP, fill=X)         

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
 
            #   ==============dataframeleft========
        DataFrameLeft=LabelFrame(frame,text="Customer Information", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMemebr =Label(DataFrameLeft,bg=("powder blue"),text="Memeber",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMemebr.grid(row=0,column=0,sticky=W)

      
        comMember = ttk.Combobox(DataFrameLeft,textvariable=self.Member_var, font=("times new roman", 15, "bold"), width=27,state="readonly")
        comMember["values"] = ("Guest", "Membership", "Membership Pro")  
        comMember.grid(row=0, column=1)  
        comMember.current(0)


        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Passport_Number",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Passport_Number_var,width=29)
        txtPRN_No.grid(row=1,column=1)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=2,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Name_var,width=29)
        txtPRN_No.grid(row=2,column=1)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Country",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=3,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Country_var,width=29)
        txtPRN_No.grid(row=3,column=1)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Adress",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=4,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Adress_var,width=29)
        txtPRN_No.grid(row=4,column=1)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Phone_Number",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=5,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Phone_Number_var,width=29)
        txtPRN_No.grid(row=5,column=1)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Gender",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=6,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Gender_var,width=29)
        txtPRN_No.grid(row=6,column=1)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Insurance",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=0,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Insurance_var,width=29)
        txtPRN_No.grid(row=0,column=3)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Destination_Country",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Destination_Country_var,width=29)  #check destination country
        txtPRN_No.grid(row=1,column=3)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Destination_city",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=2,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Destination_City_var,width=29)
        txtPRN_No.grid(row=2,column=3)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Departure_date",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=3,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Departure_Date_var,width=29)
        txtPRN_No.grid(row=3,column=3)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Arivall_Date",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=4,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Arivall_Date_var,width=29)
        txtPRN_No.grid(row=4,column=3)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Status_Payment",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=5,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Status_Payment_var,width=29)
        txtPRN_No.grid(row=5,column=3)

        lblPRN_No =Label(DataFrameLeft,bg=("powder blue"),text="Travel_Method",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=6,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman", 15, "bold"),textvariable=self.Travel_Method_var,width=29)
        txtPRN_No.grid(row=6,column=3)

        #    ====================dataframeright======
        DataFrameRight = LabelFrame(frame, text="Trip Details", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.txtBox = Text(DataFrameRight, font=("times new roman",), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Italy(Rome)','Italy(Amalfi)','Italy(Milano)','Spain(Palma de Malorca)','Spain(Barcelon)','Spain(Madrid)',
                 'France(Paris)','France(Marseille)','France(Lyon)','Germany(Berlin)','Germany(Frankfurt)','Germany(Dresden)']

        
    
        def SelectBook(event=""):
    # Get the indices of the currently selected items
            selection_indices = listBox.curselection()
    
    # Check if any item is selected
            if selection_indices:
        # Get the value of the selected item using the index
              index = selection_indices[0]
              value = listBox.get(index)
        
        # Proceed with further processing based on the selected value
              if value == 'Italy(Rome)':
                self.Destination_Country_var.set("Italy")
                self.Destination_City_var.set("Rome")
                self.Departure_Date_var.set("12.06.2024")
                self.Arivall_Date_var.set("17.06.2024")
                self.Insurance_var.set("Yes")
                self.Travel_Method_var.set("Train")
                self.Status_Payment_var.set("Before")

              elif value == 'Italy(Amalfi)':
                self.Destination_Country_var.set("Italy")
                self.Destination_City_var.set("Amalfi")
                self.Departure_Date_var.set("15.06.2024")
                self.Arivall_Date_var.set("20.06.2024")
                self.Insurance_var.set("no")
                self.Travel_Method_var.set("Plane")
                self.Status_Payment_var.set("After")

              elif value == 'Italy(Milano)':
                self.Destination_Country_var.set("Italy")
                self.Destination_City_var.set("Milano")
                self.Departure_Date_var.set("30.06.2024")
                self.Arivall_Date_var.set("5.07.2024")
                self.Insurance_var.set("Yes")
                self.Travel_Method_var.set("Plane")
                self.Status_Payment_var.set("After")

              elif value == 'Spain(Barcelona)':
                self.Destination_Country_var.set("Spain")
                self.Destination_City_var.set("Barcelon")
                self.Departure_Date_var.set("12.05.2024")
                self.Arivall_Date_var.set("20.05.2024")
                self.Insurance_var.set("Yes")
                self.Travel_Method_var.set("Train")
                self.Status_Payment_var.set("Before")

              elif value == 'Spain(Madrid)':
                self.Destination_Country_var.set("Spain")
                self.Destination_City_var.set("Madrid")
                self.Departure_Date_var.set("11.08.2024")
                self.Arivall_Date_var.set("17.08.2024")
                self.Insurance_var.set("No")
                self.Travel_Method_var.set("Bus")
                self.Status_Payment_var.set("After")

              elif value == 'Spain(Palma de Malorca)':
                self.Destination_Country_var.set("Spain")
                self.Destination_City_var.set("Palma de Malorca")
                self.Departure_Date_var.set("12.09.2024")
                self.Arivall_Date_var.set("17.09.2024")
                self.Insurance_var.set("Yes")
                self.Travel_Method_var.set("Bus")
                self.Status_Payment_var.set("Before")

              elif value == 'France(Paris)':
                self.Destination_Country_var.set("France")
                self.Destination_City_var.set("Paris")
                self.Departure_Date_var.set("15.05.2024")
                self.Arivall_Date_var.set("17.05.2024")
                self.Insurance_var.set("No")
                self.Travel_Method_var.set("Bus")
                self.Status_Payment_var.set("After")

              elif value == 'France(Marseille)':
                self.Destination_Country_var.set("France")
                self.Destination_City_var.set("Marseille")
                self.Departure_Date_var.set("30.06.2024")
                self.Arivall_Date_var.set("2.07.2024")
                self.Insurance_var.set("No")
                self.Travel_Method_var.set("Bus")
                self.Status_Payment_var.set("After")

              elif value == 'France(Lyon)':
                self.Destination_Country_var.set("France")
                self.Destination_City_var.set("Lyon")
                self.Departure_Date_var.set("10.05.2024")
                self.Arivall_Date_var.set("17.05.2024")
                self.Insurance_var.set("yes")
                self.Travel_Method_var.set("Train")
                self.Status_Payment_var.set("Before")

              elif value == 'Germany(Berlin)':
                self.Destination_Country_var.set("Germany")
                self.Destination_City_var.set("Berlin")
                self.Departure_Date_var.set("20.05.2024")
                self.Arivall_Date_var.set("26.05.2024")
                self.Insurance_var.set("Yes")
                self.Travel_Method_var.set("Train")
                self.Status_Payment_var.set("Before")

              elif value == 'Germany(Frankfurt)':
                self.Destination_Country_var.set("Germany")
                self.Destination_City_var.set("Frankfurt")
                self.Departure_Date_var.set("5.06.2024")
                self.Arivall_Date_var.set("10.06.2024")
                self.Insurance_var.set("Yes")
                self.Travel_Method_var.set("Plane")
                self.Status_Payment_var.set("After")

              elif value == 'Germany(Dresden)':
                self.Destination_Country_var.set("Germany")
                self.Destination_City_var.set("Dresden")
                self.Departure_Date_var.set("15.08.2024")
                self.Arivall_Date_var.set("25.08.2024")
                self.Insurance_var.set("Yes")
                self.Travel_Method_var.set("Plane")
                self.Status_Payment_var.set("After")
            else:
        # Handle the case when no item is selected
               pass

# Create the Listbox widget
        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

# Populate the Listbox with items
        for item in listBooks:
          listBox.insert(END, item)

        # ==============================buttons frame======

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",command=self.update,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text="Delete",command=self.delete,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Resest",command=self.reset,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        # ==============================information frame======

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, padx=20, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table =ttk.Treeview(Table_frame,column=("Member", "Passport_Number", "Name", "Country", "Adress", "Phone_Number", "Gender", "Insurance", "Destination_Country", "Departure_City","Arivall_Date", "Status_Payment", "Travel_Method"),xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)




    
        self.library_table.heading("Member", text="Member")
        self.library_table.heading("Passport_Number", text="Passport Number")
        self.library_table.heading("Name", text="Name")
        self.library_table.heading("Country", text="Country")
        self.library_table.heading("Adress", text="Adress")
        self.library_table.heading("Phone_Number", text="Phone Number")
        self.library_table.heading("Gender", text="Gender")
        self.library_table.heading("Insurance", text="Insurance")
        self.library_table.heading("Destination_Country", text="Destination Country")
        self.library_table.heading("Departure_City", text="Departure City")
        self.library_table.heading("Arivall_Date", text="Arivall Date")
        self.library_table.heading("Status_Payment", text="Status Payment")
        self.library_table.heading("Travel_Method", text="Travel Method")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH,expand=1) 

        self.library_table.column("Member",width=100)
        self.library_table.column("Passport_Number",width=100)
        self.library_table.column("Name",width=100)
        self.library_table.column("Country",width=100)
        self.library_table.column("Adress",width=100)
        self.library_table.column("Phone_Number",width=100)
        self.library_table.column("Gender",width=100)
        self.library_table.column("Insurance",width=100)
        self.library_table.column("Destination_Country",width=100)
        self.library_table.column("Departure_City",width=100)
        self.library_table.column("Arivall_Date",width=100)
       
        self.library_table.column("Status_Payment",width=100)
        self.library_table.column("Travel_Method",width=100)
        
        self.fetch_data()
        # self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)


    def adda_data(self):
    




        conn = mysql.connector.connect(user='root', password='Election@123',
                                   host='localhost', database='sakila',
                                   auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO library VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.Member_var.get(),
            self.Passport_Number_var.get(),
            self.Name_var.get(),
            self.Country_var.get(),
            self.Adress_var.get(),
            self.Phone_Number_var.get(),
            self.Gender_var.get(),
            self.Insurance_var.get(),
            self.Destination_Country_var.get(),
            self.Destination_City_var.get(),
            self.Departure_Date_var.get(),
            self.Arivall_Date_var.get(),
            self.Status_Payment_var.get(),
            self.Travel_Method_var.get()
                                ))
        
        # my_cursor.execute("INSERT INTO library VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
        #    self.Member_var.get(),
        #    self.Passport_Number_var.get(),
        #    self.Name_var.get(),
        #    self.Country_var.get(),
        #    self.Adress_var.get(),
        #    self.Phone_Number_var.get(),
        #    self.Gender_var.get(),
        #    self.Insurance_var.get(),
        #    self.Destination_Country_var.get(),
        #    self.Destination_City_var.get(),
        #    self.Departure_Date_var.get(),
        #    self.Arivall_Date_var.get(),
        #    self.Status_Payment_var.get(),
        #    self.Travel_Method_var.get()
        #                                                    ))

        
        
                                                                                #  ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Succes","Member has been inserted successfuly")

    def update(self):
        conn = mysql.connector.connect(user='root', password='Election@123',
                                   host='localhost', database='sakila',
                                   auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        # my_cursor.execute("UPDATE library SET Member=%s, Passport_Number=%s, Name=%s, Country=%s, Adress=%s, Phone_Number=%s, Gender=%s, Insurance=%s, Destination_Country=%s, Destination_City=%s, Departure_Date=%s, Arivall_Date=%s, Status_Payment=%s, Travel_Method=%s WHERE Passport_Number=%s ",
        #               (
        #                   self.Member_var.get(),
        #                   self.Passport_Number_var.get(),
        #                   self.Name_var.get(),
        #                   self.Country_var.get(),
        #                   self.Adress_var.get(),
        #                   self.Phone_Number_var.get(),
        #                   self.Gender_var.get(),
        #                   self.Insurance_var.get(),
        #                   self.Destination_Country_var.get(),
        #                   self.Destination_City_var.get(),
        #                   self.Departure_Date_var.get(),
        #                   self.Arivall_Date_var.get(),
        #                   self.Status_Payment_var.get(),
        #                   self.Travel_Method_var.get(),
        #                   self.Passport_Number_var.get()
        #               ))

        my_cursor.execute("""
    UPDATE library 
    SET Member=%(Member)s, 
        Passport_Number=%(Passport_Number)s, 
        Name=%(Name)s, 
        Country=%(Country)s, 
        Adress=%(Adress)s, 
        Phone_Number=%(Phone_Number)s, 
        Gender=%(Gender)s, 
        Insurance=%(Insurance)s, 
        Destination_Country=%(Destination_Country)s, 
        Destination_City=%(Destination_City)s, 
        Departure_Date=%(Departure_Date)s, 
        Arivall_Date=%(Arivall_Date)s, 
        Status_Payment=%(Status_Payment)s, 
        Travel_Method=%(Travel_Method)s 
    WHERE Passport_Number=%(Passport_Number)s
""", {
    'Member': self.Member_var.get(),
    'Passport_Number': self.Passport_Number_var.get(),
    'Name': self.Name_var.get(),
    'Country': self.Country_var.get(),
    'Adress': self.Adress_var.get(),
    'Phone_Number': self.Phone_Number_var.get(),
    'Gender': self.Gender_var.get(),
    'Insurance': self.Insurance_var.get(),
    'Destination_Country': self.Destination_Country_var.get(),
    'Destination_City': self.Destination_City_var.get(),
    'Departure_Date': self.Departure_Date_var.get(),
    'Arivall_Date': self.Arivall_Date_var.get(),
    'Status_Payment': self.Status_Payment_var.get(),
    'Travel_Method': self.Travel_Method_var.get()
})





        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

   



        messagebox.showinfo("Success", "Member has been updated")



    
    def fetch_data(self):
         conn = mysql.connector.connect(user='root', password='Election@123',
                                   host='localhost', database='sakila',
                                   auth_plugin='mysql_native_password')
         my_cursor = conn.cursor()  # Corrected cursor invocation
         my_cursor.execute("SELECT * FROM library")
         rows = my_cursor.fetchall()
         if len(rows) != 0:
           self.library_table.delete(*self.library_table.get_children())  # Corrected syntax
           for row in rows:  # Changed 'in' to 'row' to avoid syntax error
            self.library_table.insert("", END, values=row)  # Changed 'i' to 'row' to use correct variable
         conn.commit()
         conn.close()


    # def get_cursor(self,event=""):
    #    cursor_row=self.library_table.focus()
    #    content=self.library_table.item(cursor_row)
    #    row=content['values']

    #    self.Member_var.set(row[0])
    #    self.Passport_Number_var.set(row[1])
    #    self.Name_var.set(row[2])
    #    self.Country_var.set(row[3])
    #    self.Adress_var.set(row[4])
    #    self.Phone_Number_var.set(row[5])
    #    self.Gender_var.set(row[6])
    #    self.Insurance_var.set(row[7])
    #    self.Destination_Country_var.set(row[8])
    #    self.Destination_City_var.set(row[9])
    #    self.Departure_Date_var.set(row[10])
    #    self.Arivall_Date_var.set(row[11])
    #    self.Status_Payment_var.set(row[12])
    #    self.Travel_Method_var.set(row[13])

    def get_cursor(self, event=""):  # Define the method with the event parameter
       cursor_row = self.library_table.focus()
       content = self.library_table.item(cursor_row)
       row = content['values']

       self.Member_var.set(row[0])
       self.Passport_Number_var.set(row[1])
       self.Name_var.set(row[2])
       self.Country_var.set(row[3])
       self.Adress_var.set(row[4])
       self.Phone_Number_var.set(row[5])
       self.Gender_var.set(row[6])
       self.Insurance_var.set(row[7])
       self.Destination_Country_var.set(row[8])
       self.Destination_City_var.set(row[9])
       self.Departure_Date_var.set(row[10])
       self.Arivall_Date_var.set(row[11])
       self.Status_Payment_var.set(row[12])
       self.Travel_Method_var.set(row[13])

       

    def showData(self):
       self.txtBox.insert(END,"Member\t\t"+self.Member_var.get()+"\n")
       self.txtBox.insert(END,"Passport_Number\t\t"+self.Passport_Number_var.get()+"\n")
       self.txtBox.insert(END,"Name\t\t"+self.Name_var.get()+"\n")
       self.txtBox.insert(END,"Country\t\t"+self.Country_var.get()+"\n")
       self.txtBox.insert(END,"Adress\t\t"+self.Adress_var.get()+"\n")
       self.txtBox.insert(END,"Phone_Number\t\t"+self.Phone_Number_var.get()+"\n")
       self.txtBox.insert(END,"Gender\t\t"+self.Gender_var.get()+"\n")
       self.txtBox.insert(END,"Insurance\t\t"+self.Insurance_var.get()+"\n")
       self.txtBox.insert(END,"Destination_Country\t\t"+self.Destination_Country_var.get()+"\n")
       self.txtBox.insert(END,"Destination_City\t\t"+self.Destination_City_var.get()+"\n")
       self.txtBox.insert(END,"Departure_Date\t\t"+self.Departure_Date_var.get()+"\n")
       self.txtBox.insert(END,"Arival_Date\t\t"+self.Arivall_Date_var.get()+"\n")
       self.txtBox.insert(END,"Status_Payment\t\t"+self.Status_Payment_var.get()+"\n")
       self.txtBox.insert(END,"Travel_Method\t\t"+self.Travel_Method_var.get()+"\n")
       
    def reset(self):
       self.Member_var.set("")
       self.Passport_Number_var.set("")
       self.Name_var.set("")
       self.Country_var.set("")
       self.Adress_var.set("")
       self.Phone_Number_var.set("")
       self.Gender_var.set("")
       self.Insurance_var.set("")
       self.Destination_Country_var.set("")
       self.Destination_City_var.set("")
       self.Departure_Date_var.set("")
       self.Arivall_Date_var.set("")
       self.Status_Payment_var.set("")
       self.Travel_Method_var.set("")
       self.txtBox.delete("1.0",END)

       
    def iExit(self):
       iExit=tkinter.messagebox.askyesno("Librardy management System","Do you want to exit?:")
       if iExit>0:
          self.root.destroy()
          return
       

    # def delete(self):
    # #    if self.Passport_Number_var.get()=="" or self.id_var.get()=="":
    #      if self.Passport_Number_var.get():# == "" or self.id_var.get() == "":
    #         messagebox.showerror("Error","First select the Member")
    #      else :
    #         conn = mysql.connector.connect(user='root', password='Election@123',
    #                                host='localhost', database='sakila',
    #                                auth_plugin='mysql_native_password')
    #         my_cursor=conn.cursor()
    #         query="delete from library where Passport_Number=%s"
    #         value=(self.Passport_Number_var.get())
    #         my_cursor.execute(query,value)
    #         conn.commit()
    #         self.fetch_data()
    #         self.reset()
    #         conn.close()
       
    #         messagebox.showinfo("Member has been deleted")

    def delete(self):
     if self.Passport_Number_var.get() == "":
        messagebox.showerror("Error", "First select the Member")
     else:
        conn = mysql.connector.connect(user='root', password='Election@123',
                                       host='localhost', database='sakila',
                                       auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        query = "delete from library where Passport_Number=%s"
        value = (self.Passport_Number_var.get(),)  # Make it a tuple
        my_cursor.execute(query, value)
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()  # Added parentheses to call the method
       
        messagebox.showinfo("Member has been deleted")





if __name__ == "__main__":
    root = Tk()  # Corrected the capitalization of 'Tk'
    obj = LibraryManagementSystem(root)  
    root.mainloop()

    

