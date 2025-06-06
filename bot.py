import os
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv

from eureka import get_eureka_response

# Load environment variables from .env file
load_dotenv()

# Setup bot
intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    await bot.change_presence(
        activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="for 'euri'")
    )
    print(f"Euri is online as {bot.user}!")


@bot.event
async def on_message(message: nextcord.Message) -> None:
    if message.author == bot.user:
        return

    if "euri" in message.content.lower():
        async with message.channel.typing():
            response = get_eureka_response(
                query=message.content,
                api_key=os.getenv("EUREKA_API_KEY"),
                user=message.author.id
            )
            await message.channel.send(response.get("response", "Sorry, I couldn't process that."))

    await bot.process_commands(message)


@bot.command()
async def ping(ctx: commands.Context) -> None:
    await ctx.send("Pong!")

@bot.command(name="support")
async def support(ctx: commands.Context) -> None:
    embed = nextcord.Embed(
        title="🛠️ Need Help? Here's how to reach us!",
        description="Thanks for using **Euri**, powered by [Eureka-AI](https://eureka-ai.co.uk)!",
        color=nextcord.Color.orange()
    )

    embed.add_field(
        name="📚 Documentation",
        value="[View the Docs](https://eureka-technologies.gitbook.io/eureka-technologies/)",
        inline=False
    )
    embed.add_field(
        name="🌐 Website",
        value="[https://eureka-ai.co.uk](https://eureka-ai.co.uk)",
        inline=False
    )
    embed.add_field(
        name="✉️ Contact Email",
        value="hello@eureka-ai.co.uk",
        inline=False
    )

    embed.set_footer(text="Euri by Eureka Technologies • Open Source AI Tools")

    await ctx.send(embed=embed)


# Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))
