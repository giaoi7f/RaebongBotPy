import os
import html
import discord
from discord.ext import commands
import re
import random
from hanspell import spell_checker
from dotenv import load_dotenv
from discord.ui import view
from discord import utils
from emojiLink import emoji_dict, emoji_name, emoji_name_1
from name import name_list
from question import question

emoji_regex = re.compile(r'<:\w*:\d*>')

load_dotenv()
token = os.environ.get('token')

class Bot(commands.Bot):
    def __init__(self):
        self.command_prefix='!'
        self.fight_embed=False
        intents = discord.Intents.all()
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=intents)

    async def on_ready(self):
        await logging(f'{self.user}로 로그인함 (ID: {self.user.id})')
        await self.change_presence(activity=discord.Game(name="광질"))

        # self.music = []
        # async for message in self.get_channel(962604153891323934).history():
        #     if message.content.startswith('> '): #and message.author.id == self.application_id
        #         self.music.append(message.content)
        # print("MusicArr Added :\n" + "\n".join(self.music))

    async def on_message(self, msg):
        if msg.author.bot or msg.author.id == self.user.id:
            return

        if msg.content == 'e' or msg.content == 'E' or msg.content == 'ㄷ':
            await msg.delete()
            emote_view = EmoteButtons()
            emote_msg = await msg.channel.send(view=emote_view)
            await emote_view.wait()
            if emote_view.value:
                    await emote_msg.delete()
            return

        #enlarge emoticon with image_embed
        if msg.content.startswith('<:'):
            emoji = emoji_regex.findall(msg.content)[0]
            if emoji == msg.content:
                await msg.delete()
                await msg.channel.send(embed=image_embed(
                        msg.author, f"https://cdn.discordapp.com/emojis/{msg.content.split(':')[2][:-1]}.png"))
                return

        if msg.content in emoji_dict:
            await msg.delete()
            await msg.channel.send(embed=image_embed(msg.author, emoji_dict[msg.content]))
            return

        #Team
        if msg.content == '!내전':
            channel = msg.author.voice.channel
            if channel:
                if self.fight_embed:
                    await self.fight_embed.delete()
                member = channel.members
                player = []
                for user in member:
                    if user.id in name_list:
                        player.append(name_list[user.id])
                    else:
                        player.append(user.name)

                embed = discord.Embed(title=f"내전 ({len(player)}명)",description=", ".join(sorted(player)),color=0xff0000)
                random.shuffle(player)
                embed.add_field(name="Team1", value=" / ".join(sorted(player[:int(len(player) / 2)])), inline=False)
                embed.add_field(name="Team2", value=" / ".join(sorted(player[int(len(player) / 2):])), inline=True)
                self.fight_embed = await msg.reply(embed=embed)
            else:
                await msg.reply('보이스채널에 있어야합니다')

        #Spell check comm
        if msg.content.startswith("!검사 "):
            checked_spell = spell_check(utils.remove_markdown(msg.content[4:]))
            if checked_spell:
                await msg.reply(checked_spell)

        #Question
        if msg.content.startswith('!질문 '):
            if re.compile('\d ').match(msg.content[4:6]):
                await msg.reply(f"***> {msg.author.name}***{question(msg.content[6:], msg.content[4])}")
            elif re.compile('\d\d ').match(msg.content[4:7]):
                if int(msg.content[4:6]) > 69:
                    await msg.reply('!질문 (1~69) (~하는 것)')
                else:
                    await msg.reply(f"***> {msg.author.name}***{question(msg.content[7:], msg.content[4:6])}")
            else:
                await msg.reply('!질문 (1~69) (~하는 것)')

class EmoteButtons(discord.ui.View):
    def __init__(self, *, timeout=10):
        super().__init__(timeout=timeout)
        self.value = None
    
    def on_timeout(self):
        self.value = True
        self.stop()
    
    @discord.ui.button(label=emoji_name_1[0],style=discord.ButtonStyle.gray,row=0)
    async def button0(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[1],style=discord.ButtonStyle.gray,row=0)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[2],style=discord.ButtonStyle.gray,row=0)
    async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[3],style=discord.ButtonStyle.gray,row=1)
    async def button3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[4],style=discord.ButtonStyle.gray,row=1)
    async def button4(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[5],style=discord.ButtonStyle.gray,row=1)
    async def button5(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[6],style=discord.ButtonStyle.gray,row=2)
    async def button6(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[7],style=discord.ButtonStyle.gray,row=2)
    async def button7(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[8],style=discord.ButtonStyle.gray,row=2)
    async def button8(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[9],style=discord.ButtonStyle.gray,row=3)
    async def button9(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[10],style=discord.ButtonStyle.gray,row=3)
    async def button10(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=emoji_name_1[11],style=discord.ButtonStyle.gray,row=3)
    async def button11(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        await bot.get_channel(interaction.channel_id).send(embed=image_embed(interaction.user, emoji_dict[button.label]))
        self.stop()
    @discord.ui.button(label=1,style=discord.ButtonStyle.blurple,row=4,disabled=True)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        children = self.children
        for i in range(0, 12):
            children[i].label = emoji_name[0][i]
        for i in range(12, 16):
            children[i].disabled = False
        button.disabled = True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label=2,style=discord.ButtonStyle.blurple,row=4)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        children = self.children
        for i in range(0, 12):
            children[i].label = emoji_name[1][i]
        for i in range(12, 16):
            children[i].disabled = False
        button.disabled = True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label=3,style=discord.ButtonStyle.blurple,row=4)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        children = self.children
        for i in range(0, 12):
            children[i].label = emoji_name[2][i]
        for i in range(12, 16):
            children[i].disabled = False
        button.disabled = True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label=4,style=discord.ButtonStyle.blurple,row=4)
    async def menu4(self, interaction: discord.Interaction, button: discord.ui.Button):
        children = self.children
        for i in range(0, 12):
            children[i].label = emoji_name[3][i]
        for i in range(12, 16):
            children[i].disabled = False
        button.disabled = True
        await interaction.response.edit_message(view=self)

bot = Bot()

#make embed includes image
def image_embed(author, url):
    embed = discord.Embed(color=author.color)
    embed.set_author(name=author.display_name, icon_url=author.avatar.url)
    embed.set_image(url=url)
    return embed

#log detail terminal and specific text channel
async def logging(detail):
    print(f"Logging: {detail}")
    await bot.get_channel(962604153891323934).send(str(detail))

#string to spell-checked string with discord markdown
def spell_check(str):
    str = str.replace('\n', "<br>")
    print(str)
    result = spell_checker.check(str)
    if result.errors == 0:
        return False
        
    rt_str = []
    for sentence in str.split(): #sentence = 비오듯쏟아지던습하고
        check = spell_checker.check(sentence).words
        words = []
        for word, value in check.items(): #word = 비오듯, value = 1

            if word == "<span":
                continue
            if word[0:20] == "class='violet_text'>":
                words.append(f"~~{word[20:]}~~")
                continue

            #통과, 맞춤법, 띄어쓰기, 표준어, 통계적교정
            if value == 0 or value == 2:
                words.append(f"{word}")
            elif value == 1:
                words.append(f"**{word}**")
            else:
                words.append(f"[?]")
                
        words = " ".join(words)
        if len(check) != 1:
            rt_str.append(f"__{words}__")
        else:
            rt_str.append(f"{words}")
    
    print(rt_str)
    rt_str = " ".join(rt_str)
    rt_str = html.unescape(rt_str).replace("<br>", "\n")
    return re.sub(r'<.*>', "", rt_str)

bot.run(token)