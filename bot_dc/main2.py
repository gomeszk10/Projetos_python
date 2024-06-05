import discord
import random
from dotenv import load_dotenv
import os
from discord.ext import commands
from discord import FFmpegPCMAudio

load_dotenv()
token = os.getenv('tokendiscord2')

permissoes = discord.Intents.default()
permissoes.voice_states = True
permissoes.message_content = True
permissoes.members = True
bot = commands.Bot(command_prefix="-", intents=permissoes)

@bot.command()
async def escreva(ctx:commands.Context, *,frase):
   await ctx.send(frase)

@bot.command()
async def cafe (ctx:commands.Context):
   await ctx.reply('Esse cara é uma lenda slk')

@bot.command()
async def ariel (ctx:commands.Context):
   await ctx.reply('Arielo pontchêrélo')

@bot.command()
async def ola(ctx:commands.Context):
   member = ctx.author
   await ctx.reply(f"Olá, {member.display_name}")

@bot.command()
async def ola2(ctx:commands.Context):
   member = ctx.author
   await ctx.reply(f"Olá, {member.name}")

@bot.command()
async def comandos(ctx:commands.Context):
   member = ctx.author
   await ctx.reply(f"Olá, {member.mention}, os comandos são: \n -furly 1-8 \n -cafe")

@bot.command()
async def vito(ctx:commands.Context):
   member = ctx.author
   await ctx.reply(f"O vito é esquema de aposta ")

@bot.command()
async def join2(ctx:commands.Context):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
        print(f'Bot entrou na chamada de voz em {channel}.')
    except Exception as e:
        print(f"Erro ao entrar na chamada de voz: {e}")

@bot.command()
async def sai2(ctx:commands.Context):
        voice_client = ctx.guild.voice_client
        await voice_client.disconnect()

@bot.command()
async def estourado(ctx: commands.Context):
    try: 
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()
      #  else:
         #   await voice_client.move_to(voice_channel)

        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\peste.mp3')
        voice_client.play(audio_source)
    except Exception as e:
        await ctx.send(f"Ocorreu um erro: {e}")

@bot.command()
async def estourado2(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\estourado2.mp3')
        voice_client.play(audio_source)

@bot.command()
async def estourado3(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\estourado3.mp3')
        voice_client.play(audio_source)

@bot.command()
async def furly1(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo tem muié no meu time.")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\furlyenorme.mp3')
        voice_client.play(audio_source)

@bot.command()
async def furly2(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo furly é...")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\furlytolete.mp3')
        voice_client.play(audio_source)

@bot.command()
async def furly3(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo clbc seu zé bct.")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\furlyrust.mp3')
        voice_client.play(audio_source)

@bot.command()
async def furly4(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo vem no cs fdp.")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\csfdp.m4a')
        voice_client.play(audio_source)

@bot.command()
async def furly5(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo não respeito baiano.")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\baiano.mp3')
        voice_client.play(audio_source)

@bot.command()
async def furly6(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo banga meu pau.")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\bangameupau.mp3')
        voice_client.play(audio_source)

@bot.command()
async def furly7(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo furly peru.")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\peru.mp3')
        voice_client.play(audio_source)

@bot.command()
async def furly8(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo furly sendo kikado.")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\kikado.mp3')
        voice_client.play(audio_source)

@bot.command()
async def furly9(ctx: commands.Context):
        
        voice_channel = ctx.author.voice.channel
        voice_client = ctx.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()

        member = ctx.author
        await ctx.reply(f"{member.mention}Reproduzindo macaco macaco.")
        audio_source = FFmpegPCMAudio('c:\\Users\\Guilherme\\Desktop\\projetos_python\\bot_dc\\macaco.mp4')
        voice_client.play(audio_source)

@bot.command()
async def pause(ctx: commands.Context):
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Áudio pausado.")

@bot.command()
async def resume(ctx: commands.Context):
    voice_client = ctx.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send("Áudio retomado.")

@bot.command()
async def skip(ctx: commands.Context):
    voice_client = ctx.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        await ctx.send("Áudio pulado.")


@bot.event
async def  on_member_join(membro:discord.Member):
    canal = membro.guild.get_channel(454952919133847554)
    await  canal.send(f"{membro.mention} Bem vindo!!!\n Mais um pra ver a careca do furry")

# isso é do mal
# @bot.event
# async def on_message(msg:discord.Message):
#     autor = msg.author
#     if autor.bot:
#         return
#     await msg.reply('Furly é careca')



@bot.event
async def on_ready():
    print("OK")

bot.run(token)