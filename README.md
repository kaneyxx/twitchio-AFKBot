# twitchio-AFKBot
AFK for stickers/subscription etc.

The bot is based on python module [twitchio](https://github.com/TwitchIO/TwitchIO)

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
* language: English='en', 中文='zh', にほんご='ja', français='fr'
* game_id: check posted below(you can also modify code to get)
* limit: 1~100



| English  | 中文 | game_id |
| -------- | -------- | -------- |
| IRL     |  IRL    | 509658     |
| Music and Performing Arts| 音樂與表演藝術|26936|
| Rainbow Six: Siege | 虹彩六號 | 460630 |
| League of Legends | 英雄聯盟 | 21779|
| Teamfight Tactics | 聯盟戰棋 | 513143 |
| Hearthstone | 爐石戰記 | 138585 |
| Age of Empire II:Def | 世紀帝國2決定版| 512988 |
| PUBG | 吃雞 | 493057
| World of Warcraft | 魔獸世界 | 18122 |
| Monster Hunter Wolrd|魔物獵人世界|497467|
| Dead by Daylight | 黎明死線 | 491487|
| Maple Story | 楓之谷 | 19976|
| Pokemon Sword/Shield| 寶可夢劍盾| 497451|
| Overwatch | 鬥陣特攻 | 488552|
