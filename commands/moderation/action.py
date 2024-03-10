import disnake
from disnake.ext import commands
from disnake.enums import ButtonStyle
import sqlite3

from datetime import date, time, timedelta, datetime

db = sqlite3.connect("server.db") 
cur = db.cursor()

class Back(disnake.ui.View):

    def __init__(self, client, author, target):
        self.client = client
        self.author = author
        self.target = target
        super().__init__(timeout=None)

    @disnake.ui.button(label="Назад", style=ButtonStyle.red)
    async def Back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Взаимодействие с участником —\n{self.target}",
            description = f"{self.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}",
            color = 0x2b2d31
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target))

class Back_two(disnake.ui.View):
    def __init__(self, client, author, target):
        self.client = client
        self.author = author
        self.target = target
        super().__init__(timeout=None)

    @disnake.ui.button(label="Отмена", style=ButtonStyle.red)
    async def Back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Взаимодействие с участником —\n{self.target}",
            description = f"{self.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}", color = 0x2b2d31
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target))

class Mute(disnake.ui.View):
    def __init__(self, client, author, target):
        self.client = client
        self.author = author
        self.target = target
        super().__init__(timeout=None)
    
    async def interaction_check(self, interaction: disnake.MessageCommandInteraction):
        usr_roles = []
        for role in interaction.user.roles:
            usr_roles.append(role)
        def chek_roles(user: disnake.Member):
            valid_roles = [1184928071413928047, 1184928071397163097, 1184928071397163099] # роли которые могу использовать кнопки
            for urole in usr_roles:
                print(urole)
                if urole.id in valid_roles:
                    return True
                else:
                    pass
            return False
        
        if interaction.user == self.author and chek_roles(interaction.user) is True:
            return True
        else:
            return False

    @disnake.ui.button(label="5 мин", style=ButtonStyle.grey)
    async def one(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = "Замутить пользователя",
            description = "В чате напишите причину по которой хотите замутить пользователя",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.defer()
        await interaction.edit_original_message(embed = embed, view = None)

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        msg = await self.client.wait_for('message', check=check)
        reason = '{.content}'.format(msg)
        await msg.delete()
        dt = timedelta(seconds = 300)
        await self.target.timeout(duration = dt, reason = reason)
        await interaction.edit_original_message(embed = disnake.Embed(
            title = f"{self.target} замучен на 5 мин по причине {reason}", color = 0x2b2d31
        ), view = None)

    @disnake.ui.button(label="30 мин", style=ButtonStyle.grey)
    async def two(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = "Замутить пользователя",
            description = "В чате напишите причину по которой хотите замутить пользователя",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.defer()
        await interaction.edit_original_message(embed = embed, view = None)

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        msg = await self.client.wait_for('message', check=check)
        reason = '{.content}'.format(msg)
        await msg.delete()
        dt = timedelta(seconds = 1800)
        await self.target.timeout(duration = dt, reason = reason)
        await interaction.edit_original_message(embed = disnake.Embed(
            title = f"{self.target} замучен на 30 мин по причине {reason}", color = 0x2b2d31
        ), view = None)

    @disnake.ui.button(label="1 час", style=ButtonStyle.grey)
    async def three(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = "Замутить пользователя",
            description = "В чате напишите причину по которой хотите замутить пользователя",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.defer()
        await interaction.edit_original_message(embed = embed, view = None)

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        msg = await self.client.wait_for('message', check=check)
        reason = '{.content}'.format(msg)
        await msg.delete()
        dt = timedelta(seconds = 3600)
        await self.target.timeout(duration = dt, reason = reason)
        await interaction.edit_original_message(embed = disnake.Embed(
            title = f"{self.target} замучен на 1 час по причине {reason}", color = 0x2b2d31
        ), view = None)

    @disnake.ui.button(label="5 часов", style=ButtonStyle.grey)
    async def four(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = "Замутить пользователя",
            description = "В чате напишите причину по которой хотите замутить пользователя",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.defer()
        await interaction.edit_original_message(embed = embed, view = None)

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        msg = await self.client.wait_for('message', check=check)
        reason = '{.content}'.format(msg)
        await msg.delete()
        dt = timedelta(seconds = 18000)
        await self.target.timeout(duration = dt, reason = reason)
        await interaction.edit_original_message(embed = disnake.Embed(
            title = f"{self.target} замучен на 5 часов по причине {reason}", color = 0x2b2d31
        ), view = None)

    @disnake.ui.button(label="12 часов", style=ButtonStyle.grey)
    async def five(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = "Замутить пользователя",
            description = "В чате напишите причину по которой хотите замутить пользователя",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.defer()
        await interaction.edit_original_message(embed = embed, view = None)

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        msg = await self.client.wait_for('message', check=check)
        reason = '{.content}'.format(msg)
        await msg.delete()
        dt = timedelta(seconds = 43200)
        await self.target.timeout(duration = dt, reason = reason)
        await interaction.edit_original_message(embed = disnake.Embed(
            title = f"{self.target} замучен на 12 часов по причине {reason}", color = 0x2b2d31
        ), view = None)

    @disnake.ui.button(label = "Отмена", style=ButtonStyle.red, row = 1)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = f"Взаимодействие с участником —\n{self.target}",
            description = f"{self.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}",
            color = 0x2b2d31
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target))

class Warns(disnake.ui.Button):
    def __init__(self, label, author, target, con):
        super().__init__(label = label, style = disnake.ButtonStyle.primary)
        self.author = author
        self.target = target
        self.con = con

    async def callback(self, interaction):
        cur.execute("DELETE FROM warn WHERE _rowid_ = ?", [self.con])
        db.commit()
        await interaction.response.edit_message(embed = disnake.Embed(
            title = "Действие выполненно",
            description = f" у {self.target.mention} был снято предупреждение, админимтратором - {self.author.mention}",
            color = 0x2b2d31
        ),view = None)

class Back_one(disnake.ui.Button):
    def __init__(self, client, author, target):
        super().__init__(label = "Отмена", style = disnake.ButtonStyle.red)
        self.client = client
        self.author = author
        self.target = target

    async def callback(self, interaction):
        embed = disnake.Embed(
            title = f"Взаимодействие с участником —\n{self.target}",
            description = f"{self.author.mention}, Выберите опцию для взаимодействия с {self.target.mention}",
            color = 0x2b2d31
        )
        embed.set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        )
        embed.set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = ModerationButtons(self.client, self.author, self.target))

class ModerationButtons(disnake.ui.View):
    
    def __init__(self, client, author, target):
        self.client = client
        self.author = author
        self.target = target
        super().__init__(timeout=None)
    
    async def interaction_check(self, interaction):
        usr_roles = []
        for role in interaction.user.roles:
            usr_roles.append(role)
        def chek_roles(user: disnake.Member):
            valid_roles = [1184928071413928047, 1184928071397163097, 1184928071397163099] # роли которые могу использовать кнопки
            for urole in usr_roles:
                print(urole)
                if urole.id in valid_roles:
                    return True
                else:
                    pass
            return False
        
        if interaction.user == self.author and chek_roles(interaction.user) is True:
            return True
        else:
            return False

    @disnake.ui.button(emoji='<:emoji_95:1070727282760613969>',label = "История нарушений", style=ButtonStyle.gray,row = 1)
    async def Warn_History(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cur.execute("SELECT * FROM warn WHERE id = ?", [self.target.id]).fetchone() == None:
            await interaction.response.send_message(embed = disnake.Embed(
                title = "у учасника отсутвуют предупреждения", color = 0x2b2d31
            ), ephemeral = True)
        else:
            emb = disnake.Embed(
                title = "Список предупреждений"
            )
            a = 0
            for x in cur.execute("SELECT * FROM warn WHERE id = ?", [self.target.id]):
                a += 1
                emb.add_field(name = f"{a}) {x[2]}", value = f"date: {x[3]}\nadm: <@{x[1]}>")
            await interaction.response.edit_message(embed = emb, view = Back(self.client, self.author, self.target))

    @disnake.ui.button(emoji='<:emoji_96:1070727334690304000>',label = "Забанить", style=ButtonStyle.gray)
    async def Ban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = "Забанить пользователя",
            description = "В чате напишите причину по которой хотите забанить пользователя",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.edit_message(embed = embed, view = Back_two(self.client, self.author, self.target))
        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel
            
        msg = await self.client.wait_for('message', check=check)
        messg = '{.content}'.format(msg)
        await msg.delete()

        embed = disnake.Embed(
            title = "Забанить пользователя",
            description = f"Вы забанили пользователя по причине `{messg}`",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        for nrole in self.target.roles:
            try:
                await self.target.remove_roles(nrole)
            except:
                print(nrole)
        role = interaction.guild.get_role(1194615690611654736) # Роль бана
        await self.target.add_roles(role)
        await interaction.edit_original_message(embed = embed, view = None)

    @disnake.ui.button(emoji='<:emoji_97:1070727377115688960>',label = "Разбанить", style=ButtonStyle.gray)
    async def Unban(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = "Разбанить пользователя",
            description = "Вы разабанили пользователя",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        banrole = interaction.guild.get_role(1194615690611654736) # Роль бана
        await self.target.remove_roles(banrole)
        role = interaction.guild.get_role(1184928071397163092) # Роль обычного пользователя
        await self.target.add_roles(role)
        await interaction.response.edit_message(embed = embed, view = Back(self.client, self.author, self.target))

    @disnake.ui.button(emoji='<:emoji_98:1070727412226207804>',label="Замутить", style=ButtonStyle.grey, row = 2)
    async def Mute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.target.current_timeout == None:
            embed = disnake.Embed(
                title = "Замутить пользователя",
                description = "Время",
                color = 0x2b2d31
            ).set_author(
                name = self.target,
                url = f"https://discordapp.com/users/{self.target.id}/",
                icon_url = self.target.avatar
            ).set_thumbnail(
                url = self.target.avatar
            )
            await interaction.response.edit_message(embed = embed, view = Mute(self.client, self.author, self.target))
        else:
            await interaction.response.send_message(embed = disnake.Embed(
                title = f"{self.target} уже в муте", color = 0x2b2d31
            ), ephemeral = True)

    @disnake.ui.button(emoji='<:emoji_99:1070727462331371590>',label="Размутить", style=ButtonStyle.grey, row = 2)
    async def Unmute(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if self.target.current_timeout == None:
            await interaction.response.send_message(embed = disnake.Embed(
                title = f"{self.target} не замучен", color = 0x2b2d31
            ), ephemeral = True)
        else:
            await self.target.timeout(duration = None)
            await interaction.response.edit_message(embed = disnake.Embed(
                title = f"{self.target} размучен", color = 0x2b2d31
            ))

    @disnake.ui.button(emoji='<:emoji_100:1070727521479434280>',label="Выдать предупреждение", style=ButtonStyle.grey, row = 3)
    async def Warn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(
            title = "Выдать предупреждение пользователя",
            description = "В чате напишите причину по которой хотите выдать предупреждение пользователю",
            color = 0x2b2d31
        ).set_author(
            name = self.target,
            url = f"https://discordapp.com/users/{self.target.id}/",
            icon_url = self.target.avatar
        ).set_thumbnail(
            url = self.target.avatar
        )
        await interaction.response.defer()
        await interaction.edit_original_message(embed = embed, view = Back_two(self.client, self.author, self.target))

        def check(m):
            return m.author == interaction.author and m.channel == interaction.channel

        msg = await self.client.wait_for('message', check=check)
        reason = '{.content}'.format(msg)
        await msg.delete()
        cur.execute("INSERT INTO warn VALUES(?,?,?,?)",[self.target.id, self.author.id, reason, datetime.today().replace(microsecond=0)])
        db.commit()
        await interaction.edit_original_message(embed = disnake.Embed(
            title = f"{self.target} получил предупреждение по причине {reason}", color = 0x2b2d31,
        ), view = None)

    @disnake.ui.button(emoji='<:emoji_97:1070727377115688960>',label="Снять предупреждение", style=ButtonStyle.grey, row = 3)
    async def Unwarn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if cur.execute("SELECT * FROM warn WHERE id = ?", [self.target.id]).fetchone() == None:
            return await interaction.response.send_message(embed = disnake.Embed(
                title = "у учасника отсутвуют предупреждения", color = 0x2b2d31,
            ), ephemeral = True)
        view = disnake.ui.View()
        for x in cur.execute("SELECT id, adm, reason, _rowid_ FROM warn WHERE id = ?", [self.target.id]):
            view.add_item(Warns(label = x[2], author = self.author, target = self.target, con = x[3]))
        view.add_item(Back_one(self.client, self.author, self.target))
        await interaction.response.edit_message(embed = disnake.Embed(
            title = "выберите предупреждение", color = 0x2b2d31,
        ), view = view)

    @disnake.ui.button(emoji='<:emoji_88:1070713301035663411>',label="Выйти", style=ButtonStyle.red, row = 4)
    async def back(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        await interaction.edit_original_message(embed = disnake.Embed(
            title = "Удаление сообщение...", color = 0x2b2d31,
        ), view = None)
        await interaction.delete_original_message()

class Action(commands.Cog):

    def __init__(self, client):
        self.client = client
        print('Commands {} is loaded'.format(self.__class__.__name__))

    @commands.slash_command(name='action', description='взаимодействие с участником')
    async def action(self, inter, target: disnake.Member = commands.Param(name = "пользователь")):
        if target == None:
            target = await self.bot.fetch_user(target)
            print(target)
        if target == inter.author:
            embed = disnake.Embed(
                title = "Взаимодействие с участником",
                description = "Вы не можете взаимодействовать с самим собой",
                color = 0x2b2d31
            ).set_author(
                name = target,
                url = f"https://discordapp.com/users/{target.id}/",
                icon_url = target.avatar
            ).set_thumbnail(
                url = target.avatar
            )
            await inter.send(embed = embed, ephemeral = True)
            return True
        if inter.author.top_role <= target.top_role:
            embed = disnake.Embed(
                title = "Взаимодействие с участником",
                description = "Вы не можете взаимодействовать с участиником так как ваша роль ниже или равна роли участника",
                color = 0x2b2d31
            ).set_author(
                name = target,
                url = f"https://discordapp.com/users/{target.id}/",
                icon_url = target.avatar
            ).set_thumbnail(
                url = target.avatar
            )
            await inter.send(embed = embed, ephemeral = True)
        else:
            embed = disnake.Embed(
                title = f"Взаимодействие с участником —\n{target}",
                description = f"{inter.author.mention}, Выберите опцию для взаимодействия с {target.mention}",
                color = 0x2b2d31
            )
            embed.set_author(
                name = target,
                url = f"https://discordapp.com/users/{target.id}/",
                icon_url = target.avatar
            )
            embed.set_thumbnail(
                url = target.avatar
            )
            await inter.send(embed = embed, view = ModerationButtons(self.client, inter.author, target))
            
    @action.error
    async def on_command_error(self, inter, error):
        if isinstance(error, commands.MissingRole):
            embed = disnake.Embed(
                title="Недостаточно прав!",
                description=f"{inter.author.mention} у вас нет прав на это действие!",
                color = 0x2b2d31
            )
            embed.set_thumbnail(url=inter.author.display_avatar.url)
            await inter.send(embed=embed, ephemeral=True)


def setup(client):
    client.add_cog(Action(client))