import mysql.connector
import mysql.connector
import tkinter
import random
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

login_page = Tk()
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Sumit_8983",
    database="shop_management_system"
)
mycursor = mydb.cursor()
f_head = "comicsans 10 bold"
f1 = "californian 10 "
login_page.geometry("400x144")
pass_word = ["1234"]


def logIn():
    for pw in pass_word:
        if (pass_entry.get() == pw):
            main_window = Tk()
            main_window.title("Shop management System")
            main_window.geometry("400x400")

            # Adding Welcome text

            welcome_txt = Label(main_window, text="Welcome to the Shop Management System!", relief=RAISED,
                                borderwidth=4, bg="peach puff", padx=5, pady=5, font=f_head)
            welcome_txt.place(x=50, y=10)

            # Adding the  button

            search_button = Button(main_window, text="Search", font=f1, pady=5, padx=5, command=search)
            search_button.place(x=10, y=50)

            add_button = Button(main_window, text="Add Product", font=f1, pady=5, padx=5, command=add_product)
            add_button.place(x=10, y=90)

            delete_button = Button(main_window, text="Delete Product", font=f1, pady=5, padx=5, command=delete_product)
            delete_button.place(x=10, y=135)

            update_button = Button(main_window, text="Update Product", font=f1, pady=5, padx=5, command=update_product)
            update_button.place(x=10, y=175)

            PFT_button = Button(main_window, text="Proceed for Transaction", font=f1, pady=5, padx=5,
                                command=proceed_for_transaction)
            PFT_button.place(x=10, y=220)

            trans_history_button = Button(main_window, text="Transaction History Report", font=f1, pady=5, padx=5,
                                          command=trans_history)
            trans_history_button.place(x=10, y=260)

            stock_report_button = Button(main_window, text="Stock Report", font=f1, pady=5, padx=5,
                                         command=stock_report)
            stock_report_button.place(x=10, y=300)

            sales_report_button = Button(main_window, text="Sales Report", font=f1, pady=5, padx=5,
                                         command=sales_report)
            sales_report_button.place(x=10, y=340)

            login_page.destroy()
            main_window.mainloop()
        else:
            messagebox.showerror("showerror", "Incorrect Password")


def reset_tab():
    reset_window = Tk()
    reset_window.title("Reset Password")
    reset_window.geometry("400x300")
    # Adding enter the old password text
    old_pass = Label(reset_window, text="Enter the Old Password:-", relief=SUNKEN, font=f1, pady=5, padx=5)
    old_pass.place(x=10, y=50)
    reset_pass = Label(reset_window, text="Reset Password!", relief=RAISED, borderwidth=4, bg="peach puff", padx=5,
                       pady=5, font=f_head)
    reset_pass.place(x=120, y=10)
    # Entry field for old pass
    reset = StringVar()
    resetpass_entry = Entry(reset_window, textvariable=reset, font=f1)
    resetpass_entry.place(x=180, y=50)
    # New pass text
    new_pass = Label(reset_window, text="Enter the New Password:-", relief=SUNKEN, font=f1, pady=5, padx=5)
    new_pass.place(x=10, y=100)
    # Entry field for new pass
    newp = StringVar()
    newpass_entry = Entry(reset_window, textvariable=newp, font=f1)
    newpass_entry.place(x=180, y=100)
    # Reset Password Button
    reset__button = Button(reset_window, text="Reset Password", font=f1, pady=5, padx=5)
    reset__button.place(x=210, y=130)
    login_page.destroy()
    reset_window.mainloop()

