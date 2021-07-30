import discord
from discord.ext import commands
import os
from discord_slash import SlashCommand
import random
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_ids = [635144592534011952]


@bot.event
async def on_ready():
    channel = bot.get_channel(695014904381440092)
    await channel.send(random.choice(('im back baby',
                                      'https://cdn.discordapp.com/attachments/606550060284510218/837688700564406323/im_back_baby.mp4')))
    await bot.change_presence(activity=discord.Game(name="v3.138; /dzhelp"), status=discord.Status.dnd)
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))


@bot.event  # Smiley Channel Edit Prevention
async def on_message_edit(after, message):
    if message.channel.id == 660314906972651530 and not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
        await message.delete()


@bot.event
async def on_message(message):
    word_list = ["sus", "amogus", "amongus", "among us", "ancar", "ancars", "depressing", "phantom", "creedoo", "jojo",
                 "switchuwu", "sadra", "aira", "a1ra", "catgirl", "toast", "tanner", "apple", "vtuber", "pimps at sea",
                 "uwu", "owo", "x3"]
    sus_list = ['assets/sus/sus1.jpg', 'assets/sus/sus2.png', 'assets/sus/sus3.mp4', 'assets/sus/sus4.png',
                'assets/sus/sus5.jpg', 'assets/sus/sus6.png', 'assets/sus/sus7.png', 'assets/sus/sus8.jpg',
                'assets/sus/sus9.png', 'assets/sus/sus10.jpg', 'assets/sus/sus11.mp4', 'assets/sus/sus12.png',
                'assets/sus/sus13.mp4', 'assets/sus/sus14.mp4', 'assets/sus/sus15.mp4', 'assets/sus/sus16.png',
                'assets/sus/sus17.jpg', 'assets/sus/sus18.mov', 'assets/sus/sus19.png']
    jojo_list = ['assets/misc/jojo.mp4', 'assets/misc/jojo2.mp4']
    pimps_list = ['https://media.discordapp.net/attachments/644226511381069824/828733114464993300/pingdariogreggio.gif',
                  'https://cdn.discordapp.com/attachments/487367223808098304/836337916023406662/PimpsAtSeaDarioGreggio.mp4',
                  'https://cdn.discordapp.com/attachments/839090722464071720/842457988085317632/pimps_ds.png',
                  'https://cdn.discordapp.com/attachments/487367223808098304/842238106819231744/PimpsAtSeaMadMen.mp4',
                  'https://media.discordapp.net/attachments/839090722464071720/842190590841585694/pas-amog-us.png',
                  'https://media.discordapp.net/attachments/839090722464071720/842085327219982336/lego-pimps.png',
                  'https://cdn.discordapp.com/attachments/839090722464071720/840010604445564958/passponge.mp4']
    send = message.channel.send
    amongus_check = message.content.lower()
    trigger = "null"

    for i in range(len(word_list)):
        if not message.content.lower().find(word_list[i]):
            trigger = word_list[i]
            break
    if message.author.bot:
        return

    if message.channel.id != 660314906972651530 and not message.content.lower().find(trigger):

        if amongus_check == "sus" or amongus_check == "amogus" or amongus_check == "amongus" or amongus_check == "among us":
            await send(file=discord.File(random.choice(sus_list)))

        if trigger == "ancar" or trigger == "ancars":
            await send(file=discord.File('assets/users/ancar.jpg'))

        if trigger == "depressing" or trigger == "phantom":
            await send(file=discord.File('assets/users/quote.png'))

        if trigger == "creedoo":
            await send(file=discord.File('assets/users/creedoo.png'))

        if trigger == "jojo":
            await send(file=discord.File(random.choice(jojo_list)))

        if trigger == "switchuwu":
            await send(file=discord.File('assets/users/switch.png'))

        if trigger == "sadra" or trigger == "aira" or trigger == "a1ra":
            await send(file=discord.File('assets/users/sadra.jpg'))

        if trigger == "catgirl":
            await send(file=discord.File('assets/users/cat2.png'))

        if trigger == "toast":
            await send(file=discord.File('assets/users/toast.png'))

        if trigger == "tanner" or trigger == "apple":
            await send(file=discord.File('assets/users/tanner.mov'))

        if trigger == "vtuber":
            await message.channel.send(
                'https://cdn.discordapp.com/attachments/644226511381069824/817003185955668038/Vtubers.mp4')

        if trigger == "pimps at sea":
            await message.channel.send(random.choice(pimps_list))

        if trigger == "uwu" or trigger == "owo" or trigger == "x3":
            await message.add_reaction('🛑')

        if trigger == "null":
            await message.add_reaction('😳')

    if message.channel.id == 660314906972651530:  # Smiley Channel Code

        if not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
            await message.delete()

        if not message.stickers:
            await message.delete()
            await message.channel.send("😃")


