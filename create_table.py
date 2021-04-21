import mysql.connector

# Establishing a connection to the database
# database = mysql.connector.connect(host="127.0.0.1", user="root", password="managedatabase", database="restaurant_db")

# Creating a cursor instance
# cursor = database.cursor()

# --------------------------------------------------------------------

# Query to create a table
# cursor.execute("CREATE TABLE inventory (item_id INTEGER AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), quantity VARCHAR(255), amount INTEGER NOT NULL, date_of_purchase DATE NOT NULL)")

# Query to delete table
# cursor.execute("DROP TABLE inventory")

# --------------------------------------------------------------------

# Inserting values into table
# sql_query = "INSERT INTO inventory (item, quantity, amount, date_of_purchase) VALUES (%s, %s, %s, %s)"
# record_1 = ("tomatoes", "10 kgs", 200, today_date)

# cursor.execute(sql_query, record_1)

# Commit to database after updating a database
# database.commit()
