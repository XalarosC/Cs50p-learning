import sys
import requests

if len(sys.argv) == 2:
    try:
        bitcoin = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)


else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    price = response["bpi"]["USD"]["rate_float"]
    amount = price * bitcoin
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("RequestExeption")
    sys.exit(1)
