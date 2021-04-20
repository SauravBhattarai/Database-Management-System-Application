import tkinter
from tkinter import *
import mysql.connector

# Establishing a connection to the database
database = mysql.connector.connect(host="127.0.0.1", user="root", password="managedatabase", database="restaurant_db")

# creating a cursor instance
cursor = database.cursor()

# Query to create a table
# cursor.execute("CREATE TABLE inventory (item_id INTEGER AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), quantity VARCHAR(255), amount INTEGER NOT NULL, date_of_purchase DATE NOT NULL)")

# Inserting values into table
# sql_query = "INSERT INTO inventory (item, quantity, amount, date_of_purchase) VALUES (%s, %s, %s, %s)"
# record_1 = ("onions", "10 kgs", 500, "2021-4-19")

# cursor.execute(sql_query, record_1)

# Commiting to database after updating a database
# database.commit()

# Defining root window
root = tkinter.Tk()
root.title("Database Management System Application")
root.geometry("500x500")
root.resizable(0,0)
root.iconbitmap("database_icon.ico")


# GUI Layout

# Define frame
entry_frame = tkinter.LabelFrame(root, text="Inventory Database", labelanchor="n")
entry_frame.pack(ipadx=20, ipady=20, padx=10, pady=10, expand=True, fill='both')

# Entry frame
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

submit_button = tkinter.Button(entry_frame, text="Submit")
submit_button.grid(row=4, column=1, pady=12, ipady=4, padx=(8,0), sticky="WE")

# Running the main loop
root.mainloop()


# Query to delete table
# cursor.execute("DROP TABLE inventory")