@slash.slash(name="ping", guild_ids=guild_ids, description="Check ping to the bot.")
async def _ping(ctx):
    await ctx.send(f"Pong! ({round(bot.latency * 1000)}ms)")


@slash.slash(name="dzhelp", guild_ids=guild_ids, description="Shows the help embed.")
async def dzhelp(ctx):
    help_embed = discord.Embed(title="Džastbot v3.138 help menu",
                               description="Welcome to džastbot help menu, here is a small command/feature list:")
    help_embed.set_author(name="Džastbot",
                          url="https://cdn.discordapp.com/attachments/695014904381440092/836329019292516392/sus16.png",
                          icon_url="https://cdn.discordapp.com/avatars/695337101876789309/199d18d7311452261f0e3dcfe49fad32.png")

    help_menu = open("help_menu.txt", "r")
    line_count = 0
    for line in help_menu:
        if line != "\n":
            line_count += 1
    help_menu.close()

    help_menu = open("help_menu.txt", "r")
    for i in range(int(line_count / 2)):
        help_name = help_menu.readline()
        help_value = help_menu.readline()
        help_embed.add_field(name=help_name, value=help_value, inline=False)
    help_menu.close()

    help_embed.set_footer(text="fuck discord fr")
    await ctx.send(embeds=[help_embed])


@slash.slash(name="changelog", guild_ids=guild_ids, description="Shows the changelog embed.")
async def changelog(ctx):
    changelog_embed = discord.Embed(title="Džastbot changelog")
    changelog_embed.set_author(name="Džastbot",
                               icon_url="https://cdn.discordapp.com/avatars/695337101876789309/199d18d7311452261f0e3dcfe49fad32.png",
                               url="https://cdn.discordapp.com/attachments/695014904381440092/836329019292516392/sus16.png")

    changelog_menu = open("changelog_menu.txt", "r")
    line_count = 0
    for line in changelog_menu:
        if line != "\n":
            line_count += 1
    changelog_menu.close()

    changelog_menu = open("changelog_menu.txt", "r")
    for i in range(int(line_count / 2)):
        changelog_name = changelog_menu.readline()
        changelog_value = changelog_menu.readline()
        changelog_embed.add_field(name=changelog_name, value=changelog_value, inline=False)
    changelog_menu.close()

    changelog_embed.set_footer(text="fuck discord fr")
    await ctx.send(embeds=[changelog_embed])


@slash.slash(name="data", guild_ids=guild_ids, description="Sends \"Don't ask to ask\" picture.")
async def data(ctx):
    await ctx.send(file=discord.File(r'assets/misc/data.png'))


@slash.slash(name="irr", guild_ids=guild_ids, description="Sends \"This discussion/Your post\" picture.")
async def irr(ctx):
    await ctx.send(file=discord.File(r'assets/misc/20201221_153250.jpg'))


@slash.slash(name="sanchez", guild_ids=guild_ids, description="didididididididididididididi")
async def data(ctx):
    await ctx.send(file=discord.File(r'assets/misc/sanchez.mp3'))


@slash.slash(name="megadrop", guild_ids=guild_ids, description="Sends MEGA link with all NFS builds.")
async def megadrop(ctx):
    await ctx.send("Mega folder with every nfs build I could find till 2020 xmas: <https://mega.nz/folder/u18FCRpQ#mQoqpPz_vAi5JgJeGhxoZA>")


@slash.slash(name="bs", guild_ids=guild_ids, description="bullshit")
async def bs(ctx):
    await ctx.send("https://youtu.be/2uREIGawrvI")


@slash.slash(name="funny", guild_ids=guild_ids, description="for very \"funny\" statements")
async def funny(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/702620924783886336/773354751370067968/video0.mp4")


@slash.slash(name="beytah", guild_ids=guild_ids, description="for lazy fucks")
async def beytah(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/792488969866182657/868453245415227422/gay7.gif")


bot.run(TOKEN)
