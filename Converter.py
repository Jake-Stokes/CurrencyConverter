# import the libraries
import requests

# url to reference api containing real time exchange rates of global currencies
url = 'https://api.exchangerate-api.com/v4/latest/USD'


class CurrencyConverter:

    def __init__(self, url):

        # gets the data from the target url and converts it to JSON format
        self.data = requests.get(url).json()

        # sets the currencies equal to the rates in the JSON file
        self.currencies = self.data['rates']

    def convert(self, input_currency, output_currency, amount):

        # sets the initial amount to the function input
        initial_amount = amount

        # check to see if the amount is in USD ($), USD is the base for this function
        if amount != 'USD':
            amount = (amount / self.currencies[input_currency])

        # converts the amount back to the output currency
        # limits the precision of the output to 4 decimal places
        value = round(amount * self.currencies[output_currency], 4)

        # print out the data
        print(str(initial_amount) + ' ' + input_currency + ' = ' + str(value) + ' ' + output_currency)


# test case for function and class

Cur1 = input('Starting Currency')
Cur2 = input('To Currency')
Amnt = float(input('Amount'))

converter = CurrencyConverter(url)
converter.convert(Cur1, Cur2, Amnt)