#searching is done
def search():
    def find():

        product_name = p_n.get()
        mycursor = mydb.cursor()

        mycursor.execute("select P_Quantity from product where P_name = '" + product_name + "'")
        result = mycursor.fetchall()
        if bool(result):
            res = result[0]

            if res[0] == 0:
                Label(root,text="Not in stock!").place(x=30,y=180)
                # messagebox.showinfo("showinfo", "Not in stock!!!")
            else:
                Label(root,text=f"Stock is present! Available stock is {res[0]}").place(x=30,y=180)
                # messagebox.showinfo("showinfo", "Stock is present! Available Stock is " + str(res[0]))

        else:
            messagebox.showinfo("showinfo", "No such product is present!")

    root = Tk()
    root.title("Search Window")
    root.geometry("400x300")

    def des():
        root.destroy()

    Label(root, text="Product Name").place(x=30, y=60)
    Button(root, text="Search", height=1, width=13, command=find).place(x=140, y=90)
    Button(root, text="Close", height=1, width=13, command=des).place(x=140, y=130)
    # entry for product name
    p_n = Entry(root)
    p_n.place(x=140, y=60)

    root.mainloop()

#is working
def add_product():
    mysqldb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="Sumit_8983",
        database="shop_management_system"
    )
    mycursor = mysqldb.cursor()

    def GetValue(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0, select['c_id'])
        e2.insert(0, select['P_name'])
        e3.insert(0, select['P_cat'])
        e4.insert(0, select['P_price'])
        e5.insert(0, select['Quantity'])
        e6.insert(0, select['P_mfg'])
        e7.insert(0, select['P_expi'])

    def Add():
        mysqldb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Sumit_8983",
            database="shop_management_system"
        )
        mycursor = mysqldb.cursor()
        mycursor.execute(f"select c_id from category where c_name = '{e3.get()}'")
        e8 = mycursor.fetchall()

        cat_id = e8[0]
        c_id = cat_id[0]
        # print(c_id)
        P_id = e1.get()
        P_name = e2.get()
        P_cat = c_id
        P_price = e4.get()
        P_Quantity = e5.get()
        P_mfg = e6.get()
        P_expi = e7.get()

        try:
            sql = "INSERT INTO product(P_id, P_name,P_cat ,P_price,P_Quantity,P_mfg,P_expi) VALUES (%s, %s, %s, %s,%s,%s,%s)"
            val = (P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi)
            mycursor.execute(sql, val)
            # mycursor.execute(f"INSERT INTO product(P_id, P_name,P_cat ,P_price,P_Quantity,P_mfg,P_expi) VALUES ({P_id},{P_name},{P_cat},{P_price},{P_Quantity},{P_mfg},{P_expi})")
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record inserted successfully...")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e1.focus_set()
        except Exception as e:

           # print(e)
            mysqldb.rollback()
            mysqldb.close()

    def show():
        mysqldb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Sumit_8983",
            database="shop_management_system"
        )
        mycursor = mysqldb.cursor()
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT P_id,P_name,P_cat,P_price,P_Quantity,P_mfg,P_expi FROM product")
        records = mycursor.fetchall()
        #print(records)
        for i, (P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi) in enumerate(records, start=1):
            listBox.insert("", "end", values=(P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi))
            mysqldb.close()

    root = Tk()
    root.geometry("750x600")

    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8

    # tk.Label(root, text ="shop product",fg="green",font=(None,30)).place(x=300,y=200)
    tk.Label(root, text="product ID").place(x=10, y=10)
    tk.Label(root, text="Name").place(x=10, y=40)
    tk.Label(root, text="category").place(x=10, y=70)
    tk.Label(root, text="Price").place(x=10, y=100)

    tk.Label(root, text="Quantity").place(x=10, y=130)
    tk.Label(root, text="MFG").place(x=10, y=160)
    tk.Label(root, text="EXP").place(x=10, y=190)

    e1 = Entry(root)  # pid
    e1.place(x=140, y=10)

    e2 = Entry(root)  # pname
    e2.place(x=140, y=40)

    e3 = Entry(root)  # categoryname
    e3.place(x=140, y=70)

    e4 = Entry(root)  # price
    e4.place(x=140, y=100)

    e5 = Entry(root)  # quantity
    e5.place(x=140, y=130)

    e6 = Entry(root)  # MFG
    e6.place(x=140, y=160)

    e7 = Entry(root)  # EXP
    e7.place(x=140, y=190)

    Button(root, text="Add", command=Add, height=3, width=10).place(x=100, y=230)
    # Button(root, text="update", command = update,height=3, width= 13).place(x=140, y=230)
    # Button(root, text="Delete", command = delete,height=3, width= 13).place(x=250, y=230)
    def des():
        root.destroy()
    Button(root,text="Close",command=des,height=3, width=10).place(x=550, y=500)
    cols = ('P_id', 'P_name', 'P_cat', 'P_price', 'Quantity', 'MFG', 'EXP')
    listBox = ttk.Treeview(root, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col, anchor=tkinter.CENTER)
        listBox.column(col, width=70, minwidth=50, anchor=tkinter.CENTER)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=200)

    show()
    listBox.bind('<Double-Button-1>', GetValue)
    listBox.place(x=20, y=320)
    root.mainloop()

