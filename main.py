import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import mysql.connector
from datetime import datetime

# Defining root window
root = tkinter.Tk()
root.title("Database Management System Application")
root.geometry("1000x375")
root.resizable(0, 0)
root.iconbitmap("database_icon.ico")

# Functions
def show_values():
    # Establishing a connection to the database
    database = mysql.connector.connect(host="127.0.0.1", user="root", password="managedatabase",
                                       database="restaurant_db")

    # Creating a cursor instance
    cursor = database.cursor()

    # Inserting data in the treeview
    cursor.execute("SELECT * FROM inventory")

    # Initiaing count for iid of inserting in the values
    count = 0

    # Show data in table
    for row in cursor:
        tree_view.insert(parent="", index="end", iid=count, text="", values=(row[0], row[1], row[2], row[3], row[4]))
        count += 1

def submit(amount):
    # Establishing a connection to the database
    database = mysql.connector.connect(host="127.0.0.1", user="root", password="managedatabase",
                                       database="restaurant_db")

    # Creating a cursor instance
    cursor = database.cursor()

    # Getting current date
    today_date = datetime.today().strftime('%Y-%m-%d')

    # Inserting values into table
    sql_query = "INSERT INTO inventory (item, quantity, amount, date_of_purchase) VALUES (%s, %s, %s, %s)"
    values = [item_input.get(), quantity_input.get(), amount, today_date]

    # Executing query
    cursor.execute(sql_query, values)

    # Commit to database after updating a database
    database.commit()

    # Label to show user the action result
    strings = item_input.get() + ", " + quantity_input.get() + ", " + str(amount) + ", " + today_date
    output_label.config(text=strings)

    # Close connection
    database.close()

    # Show values in the treeview
    show_values()

    # Clearing all the entry fields
    item_input.delete(0, END)
    quantity_input.delete(0, END)
    amount_input.delete(0, END)


def output_number():
    try:
        # testing whether it is a integer
        float(amount_input.get())
        amount = int(amount_input.get())
        # output_label.config(text=amount)
        submit(amount)
    except ValueError:
        output_label.config(text="Error! Please enter a number in the amount field")



# GUI Layout

# Define frame
entry_frame = tkinter.LabelFrame(root, text="Inventory Database", labelanchor="nw", width=500)
results_frame = tkinter.Frame(root, width=500)

entry_frame.pack(ipadx=10, ipady=5, padx=5, pady=10, side=LEFT, expand=False, fill=BOTH)
results_frame.pack(ipadx=5, ipady=6, padx=5, pady=10, expand=False, fill=BOTH)

# Entry frame layout
description_text = "Please enter the descriptions below:"
description_label = tkinter.Label(entry_frame, text=description_text)
item_label = tkinter.Label(entry_frame, text="Item", width=25)
item_input = tkinter.Entry(entry_frame, borderwidth=2, width=45)
quantity_label = tkinter.Label(entry_frame, text="Quantity")
quantity_input = tkinter.Entry(entry_frame, borderwidth=2)
amount_label = tkinter.Label(entry_frame, text="Amount")
amount_input = tkinter.Entry(entry_frame, borderwidth=2)
submit_button = tkinter.Button(entry_frame, text="Submit", command=output_number)
output_label = tkinter.Label(entry_frame, text='')

# Griding the elements onto the frame
description_label.grid(row=0, column=0, columnspan=2, pady=12, sticky="WE")
item_label.grid(row=1, column=0)
item_input.grid(row=1, column=1, pady=12, ipady=4, padx=(8,0))
quantity_label.grid(row=2, column=0, sticky="WE")
quantity_input.grid(row=2, column=1, pady=12, ipady=4, padx=(8,0), sticky="WE")
amount_label.grid(row=3, column=0, sticky="WE")
amount_input.grid(row=3, column=1, pady=12, ipady=4, padx=(8,0), sticky="WE")
submit_button.grid(row=4, column=1, pady=12, ipady=4, padx=(8,0), sticky="WE")
output_label.grid(row=5, column=0, columnspan=2, ipady=4, sticky="WE")

# Results Frame layout
# Creating tree view widget
tree_view = ttk.Treeview(results_frame, selectmode="extended", height=350)
tree_view.pack(ipady=5, expand=True, fill=BOTH)

# Creating columns
tree_view["columns"] = ("item_id", "item", "quantity", "amount", "date_of_purchase")

# Format columns
tree_view.column("#0", width=0, stretch=NO)
tree_view.column("item_id", anchor=CENTER, width=40, minwidth=40, stretch=NO)
tree_view.column("item", anchor=W, width=150, minwidth=100, stretch=NO)
tree_view.column("quantity", anchor=W, width=80, minwidth=80, stretch=NO)
tree_view.column("amount", anchor=CENTER, width=80, minwidth=80, stretch=NO)
tree_view.column("date_of_purchase", anchor=W, width=139, minwidth=100, stretch=NO)

# Create Headings
tree_view.heading("#0", text="0")
tree_view.heading("item_id", text="ID", anchor=CENTER)
tree_view.heading("item", text="Item", anchor=W)
tree_view.heading("quantity", text="Quantity", anchor=W)
tree_view.heading("amount", text="Amount", anchor=CENTER)
tree_view.heading("date_of_purchase", text="Date of transaction", anchor=W)


# Running the main loop
root.mainloop()
