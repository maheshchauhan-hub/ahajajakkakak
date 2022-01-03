#tg:ChauhanMahesh/DroneBots
#github.com/vasusen-code

from .. import Drone, ACCESS_CHANNEL, AUTH_USERS
from telethon import events, Button
from main.plugins.drive import drive
from telethon.tl.types import MessageMediaWebPage

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def u(event):
    if not hasattr(event.media, "webpage"):
        return
    if 'drive.google.com' in event.media.webpage.url: 
        await event.reply('.', buttons=[[Button.inline("Upload.", data="drive")]])
        
@Drone.on(events.callbackquery.CallbackQuery(data="drive"))
async def d(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await drive(event, msg) 
    
