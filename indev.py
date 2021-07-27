import discord
import os
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
from discord_slash.model import SlashCommandPermissionType
import random
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_ids = [635144592534011952]


@client.event
async def on_ready():  # todo: get rid of "Detected discord.Client!" error
    channel = client.get_channel(695014904381440092)
    await channel.send(random.choice(('im back baby', 'https://cdn.discordapp.com/attachments/606550060284510218/837688700564406323/im_back_baby.mp4')))
    await client.change_presence(activity=discord.Game(name="v3.135; /dzhelp"), status=discord.Status.dnd)
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.event  # smiley channel edit prevention code
async def on_message_edit(after, message):
    if message.channel.id == 660314906972651530 and not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
        await message.delete()


@client.event
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
        if message.content.lower().find(word_list[i]) != -1:
            trigger = word_list[i]
            break

    if message.author.bot:
        return

    if message.channel.id != 660314906972651530 and message.content.lower().find(trigger) != -1:

        if amongus_check == "sus" or amongus_check == "amogus" or amongus_check == "amongus" or amongus_check == "among us":
            await send(file=discord.File(random.choice(sus_list)))

        if trigger == "ancar":
            await send(file=discord.File('assets/users/ancar.jpg'))

        if trigger == "ancars":
            await send(file=discord.File('assets/users/ancar.jpg'))

        if trigger == "depressing":
            await send(file=discord.File('assets/users/quote.png'))

        if trigger == "phantom":
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

        if trigger == "tanner":
            await send(file=discord.File('assets/users/tanner.mov'))

        if trigger == "apple":
            await send(file=discord.File('assets/users/tanner.mov'))

        if trigger == "vtuber":
            await message.channel.send('https://cdn.discordapp.com/attachments/644226511381069824/817003185955668038/Vtubers.mp4')

        if trigger == "pimps at sea":
            await message.channel.send(random.choice(pimps_list))

        if trigger == "uwu" or trigger == "owo" or trigger == "x3":
            await message.add_reaction('🛑')

        if trigger == "null":
            await message.add_reaction('😳')

    if message.channel.id == 660314906972651530 and not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
        await message.delete()


@slash.slash(name="ping", guild_ids=guild_ids, description="Check ping to the bot.")
async def _ping(ctx):
    await ctx.send(f"Pong! ({client.latency * 1000}ms)")


@slash.slash(name="dzhelp", guild_ids=guild_ids, description="Shows the help embed.")
async def dzhelp(ctx):
    embedhelp = discord.Embed(title="Džastbot v3.135 help menu",
                              description="Welcome to džastbot help menu, here is a small command/feature list:")
    embedhelp.set_author(name="Džastbot",
                         url="https://cdn.discordapp.com/attachments/695014904381440092/836329019292516392/sus16.png",
                         icon_url="https://cdn.discordapp.com/avatars/695337101876789309/199d18d7311452261f0e3dcfe49fad32.png")
    embedhelp.add_field(name="/megadrop",
                        value="/megadrop - posts link with every nfs build i (JA) could find up to 2020 xmas ",
                        inline=False)
    embedhelp.add_field(name="/irr", value="/irr - Your post/This discussion meme", inline=False)
    embedhelp.add_field(name="/beytah", value="/beytah - for annoying fucks who cant read pins", inline=False)
    embedhelp.add_field(name="/data", value="/data - dont ask to ask", inline=False)
    embedhelp.add_field(name="/sanchez", value="/sanchez - inside joke only 10 people would get", inline=False)
    embedhelp.add_field(name="/bs", value="/bs - Bullshit", inline=False)
    embedhelp.add_field(name="/dzhelp", value="/dzhelp - Shows this message", inline=False)
    embedhelp.add_field(name="/changelog", value="/changelog - changelog", inline=False)
    embedhelp.add_field(name="/funny", value="funny - yes", inline=False)
    embedhelp.add_field(name="/ping", value="shows ping to the bot", inline=False)
    embedhelp.add_field(name="Misc:", value="/update and /loopback - things exclusive for JA (deprecated)",
                        inline=False)
    embedhelp.add_field(name="Other features:",
                        value="Responds with a picture/video to words `Ancar` `Creedoo` `Phantom` `Switchuwu` `Jojo` `Vtuber` `Sus` `Among us` `Amogus` `Amongus` `Pimps at sea` `Catgirl` `Toast` `A1ra/Aira/Sadra` `Tanner` and `Depressing`",
                        inline=False)
    embedhelp.set_footer(text="fuck discord fr")
    await ctx.send(embeds=[embedhelp])


