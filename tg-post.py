import json
from os import environ

from requests import post

# telegram variables
bottoken = environ['bottoken']
telegram_chat = "@PixysOSTEST"
# load the json file
with open('latest.json') as f:
    info = json.load(f)
# parse the json into telegram message
data = []
data.append('⚡️PixysOS Update⚡\n\n')
data.append('➡ *New build available for* *({})* *({})*\n'.format(info[0]['device'], info[0]['codename']))
data.append('👤 *By:* {}\n\n'.format(info[0]['developer_name']))

data.append('📆 *Build Date:* {}\n'.format(info[0]['build_date']))
data.append('ℹ *Build Version:* {}\n'.format(info[0]['version']))
data.append('ℹ *Build Type:* {}\n\n'.format(info[0]['build_type']))

data.append('⬇️ [Download Now: ]({})\n'.format(info[0]['download_link']))
data.append('⬇️ [XDA Thread Link: ]({})\n\n'.format(info[0]['thread_link']))

data.append('#{} #{}\n'.format(info[0]['rom_tag'], info[0]['codename']))
# remove empty entries
for i in data:
    if ': \n' in i or '()' in i:
        data.remove(i)
# create the message
caption = ''.join(data)


photo = 'https://telegra.ph/file/be46afe8c4ce5246e1cdc.jpg'
files = {
    'chat_id': (None, telegram_chat),
    'parse_mode': (None, "Markdown"),
    'text': ([​​​​​​​​​​​](https://telegra.ph/file/7195e32a5a8162927a675.jpg))",
}
url = "https://api.telegram.org/bot" + bottoken + "/sendMessage"
# post to telegram
telegram_req = post(url, files=files)
status = telegram_req.status_code
response = telegram_req.reason
if status == 200:
    print("Message sent")
else:
    print("Error: " + response)

