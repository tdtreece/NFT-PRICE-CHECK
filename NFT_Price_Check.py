import discord
from NFT_Class import nft_list
from discord.ext import commands

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def nft_buys(message):

    if message.author == bot:
        return

    await message.channel.send('Getting NFT prices...\n')

    nft_message = ''
    nft_floor = ''
    nft_price = ''

    for i in range(len(nft_list)):
        nft_list[i].nft_price_check()
        nft_message += str('{} \n'.format(nft_list[i].name))
        nft_floor += str('{} ETH \n'.format(nft_list[i].floor))
        nft_price += str('{} ETH \n'.format(nft_list[i].price))

    embed_nft = discord.Embed(title="OpenSea NFTs", url='https://opensea.io/', description="", color='')
    embed_nft.set_thumbnail(url='https://storage.googleapis.com/opensea-static/Logomark/Logomark-Blue.png')
    embed_nft.add_field(name='__NFT Collection__', value=nft_message, inline=True)
    embed_nft.add_field(name='__Current Floor__', value=nft_price, inline=True)

    await message.channel.send(embed=embed_nft)

bot.run('token')