#is working
def delete_product():
    mysqldb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="Sumit_8983",
        database="shop_management_system"
    )
    mycursor = mysqldb.cursor()

    def GetValue(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0, select['c_id'])
        e2.insert(0, select['P_name'])
        e3.insert(0, select['P_cat'])
        e4.insert(0, select['P_price'])
        e5.insert(0, select['Quantity'])
        e6.insert(0, select['P_mfg'])
        e7.insert(0, select['P_expi'])

    def delete():
        P_id = e1.get()
        mysqldb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Sumit_8983",
            database="shop_management_system"
        )
        mycursor = mysqldb.cursor()
        try:
            sql = "delete from product where P_id = %s"
            val = (P_id,)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record Delete Successfully..")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e1.focus_set()

        except Exception as e:
            #print(e)
            mysqldb.rollback()
            mysqldb.close()

    def show():
        mysqldb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Sumit_8983",
            database="shop_management_system"
        )
        mycursor = mysqldb.cursor()
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT P_id,P_name,P_cat,P_price,P_Quantity,P_mfg,P_expi FROM product")
        records = mycursor.fetchall()
        #print(records)

        for i, (P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi) in enumerate(records, start=1):
            listBox.insert("", "end", values=(P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi))
            mysqldb.close()

    root = Tk()
    root.geometry("800x600")

    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8

    # tk.Label(root, text ="shop product",fg="green",font=(None,30)).place(x=300,y=200)
    tk.Label(root, text="product ID").place(x=10, y=10)
    tk.Label(root, text="Name").place(x=10, y=40)
    tk.Label(root, text="category").place(x=10, y=70)
    tk.Label(root, text="Price").place(x=10, y=100)

    tk.Label(root, text="Quantity").place(x=10, y=130)
    tk.Label(root, text="MFG").place(x=10, y=160)
    tk.Label(root, text="EXP").place(x=10, y=190)

    e1 = Entry(root)  # pid
    e1.place(x=140, y=10)

    e2 = Entry(root)  # pname
    e2.place(x=140, y=40)

    e3 = Entry(root)  # categoryname
    e3.place(x=140, y=70)

    e4 = Entry(root)  # price
    e4.place(x=140, y=100)

    e5 = Entry(root)  # quantity
    e5.place(x=140, y=130)

    e6 = Entry(root)  # MFG
    e6.place(x=140, y=160)

    e7 = Entry(root)  # EXP
    e7.place(x=140, y=190)

    def des():
        root.destroy()

    Button(root, text="Close", command=des, height=3, width=10).place(x=550, y=500)
    # Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=230)
    # Button(root, text="update", command=update, height=3, width=13).place(x=140, y=230)
    Button(root, text="Delete", command=delete, height=3, width=10).place(x=100, y=230)

    cols = ('P_id', 'P_name', 'P_cat', 'P_price', 'Quantity', 'MFG', 'EXP')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col, anchor=tkinter.CENTER)
        listBox.column(col, width=70, minwidth=50, anchor=tkinter.CENTER)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=200)
    show()
    listBox.bind('<Double-Button-1>', GetValue)
    listBox.place(x=20, y=320)
    root.mainloop()

