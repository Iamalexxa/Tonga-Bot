import discord
from discord.ext import commands
import random
import requests

class Bot(commands.Bot):

  def __init__(self, intents: discord.Intents, **kwargs):
    super().__init__(command_prefix="!",
                     intents=intents,
                     case_insensitive=True)

  async def on_ready(self):
    print(f"Bot {self.user} is ready.")
    await self.tree.sync()
    await self.change_presence(activity=discord.Game(name="/g join Tonga"))


intents = discord.Intents.all()
bot = Bot(intents=intents)


@bot.hybrid_command(name='ping', description='I pong you back!')
async def ping(interaction: discord.Interaction):
  await interaction.send(content="Pong!")


@bot.hybrid_command(name="magic8ball",
                    description="Ask the magic 8 ball a question")
async def magic8ball(ctx):
  responses = [
      "Yes", "No", "Ask again later", "Cannot predict now",
      "Don't count on it", "Most likely", "Outlook not so good",
      "Reply hazy, try again"
  ]
  response = random.choice(responses)
  await ctx.send(content=f"Magic 8 Ball says: {response}")


@bot.hybrid_command(name='tonga', description='What is Tonga?')
async def tonga(ctx):
  """Information about Tonga."""
  await ctx.send(
      "Tonga, officially known as the Kingdom of Tonga, is a Polynesian island country situated in Oceania. "
      "Comprising a total of 171 islands, with 45 of them inhabited, Tonga covers approximately 750 km2 of land scattered "
      "across 700,000 km2 in the southern Pacific Ocean. Find out more here: https://bit.ly/Tonga"
  )


@bot.hybrid_command(name='hello', description='Say hello')
async def hello(ctx):
  """Simple hello command."""
  await ctx.send("Hello!")


@bot.hybrid_command(name='flipcoin', help='Decide heads or tails')
async def flip_coin(ctx):
  # Generate a random choice (0 for heads, 1 for tails)
  result = random.choice(['Heads', 'Tails'])

  # Send the result to the channel
  await ctx.send(f'{ctx.author.mention} flipped a coin and got **{result}**!')


@bot.hybrid_command(name='rockpaperscissors',
                    help='Play rock, paper, scissors with the bot')
async def play_rps(ctx, user_choice: str):
  choices = ['rock', 'paper', 'scissors']
  bot_choice = random.choice(choices)

  user_choice = user_choice.lower()

  if user_choice not in choices:
    await ctx.send("Invalid choice! Please choose rock, paper, or scissors.")
    return

  await ctx.send(f'{ctx.author.mention} chose **{user_choice}**!')
  await ctx.send(f'I chose **{bot_choice}**!')

  if user_choice == bot_choice:
    await ctx.send("It's a tie!")
  elif (user_choice == 'rock' and bot_choice == 'scissors') or \
       (user_choice == 'paper' and bot_choice == 'rock') or \
       (user_choice == 'scissors' and bot_choice == 'paper'):
    await ctx.send(f'{ctx.author.mention} wins!')
  else:
    await ctx.send('I win! Better luck next time.')

@bot.hybrid_command(
    name='rolldice',
    help='Roll a virtual dice with the specified number of sides')
async def roll_dice(ctx, sides: int = 6):
  if sides <= 1:
    await ctx.send(
        "Invalid number of sides. Please specify a number greater than 1.")
    return

  result = random.randint(1, sides)
  await ctx.send(
      f'{ctx.author.mention} rolled a {sides}-sided dice and got **{result}**!'
  )

@bot.hybrid_command(name='iqtest', help='Are you big brain or small brain?')
async def iq_test(ctx):
    # Generate a random IQ score between 80 and 200
    iq_score = random.randint(0, 1000)

    # Send the IQ score to the user
    await ctx.send(f'{ctx.author.mention}, your IQ score is **{iq_score}**! 🧠')

@bot.hybrid_command(name='gigachad', help='How gigachad are you??')
async def iq_test(ctx):
    # Generate a random IQ score between 80 and 200
    iq_score = random.randint(0, 1000)

    # Send the IQ score to the user
    await ctx.send(f'{ctx.author.mention}, your are **{iq_score}**% gigachad 💪')

@bot.hybrid_command(name='randommeme', help='Get a random meme!')
async def random_meme(ctx):
    # Make a request to the Meme API
    response = requests.get('https://meme-api.com/gimme')

    # Check if the request was successful
    if response.status_code == 200:
        meme_data = response.json()
        meme_url = meme_data['url']
        await ctx.send(f'Here\'s a random meme for you!\n{meme_url}')
    else:
        await ctx.send('Failed to fetch a random meme. Try again later.')


bot.run(
    'MTE4MDUxMDQyNzA5Mjg4NTUyNA.G6exmn.fjZIjpRszQPq7CN76H-EMOTuN5VRX83I8ex3Po')
