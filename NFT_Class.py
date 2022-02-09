import requests

nft_list = []


class Nft:

    def __init__(self, name, floor, api, call_date):
        self.name = name
        self.floor = floor
        self.api = api
        self.url = "https://api.opensea.io/api/v1/collection/{}/stats".format(api)
        self.call_date = call_date
        nft_list.append(self)

    def nft_price_check(self):
        r = requests.get(url=self.url)
        data = r.json()
        self.price = data['stats']['floor_price']
        # print('The current floor price of {} is {} ETH.'.format(self.name, str(self.price)))