#is working
def update_product():
    mysqldb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="Sumit_8983",
        database="shop_management_system"
    )
    mycursor = mysqldb.cursor()


    def GetValue(event, listBox=None):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0, select['c_id'])
        e2.insert(0, select['P_name'])
        e3.insert(0, select['P_cat'])
        e4.insert(0, select['P_price'])
        e5.insert(0, select['Quantity'])
        e6.insert(0, select['P_mfg'])
        e7.insert(0, select['P_expi'])

    def update():

        mysqldb = mysql.connector.connect(host="localhost", username="root", password="Sumit_8983",database="shop_management_system")
        mycursor = mysqldb.cursor()
        mycursor.execute(f"select c_id from category where c_name = '{e3.get()}'")
        e8 = mycursor.fetchall()

        cat_id = e8[0]
        c_id = cat_id[0]

        P_id = e1.get()
        P_name = e2.get()
        P_cat = c_id
        P_price = e4.get()
        P_Quantity = e5.get()
        P_mfg = e6.get()
        P_expi = e7.get()



        try:
            sql = "Update product set P_name=%s, P_cat= %s, P_price= %s,P_Quantity=%s,P_mfg=%s,P_expi=%s where P_id= %s"
            val = (P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi,P_id)
            mycursor.execute(sql, val)
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Record Updated successfully...")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e1.focus_set()
        except Exception as e:
            #print(e)
            mysqldb.rollback()
            mysqldb.close()

    def show():
        mysqldb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Sumit_8983",
            database="shop_management_system"
        )

        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT P_id,P_name,P_cat,P_price,P_Quantity,P_mfg,P_expi FROM product")
        records = mycursor.fetchall()
        #print(records)

        for i, (P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi) in enumerate(records, start=1):
            listBox.insert("", "end", values=(P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi))
            mysqldb.close()
    root = Tk()
    root.geometry("800x600")

    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    global e8

    # tk.Label(root, text ="shop product",fg="green",font=(None,30)).place(x=300,y=200)
    tk.Label(root, text="product ID").place(x=10, y=10)
    tk.Label(root, text="Name").place(x=10, y=40)
    tk.Label(root, text="category").place(x=10, y=70)
    tk.Label(root, text="Price").place(x=10, y=100)

    tk.Label(root, text="Quantity").place(x=10, y=130)
    tk.Label(root, text="MFG").place(x=10, y=160)
    tk.Label(root, text="EXP").place(x=10, y=190)

    e1 = Entry(root)  # pid
    e1.place(x=140, y=10)

    e2 = Entry(root)  # pname
    e2.place(x=140, y=40)

    e3 = Entry(root)  # categoryname
    e3.place(x=140, y=70)

    e4 = Entry(root)  # price
    e4.place(x=140, y=100)

    e5 = Entry(root)  # quantity
    e5.place(x=140, y=130)

    e6 = Entry(root)  # MFG
    e6.place(x=140, y=160)

    e7 = Entry(root)  # EXP
    e7.place(x=140, y=190)
    def des():
        root.destroy()

    Button(root, text="Close", command=des, height=3, width=10).place(x=550, y=500)
    # Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=230)
    Button(root, text="update", command=update, height=3, width=13).place(x=140, y=230)
    # Button(root, text="Delete", command=delete, height=3, width=10).place(x=100, y=230)

    cols = ('P_id', 'P_name', 'P_cat', 'P_price', 'Quantity', 'MFG', 'EXP')
    listBox = ttk.Treeview(root, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col, anchor=tkinter.CENTER)
        listBox.column(col, width=70, minwidth=50, anchor=tkinter.CENTER)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=200)
    show()
    listBox.bind('<Double-Button-1>', GetValue)
    listBox.place(x=20, y=320)
    root.mainloop()

