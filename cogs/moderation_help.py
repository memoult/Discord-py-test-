import discord
from discord.ext import commands

class Moderation_Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Модуль {} загружен'.format(self.__class__.__name__))

@commands.command()
async def moderation_help(ctx):
    embed = discord.Embed(
        title='Moderation Help menu',
        description='Здесь вы можете увидеть команды для модерации'
    )
    commands_list = ['!очистить', '!кик', '!бан', '!разбанить', '!размут']
    descriptions_for_commands = ['Очистить чат', 'Кикнуть пользователя', 'Забанить пользователя', 'Разбанить пользователя', 'размутить пользователя']

    for command_name, description_command in zip(commands_list, descriptions_for_commands):
        embed.add_field(
            name = command_name,
            value = description_command,
            inline=False
        )

    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation_Help(bot))
