#MASS DM BY YACINE
import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send("MESSAGE?")#ADD HERE THAT YOU WANNA SEND TO YOUR FRIENDS
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}") #It maybe because of ratelimiting or they have dm disabled

client.run('YourBotToken', bot=False)#ADD YOUR TOKEN HERE NOT ANY BOT TOKEN