#pft is remaining
def proceed_for_transaction():
    root = Tk()
    root.title("bill slip")
    root.geometry('1280x720')
    f1 = "californian 10 "

    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="Sumit_8983",
        database="shop_management_system"
    )
    mycursor = mydb.cursor()

    # ======================variable=================
    c_name = StringVar()
    c_phone = StringVar()
    pro_id = IntVar()
    global item
    item = StringVar()
    Rate = IntVar()
    category = StringVar()
    # mycursor.execute(f"select c_id from category where cname = {category.get()}")
    # p_cat = mycursor.fetchall()
    # p_cat_id = p_cat[0]
    # pro_cat = p_cat_id[0]
    global quantity
    quantity = IntVar()
    global bill_no
    bill_no = StringVar()
    x = random.randint(1000, 9999)
    bill_no.set(str(x))
    global l
    l = []

    # =========================Functions================================

    def additm():
        global m,n
        mycursor.execute(f"select P_price from product where P_name = '{item.get()}'")
        rate = mycursor.fetchall()
        # print(f"rate:- ",rate)
        i_rate = rate[0]
        # print(f"i_rate:- ",i_rate)
        item_price = i_rate[0]
        # print(f"item_price:-",item_price)
        n = item_price
        m = quantity.get() * n
        l.append(m)
        if item.get() != '':
            textarea.insert((10.0 + float(len(l) - 1)), f"{item.get()}\t\t{quantity.get()}\t\t{m}\n")
        else:
            messagebox.showerror('Error', 'Please enter item')

    def gbill():

        mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Sumit_8983",
            database="shop_management_system"
        )
        mycursor = mydb.cursor()
        if c_name.get() == "" or c_phone.get() == "":
            messagebox.showerror("Error", "Customer detail are must")
        else:
            textAreaText = textarea.get(10.0, (10.0 + float(len(l))))
            welcome()
            textarea.insert(END, textAreaText)
            textarea.insert(END, f"\n======================================")
            textarea.insert(END, f"\nTotal Pay bill Amount :\t\t      {sum(l)}")
            textarea.insert(END, f"\n\n======================================")
            # #Fetching the previous Product Quantity
            # print(f"select P_Quantity from product where P_name = '{item.get()}'")
            mycursor.execute(f"select P_Quantity from product where P_name = '{item.get()}'")
            previous_Quantity = mycursor.fetchall()
            p_q = previous_Quantity[0]
            previous_Quantity = p_q[0]
            # print(previous_Quantity)
            final_quantity = previous_Quantity - quantity.get()
            # print(final_quantity)

            #Fetching the Product ID
            # print(f"select P_id from product where P_name = '{item.get()}'")
            mycursor.execute(f"select P_id from product where P_name = '{item.get()}'")
            pid = mycursor.fetchall()
            PID = pid[0]
            P_id = PID[0]
            # -print(P_id)
            # sql = f"update product set P_Quantity = {final_quantity} where P_name='{item.get()}'"
            # print(f"update product set P_Quantity = {final_quantity} where P_name='{item.get()}'")
            # mycursor.execute(f"update product set P_Quantity = {final_quantity} where P_name='{item.get()}'")
            mycursor.execute(f"update product set P_Quantity = {final_quantity} where P_id={pro_id.get()}")


    def clear():
        c_name.set('')
        c_phone.set('')
        item.set('')
        Rate.set(0)
        quantity.set(0)
        welcome()

    def exit():
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            root.destroy()



    def welcome():
        textarea.delete(1.0, END)
        textarea.insert(END, "\t     Welcome to Shop")
        textarea.insert(END, f"\n\nBill Number:\t\t{bill_no.get()}")
        textarea.insert(END, f"\nCustomer Name:\t\t{c_name.get()}")
        textarea.insert(END, f"\nPhone Number:\t\t{c_phone.get()}")
        textarea.insert(END, f"\n\n======================================")
        textarea.insert(END, "\nProduct\t\tQTY\t\tPrice")
        textarea.insert(END, f"\n======================================\n")
        textarea.configure(font='arial 15 bold')

    title = Label(root, pady=2, text="Billing Software", bd=12, font=f1, relief=GROOVE, justify=CENTER)
    title.pack(fill=X)

    # =================Product Frames=================
    F1 = LabelFrame(root, bd=10, relief=GROOVE, text='Customer Details', font=f1)
    F1.place(x=0, y=80, relwidth=1)

    cname_lbl = Label(F1, text='Customer Name', font=f1).grid(row=0, column=0, padx=20, pady=5)
    cname_txt = Entry(F1, width=15, textvariable=c_name, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=0,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=5)

    cphone_lbl = Label(F1, text='Phone No. ', font=f1).grid(row=0, column=2, padx=20, pady=5)
    cphone_txt = Entry(F1, width=15, font='arial 15 bold', textvariable=c_phone, relief=SUNKEN, bd=7).grid(row=0,
                                                                                                           column=3,
                                                                                                           padx=10,
                                                                                                           pady=5)

    F2 = LabelFrame(root, text='Product Details', font=f1)
    F2.place(x=20, y=180, width=630, height=500)

    itm = Label(F2, text='Product Name', font=f1).grid(
        row=1, column=0, padx=30, pady=20)
    itm_txt = Entry(F2, width=20, textvariable=item, font=f1, relief=SUNKEN, bd=7).grid(row=1, column=1, padx=10,
                                                                                        pady=20)
    itm = Label(F2, text='Product id', font=f1).grid(
        row=0, column=0, padx=40, pady=15)
    itm_txt = Entry(F2, width=20, textvariable=pro_id, font=f1, relief=SUNKEN, bd=6).grid(row=0, column=1, padx=10,
                                                                                        pady=20)

    # cat = Label(F2, text='Category Name', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen').grid(
    # row=1, column=0, padx=30, pady=20)
    # cat_txt = Entry(F2, width=20,textvariable=category, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=1, column=1, padx=10,pady=20)

    # rate= Label(F2, text='Product Rate', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen').grid(
    # row=1, column=0, padx=30, pady=20)
    # rate_txt = Entry(F2, width=20,textvariable=Rate, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=1, column=1, padx=10,pady=20)

    n = Label(F2, text='Product Quantity', font=f1).grid(
        row=2, column=0, padx=30, pady=20)
    n_txt = Entry(F2, width=20, textvariable=quantity, font=f1, relief=SUNKEN, bd=7).grid(row=2, column=1, padx=10,
                                                                                          pady=20)

    # ========================Bill area================
    F3 = Frame(root, relief=GROOVE, bd=10)
    F3.place(x=700, y=180, width=500, height=500)

    bill_title = Label(F3, text='Bill Area', font=f1, bd=7, relief=GROOVE).pack(fill=X)
    scrol_y = Scrollbar(F3, orient=VERTICAL)
    textarea = Text(F3, yscrollcommand=scrol_y)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=textarea.yview)
    textarea.pack()
    welcome()
    # =========================Buttons======================
    btn1 = Button(F2, text='Add item', font=f1, command=additm, padx=5, pady=10, width=15)
    btn1.grid(row=3, column=0, padx=10, pady=30)
    btn2 = Button(F2, text='Generate Bill', font=f1, command=gbill, padx=5, pady=10, width=15)
    btn2.grid(row=3, column=1, padx=10, pady=30)
    btn3 = Button(F2, text='Clear', font=f1, padx=5, pady=10, command=clear, width=15)
    btn3.grid(row=4, column=0, padx=10, pady=30)
    btn4 = Button(F2, text='Exit', font=f1, padx=5, pady=10, command=exit, width=15)
    btn4.grid(row=4, column=1, padx=10, pady=30)
    root.mainloop()

