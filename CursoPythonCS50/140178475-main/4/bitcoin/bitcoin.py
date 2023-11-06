import requests
import sys
import json

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
try:
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)
else:
    try:
        info = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit(1)
    else:
        info = info.json()
        object = info["bpi"]["USD"]["rate"]
        amount = float(object.replace(",", "")) * n
        print(f"${amount:,.4f}")