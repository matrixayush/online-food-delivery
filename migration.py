import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',  # Add your MySQL password if applicable
    database='query run'  # Replace with the actual database name
)

if mydb.is_connected():
    print("Connected to the database")

# Create a cursor object
mycursor = mydb.cursor()

# Create CUSTOMER table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS CUSTOMER (
        cust_num INT PRIMARY KEY,
        cust_lname VARCHAR(50),
        cust_fname VARCHAR(50),
        cust_balance DECIMAL(10, 2)
    )
""")

# Create PRODUCT table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS PRODUCT (
        prod_num INT PRIMARY KEY,
        prod_name VARCHAR(100),
        price DECIMAL(10, 2)
    )
""")

# Create INVOICE table
mycursor.execute("""
        CREATE TABLE IF NOT EXISTS INVOICE (
        inv_num INT PRIMARY KEY,
        prod_num INT,
        cust_num INT,
        inv_date DATE,
        unit_sold INT,
        inv_amount DECIMAL(10, 2),
        FOREIGN KEY (prod_num) REFERENCES PRODUCT(prod_num),
        FOREIGN KEY (cust_num) REFERENCES CUSTOMER(cust_num)
    )
""")

print("Tables created successfully")

# Close the connection
mydb.close()
