from twitchio.ext import commands
#請先去終端 pip install twitchio


bot = commands.Bot(
    irc_token='', #填入你的oauth, 形式為"oauth:1a2b..." https://twitchapps.com/tmi/
    client_id='',  #填入註冊應用給的clien id  https://dev.twitch.tv/console/apps
    nick='', #隨意
    prefix='!!', #純掛網可以不用改
    initial_channels=['']
)


@bot.event
async def event_ready():
    login_list = []
    print(f'Ready | {bot.nick}')
    #language 英文填en, 中文填zh // game_id不知道可不填game_id=513143 // limit最多100 
    data = await bot.get_streams(language='zh',limit=100) 
    for i in data:
        id = i['user_id']
        names = await bot.get_users(id)
        login_list.append(names[0][1])
        print(login_list)
    await bot.join_channels(login_list)
    print("OK")

@bot.event
async def event_message(message):
    try:
        name = message.tags["display-name"]
        print(name,message.author,message.content,message.timestamp)
    except TypeError:
        print(message.author,message.content)
    await bot.handle_commands(message)


bot.run()
