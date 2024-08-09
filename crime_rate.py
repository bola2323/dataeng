import csv
def load_data(filename):
    my_list = []
    with open(filename) as crime_rates:
       crime_rates_data = csv.reader(crime_rates, delimiter=',')
       next(crime_rates_data)
       for row in crime_rates_data:
           my_list.append(row)
       return my_list
    
new_list = load_data('crime_rates.csv')
for row in new_list:
    print(row)
     
