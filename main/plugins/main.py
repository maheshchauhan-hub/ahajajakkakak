#tg:ChauhanMahesh/DroneBots
#github.com/vasusen-code

from .. import Drone
from telethon import events, Button
from main.plugins.drive import drive
from main.plugins.utils.utils import get_link
from LOCAL.localisation import link_animated

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def u(event):
    link = get_link(event.text)
    if link is False:
        return
    if 'drive.google.com' in link: 
        await event.client.send_message(event.chat_id, file=link_animated, reply_to=event.id, buttons=[[Button.inline("Upload.", data="drive")]])
        
@Drone.on(events.callbackquery.CallbackQuery(data="drive"))
async def d(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await drive(event, msg) 
    
