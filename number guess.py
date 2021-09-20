import discord
from discord.ext import commands
import random
import math

client = commands.Bot(command_prefix='!')

global count
count = 0

@client.command()
async def game(ctx, p : discord.Member):
	global x
	x = random.randint(1, 200)
	global player
	player = p
	print("\tYou've only ", round(math.log(200 - 1 + 1, 2)), " chances to guess the integer between 1 to 200!\n")
	embed = discord.Embed(title=f"You've only  {round(math.log(200, 2))} chances to guess the integer between 1 to 200!", colour=discord.Colour.random())
	await ctx.reply(embed=embed)

@client.command()
async def p(ctx, guess : int):
	global count
	global turn
	global player
	# while count < math.log(200, 2):

	turn = ctx.author

	if turn == player:
		if x == guess:
			print("Congratulations you did it in ", count, " try")
			embed = discord.Embed(title=f"Congratulations you did it in {count} try", colour=discord.Colour.random())
			await ctx.reply(embed=embed)
			# Once guessed, loop will break

		elif x > guess:
			print("You guessed too small!")
			await ctx.reply("You guessed too small!")

		elif x < guess:
			print("You Guessed too high!")
			await ctx.reply("You Guessed too high!")

		if count >= math.log(200, 2):
			print("\nThe number is %d" % x)
			print("\tBetter Luck Next time!")
			embed = discord.Embed(title=f"The number is {x}, Better Luck Next time!. PLease start a new game.", colour=discord.Colour.random())
			await ctx.reply(embed = embed)

		count += 1

	else:
		await ctx.reply("It's not your turn so just sit keep quite, don't jump in between.")


client.run('Your_Token')





