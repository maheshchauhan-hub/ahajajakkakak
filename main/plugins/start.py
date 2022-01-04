from .. import Drone, ACCESS_CHANNEL, AUTH_USERS
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import DEV
from main.plugins.actions import set_thumbnail, rem_thumbnail, heroku_restart

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                              [Button.inline("Menu.", data="menu")]
                              ])
    
