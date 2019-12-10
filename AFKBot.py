from twitchio.ext import commands

bot = commands.Bot(
    irc_token='oauth:', #填入你的oauth, 形式為"oauth:1a2b..." https://twitchapps.com/tmi/
    client_id='',  #填入註冊應用給的clien id  https://dev.twitch.tv/console/apps
    nick='kaneyxx', #隨意
    prefix='!!', #純掛網可以不用改
)


@bot.event
async def event_ready():
    login_list = []
    print(f'Ready | {bot.nick}')
    language_choice = input("language(N for pass): ")
    if language_choice == "N":
        language_choice = None
    game_choice = input("game_id(N for pass): ")
    if game_choice == "N":
        game_choice = None
    limit_choice = input("limit(1~100): ")
    data = await bot.get_streams(language=None,game_id=game_choice,limit=int(limit_choice))
    for i in data:
        id = i['user_id']
        names = await bot.get_users(id)
        login_list.append(names[0][1])
        # print(login_list)
    await bot.join_channels(login_list)
    print(len(login_list))
    print("OK")

# for displaying chat room
# @bot.event
# async def event_message(message):
#     try:
#         name = message.tags["display-name"]
#         print(name,message.author,message.content,message.timestamp)
#     except TypeError:
#         print(message.author,message.content)
#     await bot.handle_commands(message)


bot.run()
