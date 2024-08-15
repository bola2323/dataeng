import pyodbc

SERVER = 'BAMI\SQLEXPRESS01'
DATABASE = 'BAMINEWDB'

connectionString = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"  # Use Windows Authentication
)

try:
    conn = pyodbc.connect(connectionString)
    print("Connection successful")
except pyodbc.Error as e:
    print("Error while connecting to the database:", e)

cursor = conn.cursor()

SQLCommand = ("INSERT INTO dbo.product_table (productid, productname, productdescription, productvalue) VALUES (?,?,?,?);") 
Values = ['001','gold','metallic', 3000]

#Processing Query    
cursor.execute(SQLCommand,Values)

conn.commit()
print("Data Successfully Inserted")   
conn.close()