import requests

nft_list = []


class Nft:

    def __init__(self, name, api):
        self.name = name
        self.api = api
        self.url = "https://api.opensea.io/api/v1/collection/{}/stats".format(api)
        nft_list.append(self)

    def nft_price_check(self):
        r = requests.get(url=self.url)
        data = r.json()
        self.price = data['stats']['floor_price']
        # print('The current floor price of {} is {} ETH.'.format(self.name, str(self.price)))

# Create NFT Class Object Here -- See Example Below
# This will create the NFT object and add it to the list that will message your Discord server
# You will get the API from the Opensea.io URL for the collection
# https://opensea.io/collection/cryptopunks
CryptoPunks = Nft(name='CryptoPunks', api='cryptopunks')
