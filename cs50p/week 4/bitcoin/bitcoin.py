import requests
import sys
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


def main():

    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(price_(n))
        except ValueError:
            sys.exit('Command-line argument is not a number')

    else:
        sys.exit('Missing command-line argument')



def price_(n):
    try:
        response = requests.get(url).json()
        price = response['bpi']['USD']['rate_float']
        final = price * n
        return f'${final:,.4f}'
    except:
        return None

main()