import json
from os import environ

from requests import post

# telegram variables
bottoken = environ['bottoken']
telegram_chat = "@XiaomiChannelPro"
# load the json file
with open('latest.json') as f:
    info = json.load(f)
# parse the json into telegram message
data = []
data.append('#{} #{}\n'.format(info[0]['rom_tag'], info[0]['codename']))
data.append('*{} {} {}* Update {}\n\n'.format(info[0]['rom'], info[0]['build_type'],
                                              info[0]['version'], info[0]['build_date']))
data.append('    📱Device: {} ({})\n'.format(info[0]['device'], info[0]['codename']))
data.append('    ▪[Download]({})\n'.format(info[0]['download_link']))
data.append('    ▪[XDA Thread]({})\n'.format(info[0]['thread_link']))
data.append('    ▪[Group]({})\n'.format(info[0]['group_link']))
data.append('\n')
if str(info[0]['changelog']) != '':
    with open('changelog.txt', 'r') as c:
        data.append('⚙️ *Changelog*:\n\n' + '```\n' + c.read() + '```\n')
if str(info[0]['developer_contact']) != '':
    data.append('By: [{}]({})\n'.format(info[0]['developer_name'], info[0]['developer_contact']))
else:
    data.append('By: {}\n'.format(info[0]['developer_name']))
data.append('Join 👉@XiaomiChannelPro')
# remove empty entries
for i in data:
    if ': \n' in i or '()' in i:
        data.remove(i)
# create the message
caption = ''.join(data)
photo = info[0]['image']
files = {
    'chat_id': (None, telegram_chat),
    'caption': (None, caption),
    'parse_mode': (None, "Markdown"),
    'photo': (photo, open(photo, 'rb')),
}
url = "https://api.telegram.org/bot" + bottoken + "/sendPhoto"
# post to telegram
telegram_req = post(url, files=files)
status = telegram_req.status_code
response = telegram_req.reason
if status == 200:
    print("Message sent")
else:
    print("Error: " + response)
