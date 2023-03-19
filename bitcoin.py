import requests, sys

try:
    # first python bitcoin.py n(any number how many bitcoints we want to buy)
    n = float(sys.argv[1])
    #check if n can be converted to float (if converted :)
    if float(n):
        # we request the server to get this api
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json') 
        # then we parse to get the all api information as a dictionary
        bitcoin = response.json()
        # then we convert dict value to str otherwise we can't use replace if the value is not string. and replace comma and convert float
        rate = float(str(bitcoin['bpi']['USD']['rate']).replace(',',""))
        # multiply quantity to rate
        total_amount = n * rate
except:
    print('Value can not convert to float')
    # if the value can't be converted to float, the sys exit
    sys.exit()
    

else:
    #if everything is okey the program print the value
    print(f'{total_amount:,.4f}')





