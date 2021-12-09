from tkinter import *
import sqlite3
import tkinter.ttk as ttk

root = Tk()

root.title("Shipping Validation Virtual Form")
root.geometry("600x600")

# Create a database
conn = sqlite3.connect('Shipping_Validation.db')

# Create cursor
c = conn.cursor()


# Create database

'''c.execute(""" CREATE TABLE validation (
    time text,
    amount text,
    product_code text,
    production_date text,
    skid_ID text,
    colour text,
    label text,
    seal text,
    t_initial text,
    initials text
)""")
'''

def query():
    newWindow1 = Toplevel(root)
    newWindow1.geometry("1200x700")
    newWindow1.title("Shipping Validation Search Query")
    
    def Search():
    
        if SEARCH.get() != "":
            tree.delete(*tree.get_children())
            conn = sqlite3.connect("Shipping_Validation.db")
            cursor = conn.cursor() 
            cursor.execute("SELECT * FROM `validation` WHERE `production_date` LIKE ? AND `product_code` LIKE ?", ('%'+str(SEARCH.get())+'%', '%'+str(SEARCH2.get())+'%'))
            records = cursor.fetchall()

        for data in records:
            tree.insert('', 'end', values=(data))
        
        cursor.close()
        conn.close()

    def Reset():
        conn = sqlite3.connect("Shipping_Validation.db")
        cursor = conn.cursor()
        tree.delete(*tree.get_children())
        cursor.execute("SELECT *, oid FROM validation ")
        records = cursor.fetchall()

        for data in records:
            tree.insert('', 'end', values=(data))
            
        cursor.close()
        conn.close()

        search.delete(0, 'end')
        search2.delete(0, 'end')


    SEARCH = StringVar()
    SEARCH2 = StringVar()

    # Frame
    Top = Frame(newWindow1, width = 500, bd =1, relief=SOLID)
    Top.pack(side = TOP)
    TopFrame = Frame(newWindow1, width = 500)
    TopFrame.pack(side = TOP)
    TopForm = Frame(TopFrame, width = 300)
    TopForm.pack(side = LEFT, pady = 10)
    TopMargin = Frame(TopFrame, width = 260)
    TopMargin.pack(side = LEFT)
    MidFrame = Frame(newWindow1, width = 500)
    MidFrame.pack(side = TOP)

    lbl_title = Label(Top, width = 500, text = "Shipping Validation Search Query")
    lbl_title.pack(side = TOP, fill = X)

    scrollbarx = Scrollbar(MidFrame, orient = HORIZONTAL)
    scrollbary = Scrollbar(MidFrame, orient = VERTICAL)
    tree = ttk.Treeview(MidFrame, column = ("Time", "Amount", "Product Code", "Production Date", "Skid Number", "Colour", "Label", "Seal", "Temperature", "Employee Responsible"), selectmode = "extended", height = 400, yscrollcommand=scrollbary.set, xscrollcommand = scrollbarx.set)
    scrollbary.config(command = tree.yview)
    scrollbary.pack(side = RIGHT, fill = Y)
    scrollbarx.config(command = tree.xview)
    scrollbarx.pack(side = BOTTOM, fill=X)
    tree.heading("Time", text = "Time", anchor = W)
    tree.heading("Amount", text = "Amount", anchor = W)
    tree.heading("Product Code", text = "Product Code", anchor = W)
    tree.heading("Production Date", text = "Production Date", anchor = W)
    tree.heading("Skid Number", text = "Skid Number", anchor = W)
    tree.heading("Colour", text = "Colour", anchor = W)
    tree.heading("Label", text = "Label", anchor = W)
    tree.heading("Seal", text = "Seal", anchor = W)
    tree.heading("Temperature", text = "Temperature", anchor = W)
    tree.heading("Employee Responsible", text = "Employee Responsible", anchor = W)
    tree.column('#0', stretch = NO, minwidth = 0, width = 0)
    tree.column('#1', stretch = NO, minwidth = 0, width = 100)
    tree.column('#2', stretch = NO, minwidth = 0, width = 80)
    tree.column('#3', stretch = NO, minwidth = 0, width = 120)
    tree.column('#4', stretch = NO, minwidth = 0, width = 120)
    tree.column('#5', stretch = NO, minwidth = 0, width = 120)
    tree.column('#6', stretch = NO, minwidth = 0, width = 80)
    tree.column('#7', stretch = NO, minwidth = 0, width = 80)
    tree.column('#8', stretch = NO, minwidth = 0, width = 80)
    tree.column('#9', stretch = NO, minwidth = 0, width = 120)
    tree.column('#10', stretch = NO, minwidth = 0, width = 170)
    tree.pack()

    # Database

    conn = sqlite3.connect("Shipping_Validation.db")
    cursor = conn.cursor()

    cursor.execute("SELECT *, oid FROM validation ")
    records = cursor.fetchall()

    for data in records:
        tree.insert('', 'end', values=(data))
        
    cursor.close()
    conn.close()

    search_Label = Label(TopForm, text = "Production Date:")
    search_Label.grid(row = 0, column = 0)

    search = Entry(TopForm, textvariable = SEARCH)
    search.grid(row = 0, column = 1)

    search2_label = Label(TopForm, text = "Product Code:")
    search2_label.grid(row = 1, column = 0)

    search2 = Entry(TopForm, textvariable = SEARCH2)
    search2.grid(row = 1, column = 1)

    btn_search = Button(TopForm, text ="Search", bg ="#006dcc", command = Search)
    btn_search.grid(row = 3, column = 1)

    btn_reset = Button(TopForm, text="Reset", bg = "#006dcc", command = Reset)
    btn_reset.grid(row = 4, column = 1)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

