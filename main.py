import tkinter
from tkinter import *
import mysql.connector
from datetime import datetime

# Defining root window
root = tkinter.Tk()
root.title("Database Management System Application")
root.geometry("500x500")
root.resizable(0, 0)
root.iconbitmap("database_icon.ico")


# Functions

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
        output_label.config(text="Error! Please enter a number")



# GUI Layout

# Define frame
entry_frame = tkinter.LabelFrame(root, text="Inventory Database", labelanchor="nw")
entry_frame.pack(ipadx=20, ipady=20, padx=10, pady=10, expand=True, fill='both')


# Entry frame layout
description_text = "Please enter the descriptions below:"
description_label = tkinter.Label(entry_frame, text=description_text)
description_label.grid(row=0, column=0, columnspan=2, pady=12, sticky="WE")


item_label = tkinter.Label(entry_frame, text="Item", width=25)
item_label.grid(row=1, column=0)
item_input = tkinter.Entry(entry_frame, borderwidth=2, width=45)
item_input.grid(row=1, column=1, pady=12, ipady=4, padx=(8,0))

quantity_label = tkinter.Label(entry_frame, text="Quantity")
quantity_label.grid(row=2, column=0, sticky="WE")
quantity_input = tkinter.Entry(entry_frame, borderwidth=2)
quantity_input.grid(row=2, column=1, pady=12, ipady=4, padx=(8,0), sticky="WE")

amount_label = tkinter.Label(entry_frame, text="Amount")
amount_label.grid(row=3, column=0, sticky="WE")
amount_input = tkinter.Entry(entry_frame, borderwidth=2)
amount_input.grid(row=3, column=1, pady=12, ipady=4, padx=(8,0), sticky="WE")

submit_button = tkinter.Button(entry_frame, text="Submit", command=output_number)
submit_button.grid(row=4, column=1, pady=12, ipady=4, padx=(8,0), sticky="WE")

# Output Label
output_label = tkinter.Label(entry_frame, text='')
output_label.grid(row=5, column=0, columnspan=2, ipady=4, sticky="WE")

# Running the main loop
root.mainloop()
