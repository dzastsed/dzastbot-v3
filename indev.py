import discord, os, os.path, sys, random, urllib.request, requests, DiscordUtils
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_permission, create_option, create_choice
from dotenv import load_dotenv
from requests import Session
from bs4 import BeautifulSoup
from PIL import Image


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
guild_ids = [635144592534011952, 606548517594595329, 340493057390804993]
guild_idsadm = [635144592534011952]
current_version = "v3.148"

@bot.event
async def on_ready():
    channel = bot.get_channel(695014904381440092)
    await channel.send(random.choice(('im back baby', 'https://cdn.discordapp.com/attachments/606550060284510218/837688700564406323/im_back_baby.mp4', 'https://cdn.discordapp.com/attachments/695014904381440092/885951151441322014/baby.mp4')))
    await bot.change_presence(activity=discord.Game(name=current_version + "; /dzhelp"), status=discord.Status.dnd)
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))


@bot.event  # Smiley Channel Edit Prevention
async def on_message_edit(after, message):
    if message.channel.id == 660314906972651530 and not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
        await message.delete()

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(635144592534011952)
    role = discord.utils.get(member.guild.roles, id=635152131208380436)
    await member.add_roles(role)

@bot.event
async def on_message(message):
    word_list = ["sus", "amogus", "amongus", "among us", "ancar", "ancars", "depressing", "phantom", "creedoo", "jojo",
                 "switchuwu", "sadra", "aira", "a1ra", "catgirl", "toast", "tanner", "apple", "vtuber", "pimps at sea",
                 "uwu", "owo", "x3"]
    sus_list = ['assets/sus/sus1.jpg', 'assets/sus/sus2.png', 'assets/sus/sus3.mp4', 'assets/sus/sus4.png',
                'assets/sus/sus5.jpg', 'assets/sus/sus6.png', 'assets/sus/sus7.png', 'assets/sus/sus8.jpg',
                'assets/sus/sus9.png', 'assets/sus/sus10.jpg', 'assets/sus/sus11.mp4', 'assets/sus/sus12.png',
                'assets/sus/sus13.mp4', 'assets/sus/sus14.mp4', 'assets/sus/sus15.mp4', 'assets/sus/sus16.png',
                'assets/sus/sus17.jpg', 'assets/sus/sus18.mov', 'assets/sus/sus19.png', 'assets/sus/sus20.png',
                'assets/sus/sus21.png', 'assets/sus/sus22.png', 'assets/sus/sus23.png']
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

    if message.channel.id == 660314906972651530:

        if not message.content:
            await message.delete()

        if not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
            await message.delete()


@slash.slash(name="ping", guild_ids=guild_ids, description="Check ping to the bot.")
async def _ping(ctx):
    await ctx.send(f"Pong! ({round(bot.latency * 1000)}ms)")


@slash.slash(name="dzhelp", guild_ids=guild_ids, description="Shows the help embed.")
async def dzhelp(ctx):
    help_embed = discord.Embed(title="Džastbot " + current_version + " help menu",
                               description="Welcome to džastbot help menu, here is a small command/feature list:")
    help_embed.set_author(name="Džastbot",
                          url="https://cdn.discordapp.com/attachments/695014904381440092/836329019292516392/sus16.png",
                          icon_url="https://cdn.discordapp.com/avatars/695337101876789309/199d18d7311452261f0e3dcfe49fad32.png")

    help_menu = open("assets/menus/help_menu.txt", "r")
    line_count = 0
    for line in help_menu:
        if line != "\n":
            line_count += 1
    help_menu.close()

    help_menu = open("assets/menus/help_menu.txt", "r")
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

    changelog_menu = open("assets/menus/changelog_menu.txt", "r")
    line_count = 0
    for line in changelog_menu:
        if line != "\n":
            line_count += 1
    changelog_menu.close()

    changelog_menu = open("assets/menus/changelog_menu.txt", "r")
    for i in range(int(line_count / 2)):
        changelog_name = changelog_menu.readline()
        changelog_value = changelog_menu.readline()
        changelog_embed.add_field(name=changelog_name, value=changelog_value, inline=False)
    changelog_menu.close()

    changelog_embed.set_footer(text="fuck discord fr")
    await ctx.send(embeds=[changelog_embed])