@slash.slash(name="changelog", guild_ids=guild_ids, description="Shows the changelog embed.")
async def changelog(ctx):
    embed = discord.Embed(title="Džastbot changelog")
    embed.set_author(name="Džastbot",
                     icon_url="https://cdn.discordapp.com/avatars/695337101876789309/199d18d7311452261f0e3dcfe49fad32.png",
                     url="https://cdn.discordapp.com/attachments/695014904381440092/836329019292516392/sus16.png")
    embed.add_field(name="3.135 - hotfixes", value="3.134 - code optimizations thanks to TheMobas", inline=False)
    embed.add_field(name="3.133 - beytah update", value="3.132 - yet another rewrite", inline=False)
    embed.add_field(name="2.131 - sadra and tanner update",
                    value="2.128 - embed rework, zoomer repellent upd and no more crayon chewing", inline=False)
    embed.add_field(name="2.125-2.127 - zoomer repellent", value="2.124 - sus", inline=False)
    embed.add_field(name="2.123 - toast", value="2.122 - //funny upd", inline=False)
    embed.add_field(
        name="2.121 - trigger updates thanks to upside down fuck and grzegorz brzęczyszczykiewicz and everyone else",
        value="2.120 - internal token upd", inline=False)
    embed.add_field(name="2.119 - no more cat", value="2.118 - jojo and pimps at sea update", inline=False)
    embed.add_field(name="2.116 - im back baby", value="2.115 - smiley channel edits update", inline=False)
    embed.add_field(name="2.114 - moar sus pic", value="2.113 - pimp at sea update", inline=False)
    embed.add_field(name="2.111 - embeds update and bots blacklisted", value="2.109 - smiley channel", inline=False)
    embed.add_field(name="2.102 - added //megadrop", value="2.99-2.100 - more sus pics", inline=False)
    embed.add_field(name="2.98 - more triggers for sus pics", value="2.97 - pimps at sea update", inline=False)
    embed.add_field(name="2.96 - more sus pics", value="2.94 - added //beytah", inline=False)
    embed.add_field(name="2.92 - enabled smiley channel code",
                    value="2.85 - 2.91 - working on smiley channel revival, although disabled (code works though) plus one bugfix for sus response",
                    inline=False)
    embed.add_field(name="2.85 - changed //help to //dzhelp", value="2.84 - updated //help and //changelog textbox",
                    inline=False)
    embed.add_field(name="2.83 - added //changelog command", value="2.82 - added more sus pics", inline=False)
    embed.add_field(name="2.81 - updated //help textbox", value="CANT I JUST LEAVE THIS EMPTY", inline=False)
    embed.set_footer(text="fuck discord fr")
    await ctx.send(embeds=[embed])


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
    await ctx.send(
        "Mega folder with every nfs build I could find till 2020 xmas: <https://mega.nz/folder/u18FCRpQ#mQoqpPz_vAi5JgJeGhxoZA>")


@slash.slash(name="bs", guild_ids=guild_ids, description="bullshit")
async def bs(ctx):
    await ctx.send("https://youtu.be/2uREIGawrvI")


@slash.slash(name="funny", guild_ids=guild_ids, description="for very \"funny\" statements")
async def funny(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/702620924783886336/773354751370067968/video0.mp4")


@slash.slash(name="beytah", guild_ids=guild_ids, description="for lazy fucks")
async def beytah(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/792488969866182657/868453245415227422/gay7.gif")


client.run(TOKEN)
