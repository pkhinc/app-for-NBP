import sys
import dateutil.parser
import requests

print("CURRENCY CALCULATOR")

try: 
    currency = sys.argv[1] 
except IndexError: 
    currency = input('Podaj walute: ')

currency = currency.upper() 

try:
    date_as_str = sys.argv[2] 
except: 
    date_as_str = input("Podaj date: ") 


try:
    date = dateutil.parser.parse(date_as_str)
except ValueError: 
    print('Invalid date format')
    sys.exit(1)

# covnert date as a string 
date_for_url = date.strftime('%Y-%m-%d') # nastepuje konwertowanie daty na string


url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date_for_url}/?format=json"

# get url
response  =requests.get(url)
if response.status_code == 404: 
    print('Brak danych')
    sys.exit(2)
if not response.ok: 
    print('Unexcpected server response')
    sys.exit(3)

# convert url to nested structure of diaries
json = response.json() 

try:
    rate = json['rates'][0]['mid']  
except (ValueError, KeyError):
    print('Invalid server response')
    sys.exit(4)

print(f"1 {currency} = {rate} PLN w dniu {date.day}/{date.month}/{date.year}")