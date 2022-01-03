#TG:ChauhanMahesh/DroneBots
#Github.com/vasusen-code

import re
import os
import time
import gdown
import asyncio
from datetime import datetime as dt
from .. import Drone, BOT_UN
from telethon import events
from ethon.telefunc import fast_upload
from ethon.pyfunc import bash
from LOCAL.localisation import SUPPORT_LINK
from telethon.tl.types import MessageMediaWebPage
from main.plugins.utils.utils import get_link

#to upload files from drive folder 
#returns downloaded files path as a list
def drive_folder_download(url):
    output = gdown.download_folder(url, quiet=True)
    return output

#makes error handling handy
async def error(event, error, ps):
    await event.edit(f"An error [`{error}`] occured while {ps}.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)        
    
async def drive(event, msg):
    folder = []
    Drone = event.client
    edit = await Drone.send_message(event.chat_id, "Trying to process.", reply_to=msg.id)
    link = get_link(msg.text)
    if 'folder' in link:
        try:
            output = drive_folder_download(link)
        except Exception as e:
            print(e)
            return await error(edit, e, 'downloading') 
        folder.append(output)
    elif 'folders' in link:
        try:
            output = drive_folder_download(link)
        except Exception as e:
            print(e)
            return await error(edit, e, 'downloading') 
        folder.append(output) 
    elif 'https://drive.google.com/file/' in link:
        id = (link.split("/"))[5]
        _link = f'https://drive.google.com/uc?id={id}'
        try:
            file = gdown.download(_link, quiet=True)
        except Exception as e:
            print(e)
            return await error(edit, e, 'downloading') 
        folder.append(file)
    elif 'https://drive.google.com/uc?id=' in link:
        try:
            file = gdown.download(link, quiet=True)
        except Exception as e:
            print(e)
            return await error(edit, e, 'downloading') 
        folder.append(file)
    else:
        return await edit.edit(f'Link support not added.\n\ncontact [SUPPORT]({SUPPORT_LINK})', link_preview=False)
    await upload_folder(folder, event, edit) 
        
        
    
