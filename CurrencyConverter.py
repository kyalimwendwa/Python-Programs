from forex-python.converter
import CurrencyRates
cr=CurrencyRates()
amount=int(input("Enter amount you want to convert"))
from_currency=input("Enter currency code that has to be converted").upper()
to_currency=input("Enter currency code  to be converted to").upper()

print("You are converting",amount,from_currency,"to",to_currency,".")
output=cr.convert(from_currency,to_currency,amount)
print("The converted rate is",output)