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
        nft_floor += str('{} | {} ETH \n'.format(nft_list[i].call_date, nft_list[i].floor))
        nft_price += str('{} ETH \n'.format(nft_list[i].price))

    embed_nft = discord.Embed(title="NFT Buys", url='', description="<#912536067071172618>", color=0x63b3f7)
    embed_nft.set_thumbnail(url='https://theme.zdassets.com/theme_assets/10680073/ea23e80a00a21a2499db8b5bb95cd31be1d9efa1.png')
    embed_nft.add_field(name='__NFT Collection__', value=nft_message, inline=True)
    embed_nft.add_field(name='__Call Date | Call Price__', value=nft_floor, inline=True)
    embed_nft.add_field(name='__Current Floor__', value=nft_price, inline=True)

    await message.channel.send(embed=embed_nft)
