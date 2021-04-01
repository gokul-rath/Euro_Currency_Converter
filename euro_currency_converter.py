#Currency converter for Euro
def desiredDate(dates): #entered value must be a string
# Input Rapidapikey provided by the rapidapi webpage
    RAPIDAPIKEY = 'd88ac81114msh89e702e586cd793p16570djsn90c636b78795'  
    dates = str(dates)
# import
    import http.client  
    import json 
    import pandas as pd
    import numpy as np
    from datetime import date
    import matplotlib.pyplot as plt

# Establish the connection to the particular API 
    conn = http.client.HTTPSConnection("currency-converter5.p.rapidapi.com")

    headers = {'x-rapidapi-host': "currency-converter5.p.rapidapi.com",'x-rapidapi-key': RAPIDAPIKEY}

# First we will find the List of available currencies:
# The select API have been provided free of cost and is available for everyone
    conn.request("GET", "/currency/list", headers=headers)

    resp  = conn.getresponse()
    data = resp.read().decode("utf-8") 
    currency = json.loads(data)


# Next, we will check the currency exchange rate based on 1 euro
#This means that we will obtain all the currencies values equal to 1 euro 
    conn.request("GET", "/currency/convert", headers=headers)
    resp = conn.getresponse()
    data2 = resp.read().decode("utf-8")
    convert = json.loads(data2)

#change the data to a dataframe  
    currency_df= pd.DataFrame(currency)
    print(currency_df)

    print("Base amount Value: ",convert['amount'])

    print("Currency Base Name: ",convert['base_currency_name'])

    print("Currency Base Code: ",convert['base_currency_code'])

# we put the current date to have a better visualization of the output
    today = date.today()
    print("Today's date:", today)

    print('\n')
    print('Today, the exchange currency values are:\n')

#change the data to a dataframe
    convert_df= pd.DataFrame(convert['rates'])
    convert_df = convert_df.drop('rate_for_amount')
    print(convert_df)

    print('\n')
    print(dates, "The requested date exchange currency values are:\n")

# prepare the dynamic code so we may choose which date we want to see the currency
    Requesteddate ="/currency/historical/" + dates + ""

    conn.request("GET", Requesteddate, headers=headers)
    resp = conn.getresponse()
    data = resp.read().decode("utf-8")
    historical = json.loads(data)
    
#change the data to a dataframe
    historical_df= pd.DataFrame(historical['rates'])
    historical_df = historical_df.drop('rate_for_amount')
    print(historical_df)

