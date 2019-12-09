# twitchio-AFKBot
AFK for stickers/subscription etc.

The bot is based on python module <twitchio>  

Before running, you need to install the module by terminal  

On linux:  
**`python3 -m pip install git+https://github.com/TwitchIO/TwitchIO.git`**  
On windows:  
**`
py -version -m pip install git+https://github.com/TwitchIO/TwitchIO.git`**  

  
## Within bot.py file:  
* ***irctoken*** = "oauth:1a2b..." you can get it from [oauth](https://https://twitchapps.com/tmi/)  
* ***clientid*** = "blablabla" you can get it from [client_id](https://dev.twitch.tv/console/apps) (by registering a app)  
* ***nick*** is fine  
* ***prefix*** is used for bot's command, you can ignore it if just for AFK  
* ***initial_channels*** = ['what you like'] could be a list  

### get_streams(language='', game_id=number, limit=number)
* language: English='en', 中文='zh'
* game_id: could claim from many commands(might add soon...)
* limit: 1~100