#pft is remaining
def trans_history():
    trans_history_window = Tk()
    trans_history_window.title("Transaction History")
    trans_history_window.geometry("400x300")

    # def save_bill():
    #     op = messagebox.askyesno("Save bill", "Do you want t o save the Bill?")
    #     if op > 0:
    #         bill_details = textarea.get('1.0', END)
    #         f1 = open("bills/" + str(bill_no.get()) + ".txt", "w")
    #         f1.write(bill_details)
    #         f1.close()
    #         messagebox.showinfo("Saved", f"Bill no, :{bill_no.get()} Saved Successfully")
    #     else:
    #         return
    # save_bill()

    trans_history_window.mainloop()

#working small changes remaining
def stock_report():
    roott = tkinter.Tk()
    roott.title("Stock List")
    roott.geometry('700x500')
    options_list = ["food", "grocery", "clothes","medicine","furniture","electronic","book"]
    value_inside = tkinter.StringVar(roott)
    value_inside.set("Select an Option")
    question_menu = tkinter.OptionMenu(roott, value_inside, *options_list)
    question_menu.place(x=20, y=40)
    def des():
        roott.destroy()

    def sto():

        def show():
            mysqldb = mysql.connector.connect(host="localhost", username="root", password="Sumit_8983",
                                              database="shop_management_system")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT c_id FROM category where c_name = '{}'".format(value_inside.get()))
            records = mycursor.fetchall()
            print(records)
            rec = records[0]
            r = rec[0]
            pid = r
            # print(pid)
            mycursor.execute(
                "Select P_id,P_name,P_cat,P_price,P_Quantity,P_mfg,P_expi from product where P_cat = {}".format(pid))
            res = mycursor.fetchall()
            # print(res)

            cols = ('P_id', 'P_name', 'P_cat', 'P_price', 'Quantity', 'MFG', 'EXP')
            listBox = ttk.Treeview(roott, columns=cols, show='headings')
            for col in cols:
                listBox.heading(col, text=col, anchor=tkinter.CENTER)
                listBox.column(col, width=70, minwidth=50, anchor=tkinter.CENTER)
                listBox.grid(row=1, column=0, columnspan=2)
                listBox.place(x=10, y=150)

            for i, (P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi) in enumerate(res, start=1):
                listBox.insert("", "end", values=(P_id, P_name, P_cat, P_price, P_Quantity, P_mfg, P_expi))
                mysqldb.close()

        Button(roott, text="Close", width=15, command=des).place(x=40, y=420)

        show()

    submit_button = tkinter.Button(roott, text='Submit', command=sto)
    submit_button.place(x=220, y=40)

    roott.mainloop()#

#remaining
def sales_report():
    sales_report_window = Tk()
    sales_report_window.title("Sales Report")
    sales_report_window.geometry("400x300")

    # Program Logic

    sales_report_window.mainloop()


# Giving Title to the System
login_page.title("Shop management System")
# Adding welcome text
wel_txt = Label(login_page, text="Welcome to the Shop Management System!", relief=RAISED, borderwidth=4,
                bg="peach puff", padx=5, pady=5, font=f_head)
wel_txt.place(x=50, y=10)
# Adding the password text field
pass_label = Label(login_page, text="Enter the Password:-", relief=SUNKEN, font=f1, pady=5, padx=5)
pass_label.place(x=10, y=50)
# Adding the password entry field
passvalue = StringVar()
pass_entry = Entry(login_page, textvariable=passvalue, font=f1, show="*")
pass_entry.place(x=150, y=50)
# Adding the login button
submit_button = Button(text="Log In", font=f1, pady=5, padx=5, command=logIn)
submit_button.place(x=230, y=80)
# Adding the reset button
reset_button = Button(text="Reset", font=f1, pady=5, padx=5, command=reset_tab)
reset_button.place(x=150, y=80)
mainloop()
