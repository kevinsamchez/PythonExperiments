'''
Currency converter using the requests package and fixer API https://apilayer.com/marketplace/fixer-api#
API key: NdUqBM1G5hVn84mA3DtZeHf8zywGNl8n
https://hackr.io/blog/python-projects
'''

import requests
from datetime import datetime

def convertCurrency():
    initCurrencyPrompt = 'Enter an initial currency: '
    targetCurrencyPrompt = 'Enter a target currency: '
    datePrompt = 'Enter in desired date (DD-MM-YYYY) to check for currency conversion or leave empty for current date: '

    date = checkValiddate(datePrompt)
    initCurrency = checkValidCodes(initCurrencyPrompt)
    targetCurrency = checkValidCodes(targetCurrencyPrompt)

    while True:
        try:
            amount = float(input('Enter in the amount to convert: '))
        except ValueError:
            "Enter in a number"
            continue

        if amount > 0:       
            break
        else:
            print('A value greater than 0 must be entered.')
            continue    

    if date != '':
        url = ('https://api.apilayer.com/fixer/convert?to='
              + targetCurrency + '&from=' + initCurrency +
            '&amount=' + str(amount) + '&date=' + str(date))
    else:
        url = ('https://api.apilayer.com/fixer/convert?to='
              + targetCurrency + '&from=' + initCurrency +
            '&amount=' + str(amount))        
    
    payload = {}
    headers= {
        "apikey": "NdUqBM1G5hVn84mA3DtZeHf8zywGNl8n"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    statusCode = response.status_code
    result = response.json()

    if statusCode == 200:
        print(f'${amount:.2f} {initCurrency} is ${result["result"]:.2f} {targetCurrency} on {datetime.strptime(result["date"],"%Y-%m-%d").date():%d-%m-%Y}')
    else:
        print('Something went wrong!')

def currencyCodes():
#retrieve valid three letter currency codes from the API
    url = "https://api.apilayer.com/fixer/symbols"

    payload = {}
    headers= {
        "apikey": "NdUqBM1G5hVn84mA3DtZeHf8zywGNl8n"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.json()

    if status_code == 200:
        return result['symbols'].keys()
    else:
        print('Something went wrong!')

def checkValidCodes(prompt):
#checks the entered currency is valid according to the three letter abbreviations provided by the API
    global validCurrencies
    while True:
        currency = str.upper(input(prompt))
        if currency in validCurrencies:
            return currency
        else:
            print('A valid three letter abbreviation is required.')
            continue

def checkValiddate(prompt):
#checks entered dates are valid dates
    while True:
        try:
            date = input(prompt)
            if date != '':
                date = datetime.strptime(date,'%d-%m-%Y').date() #this converts it back to the default which is yyyy-mm-dd
                return date
            else:
                return date
        except ValueError:
            print('This is not a valid date')
            continue

validCurrencies = currencyCodes()
convertCurrency()