def submit():
    # Create a database
    conn = sqlite3.connect('Shipping_Validation.db')
    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO validation VALUES (:time, :amount, :product_code, :production_date, :skid_ID, :colour, :label, :seal, :t_initial, :initials)",
        {
            'time' : time.get(),
            'amount' : amount.get(),
            'product_code' : p_code.get(),
            'production_date' : p_date.get(),
            'skid_ID' : skid_ID.get(),
            'colour' : colour.get(),
            'label' : label.get(),
            'seal' : seal.get(),
            't_initial' : t_initial.get(),
            'initials' : initials.get()
        })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    time.delete(0, END)
    amount.delete(0, END)
    p_code.delete(0, END)
    p_date.delete(0, END)
    skid_ID.delete(0, END)
    colour.delete(0, END)
    label.delete(0, END)
    seal.delete(0, END)
    t_initial.delete(0, END)
    initials.delete(0, END)


time = Entry(root, width = 30)
time.grid(row = 0, column = 1, padx = 20)
timelabel = Label(root, text = "Time:").grid(row = 0, column = 0)


amount = Entry(root, width = 30)
amount.grid(row = 1, column = 1)
amountlabel = Label(root, text = "Amount:").grid(row = 1, column = 0)

p_code = Entry(root, width = 30)
p_code.grid(row = 2, column = 1, padx = 20)
p_codelabel = Label(root, text = "Product Code:").grid(row = 2, column = 0)

p_date = Entry(root, width = 30)
p_date.grid(row = 3, column = 1, padx = 20)
p_datelabel = Label(root, text = "Production Date (MM/DD/YYYY):").grid(row = 3, column = 0)

skid_ID = Entry(root, width = 30)
skid_ID.grid(row = 4, column = 1, padx = 20)
skid_IDlabel = Label(root, text = "Skid ID:").grid(row = 4, column = 0)

colour = Entry(root, width = 30)
colour.grid(row = 5, column = 1, padx = 20)
colourlabel = Label(root, text = "Colour (P/F):").grid(row = 5, column = 0)

label = Entry(root, width = 30)
label.grid(row = 6, column = 1, padx = 20)
labellabel = Label(root, text = "Label (P/F):").grid(row = 6, column = 0)

seal = Entry(root, width = 30)
seal.grid(row = 7, column = 1, padx = 20)
seallabel = Label(root, text = "Seal (P/F):").grid(row = 7, column = 0)

t_initial = Entry(root, width = 30)
t_initial.grid(row = 8, column = 1)
t_initiallabel = Label(root, text = "Initial Temperature").grid(row = 8, column = 0)

initials = Entry(root, width = 30)
initials.grid(row = 9, column = 1)
initiallabel = Label(root, text = "Person Responsible:").grid(row = 9, column = 0)

submit_btn = Button(root, text="Add Record To Database", command = submit)
submit_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx=100)

query_btn = Button(root, text = "Show Records", command = query)
query_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx=100)

root.mainloop()