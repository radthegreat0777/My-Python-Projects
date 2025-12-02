#Currency Converter Using an API
import requests

amount = 1008989.50
from_currency = "LKR"
to_currency = "USD"
api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

response = requests.get(api_url)
data = response.json()

if to_currency in data['rates']:
    conversion_rate = data['rates'][to_currency]
    converted_amount = amount * conversion_rate
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print(f"Conversion rate for {to_currency} not found.")
