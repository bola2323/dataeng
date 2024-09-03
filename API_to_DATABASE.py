# API to DATABASE—
import pandas as pd

import requests

import json

import csv

import pyodbc

from sqlalchemy import create_engine

url = 'https://informed-data-challenge.netlify.app/api/breweries'

# Define the CSV file and header

csv_file = 'breweries_data.csv'

csv_header = ['Name', 'Street', 'City', 'State', 'Country', 'Phone', 'Website']

 

# Get request function



# data = get_request(url)
 

def get_request(data_url: str):

    response = requests.get(data_url)

    return response.json()



# Function to manipulate and retrieve the data

# brewery_data_list = brewery_loop(data)

def brewery_loop(data):

    brewery_info_list = []

    num_Breweries_data = len(data["data"])

    for i in range(num_Breweries_data):

        New_Breweries_data = {}

        # name, street, city, state, country, phone number, and website

        for key, value in data.items():

            New_Breweries_data.update(value[i])

       

        # Extract relevant information

        brewery_info = [

            New_Breweries_data.get('name', ''),

            New_Breweries_data.get('street', ''),

            New_Breweries_data.get('city', ''),

            New_Breweries_data.get('state', ''),

            New_Breweries_data.get('country', ''),

            New_Breweries_data.get('phone', ''),

            New_Breweries_data.get('website_url', '')

        ]

        brewery_info_list.append(brewery_info)

   

    return brewery_info_list

 

# Function for CSV file

def make_csv(data_list, header:list, filename:str):

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:

        # Create a CSV writer object

        csv_writer = csv.writer(csvfile)

 

        # Write the header to the CSV file

        csv_writer.writerow(header)

 

        # Write the brewery information to the CSV file

        csv_writer.writerows(data_list)

        return  csv_writer

       

# Call the Get request function

data = get_request(url)

 

# Call the loop function

brewery_data_list = brewery_loop(data)

 

# Call the CSV function

make_csv(brewery_data_list, csv_header, csv_file)

 

df = pd.read_csv(csv_file)

# path = r'C:\Python\Live Scripts\Ops_Migration\destination_folder'
path = r"C:\Users\adebb\destination_folder"

# df.to_csv(path +'/christian.csv')
df.to_csv(path +'/bamyat_sales.csv')
print("file now saved")

 

 

SERVER = 'BAMI\SQLEXPRESS01'
DATABASE = 'BAMINEWDB'
USERNAME = "BAMI\adebb"
PASSWORD = ""
Trusted_Connection = "yes"
connectionString = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"  # Use Windows Authentication
)

try:
    # cnxn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=myDB;Trusted_Connection=yes;')
    params = 'DRIVER={ODBC Driver 17 for SQL Server};'+'SERVER='+SERVER+';DATABASE='+DATABASE+';Trusted_Connection='+ Trusted_Connection
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    conn = pyodbc.connect(connectionString)
    print("Connection successful")
except pyodbc.Error as e:
    print("Error while connecting to the database:", e)

cursor = conn.cursor()

 

 

# df.to_sql('dbo.Kabo', con=engine, if_exists='append')
df.to_sql('dbo.Kabo', con=engine,)

print(f'Data has been written to {csv_file}')