import requests
import json
import time
import csv

#get the price of bitcoin from bybit.
def get_price():
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    price = data['result'][0]['last_price']
    return price

#write the price of bitcoin to a csv file.
def write_price(price):
    with open('price66.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['price', 'time'])
        writer.writerow([price, time.ctime()])

#update the csv file with the new price and current time every 1 second.
def update_price():
    while True:
        price = get_price()
        with open('price66.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([price, time.ctime()])
        print(price)
        time.sleep(1)


if __name__ == "__main__":
    price = get_price()
    write_price(price)
    update_price()