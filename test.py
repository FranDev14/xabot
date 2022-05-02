import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    server_id = 970749075014168628 #this is my own server id
    guild = client.get_guild(server_id)
    print(guild)

client.run("OTcwMzQ1OTg1ODQ5MDUzMTg0.Ym6nHw.6a1cG83DsE6aDI1j_jAEBqkQuWw")