@slash.slash(name="reddit", guild_ids=guild_ids, description="Finds a post from Reddit")  # prideti "timed out" errora ar kazka pns ir galbut pabandyt kazka kad leistu keleta zodziu kaip keyworda parasyt
async def reddit(ctx, keyword):
    with Session() as s:
        link_check = False
        reddit_post_check = False
        post_number = 0
        headers = {'User-Agent': 'Mozilla/5.0'}
        site = s.get("https://www.reddit.com/search/?q=" + keyword, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        stuff = soup.find('div', class_='rpBJOHq2PR60pnwJlUyP0')

        if stuff is not None:
            upvotes = stuff.find_all('div', class_='_1rZYMD_4xY3gRcSS3p8ODO _25IkBM0rRUqWX5ZojEMAFQ')
            comments = stuff.find_all('span', class_='FHCV02u6Cp2zYL0fhQPsO')
            post_name = stuff.find_all('h3', class_='_eYtD2XCVieq6emjKBH3m')

            for a in soup.find_all('a', href=True):
                image_link = (a['href'])
                if image_link.startswith("https://i.redd.it/") or image_link.startswith("https://i.imgur.com/"):
                    link_check = True
                    for a in soup.find_all('a', href=True):
                        reddit_post = (a['href'])
                        if (a['href']) == image_link and not reddit_post_check:
                            reddit_post_check = True
                        if (reddit_post.startswith("https://www.reddit.com/r/")) and reddit_post_check:
                            break
                    embed = discord.Embed(title=post_name[post_number].get_text(), url=reddit_post, color=0xff4500)
                    embed.set_image(url=image_link)
                    embed.set_footer(text=" 👍 " + upvotes[post_number].get_text() + "  |   💬 " + comments[
                        post_number].get_text().replace('comments', '').replace('comment', ''))
                    await ctx.send(embed=embed)
                    break
                else:
                    if image_link.startswith("https://www.reddit.com/r/"):
                        post_number = post_number + 1
            if not link_check:
                await ctx.send("Sorry, but I couldn't find anything like that...")
        else:
            await ctx.send("Sorry, but I couldn't find anything like that...")


@slash.slash(name="upsidedown", guild_ids=guild_ids, description="Flips a picture upside down")
async def upsidedown(ctx, attachment=None):
    file_type = None
    if len(ctx.channel.last_message.attachments) != 0 and attachment is None:
        attachment = ctx.channel.last_message.attachments[0].url
    if attachment is not None:
        if attachment.endswith(".jpg") or attachment.endswith(".bmp"):
            file_type = ".jpg"
        elif attachment.endswith(".png") or attachment.endswith(".webp"):
            file_type = ".png"
        else:
            await ctx.send("Sorry, but I can't recognize your file...")
        if file_type is not None:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(attachment, "assets/temp_data/temp_1" + file_type)

            img = Image.open("assets/temp_data/temp_1" + file_type)
            img = img.rotate(180)
            img.save("assets/temp_data/temp_2" + file_type)
            await ctx.send(file=discord.File("assets/temp_data/temp_2" + file_type))
    else:
        await ctx.send("Sorry, but I can't find your picture...")


@slash.slash(name="data", guild_ids=guild_ids, description="Sends \"Don't ask to ask\" picture.")
async def data(ctx):
    await ctx.send(file=discord.File(r'assets/misc/data.png'))

@slash.slash(name="megadrop", guild_ids=guild_ids, description="Sends a link with all NFS build uploads.")
async def megadrop(ctx):
    await ctx.send("Masterlist of all builds up to 2024-04-02 (still WIP): https://dzastsed.github.io/nfs-builds.html")

@slash.slash(name="irr", guild_ids=guild_ids, description="Sends \"This discussion/Your post\" picture.")
async def irr(ctx):
    await ctx.send(file=discord.File(r'assets/misc/20201221_153250.jpg'))


@slash.slash(name="sanchez", guild_ids=guild_ids, description="didididididididididididididi")
async def data(ctx):
    await ctx.send(file=discord.File(r'assets/misc/sanchez.mp3'))


@slash.slash(name="thisserver", guild_ids=guild_ids, description="funniest shit ive seen in my life")
async def megadrop(ctx):
    await ctx.send(
        "Literally this server https://cdn.discordapp.com/attachments/719630423948263515/889571772117155861/rapbattl.mp4")



@slash.slash(name="bs", guild_ids=guild_ids, description="bullshit")
async def bs(ctx):
    await ctx.send("https://youtu.be/2uREIGawrvI")


@slash.slash(name="funny", guild_ids=guild_ids, description="for very \"funny\" statements")
async def funny(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/702620924783886336/773354751370067968/video0.mp4")


@slash.slash(name="beytah", guild_ids=guild_ids, description="for lazy fucks")
async def beytah(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/635144592534011958/1212321805952487464/gay7-ezgif.com-resize.gif")

@slash.slash(name="died", guild_ids=guild_ids, description="died soz")
async def died(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/340493057390804993/834084789552283698/unknown.png")

@slash.slash(name="nekopic", guild_ids=guild_ids, description="sends a random neko pic (multiple choices)",
             options=[
               create_option(
                 name="nekopic",
                 description="Nekopic",
                 option_type=3,
                 required=True,
                 choices=[create_choice(name="Neko Gif", value="ngif"), create_choice(name="Smug", value="smug"), create_choice(name="Pat", value="pat"), create_choice(name="Hug", value="hug"), create_choice(name="Fox girl", value="fox_girl"), create_choice(name="Waifu", value="waifu"), create_choice(name="Tickle", value="tickle"), create_choice(name="Neko", value="neko"), create_choice(name="Feeding", value="feed"), create_choice(name="Wallpaper", value="wallpaper"), create_choice(name="Avatar", value="avatar"), create_choice(name="Baka", value="baka"), create_choice(name="Kiss", value="kiss"), create_choice(name="Slap", value="slap"), create_choice(name="Genetically engineered catgirs (the fuck)", value="gecg")])])
async def data(ctx, nekopic):
        #if not channel.id == 753600461004603402:
         #   return
        response = requests.get('https://nekos.life/api/v2/img/{}'.format(nekopic))
        data = response.json()
        print(data)
        await ctx.send(data['url'])

@slash.slash(name="restart", guild_ids=guild_idsadm, description="restart the bot")
@slash.permission(guild_id=635144592534011952,
                    permissions=[
                        create_permission(257906842942832640, SlashCommandPermissionType.USER, True),
                        create_permission(261852392134279168, SlashCommandPermissionType.USER, True),
                        create_permission(879710023863902269, SlashCommandPermissionType.ROLE, False),
                        create_permission(635149040689872958, SlashCommandPermissionType.ROLE, False),
                        create_permission(659764021779628060, SlashCommandPermissionType.ROLE, False),
                        create_permission(771936469056356393, SlashCommandPermissionType.ROLE, False),
                        create_permission(647882162057641995, SlashCommandPermissionType.ROLE, False)
                        ])

async def restart(ctx):
  await ctx.send("Restarted")
  os.system("clear")
  os.execv(sys.executable, ['python'] + sys.argv)
  


bot.run(TOKEN)
