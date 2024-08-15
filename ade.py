
import requests
import json
import csv

url = 'https://informed-data-challenge.netlify.app/api/breweries'
# Define the CSV file and header
csv_file = 'breweries_data.csv'
csv_header = ['Name', 'Street', 'City', 'State', 'Country', 'Phone', 'Website']

# Get request function
def get_request(data_url: str):
    response = requests.get(data_url)
    return response.json()



# Function to manipulate and retrieve the data
def brewery_loop(raw_data):
    brewery_info_list = []
    num_Breweries_data = len(raw_data["data"])
    for i in range(num_Breweries_data):
        New_Breweries_data = {}
        # name, street, city, state, country, phone number, and website 
        for key, value in raw_data.items():
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
        

# Call the Get request function
data = get_request(url)

# Call the loop function
brewery_data_list = brewery_loop(data)

# Call the CSV function
make_csv(brewery_data_list, csv_header, csv_file)
print(f'Data has been written to {csv_file}')
