#tg:ChauhanMahesh/DroneBots
#github.com/vasusen-code

import os
import time
from .. import Drone
from datetime import datetime
from telethon import events, Button
from main.plugins.drive import drive
from main.plugins.youtubedl import ytdl
from main.plugins.requests import weburl
from main.plugins.utils.utils import get_link, upload_file, force_sub
from main.plugins.m3u8 import download_m3u8_video
from LOCAL.localisation import link_animated, down_sticker, SUPPORT_LINK, forcesubtext

process1 = []
timer = []

async def upload_button(event, data):
    await event.client.send_message(event.chat_id, file=link_animated, reply_to=event.id, buttons=[[Button.inline("Upload.", data=data)]])

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def u(event):
    link = get_link(event.text)
    if link is False:
        return
    yy = await force_sub(event.sender_id)
    if yy is True:
        return await event.reply(forcesubtext)
    if 'drive.google.com' in link: 
        await upload_button(event, 'drive') 
    elif 'playlist' in link:
        return
    elif 'youtube' in link:
        return
    elif 'youtu.be' in link:
        return
    elif '.m3u8' in link:
        await upload_button(event, 'm3u8')
    else:
        await upload_button(event, 'upload') 
        
@Drone.on(events.callbackquery.CallbackQuery(data="drive"))
async def d(event):
    if f'{event.sender_id}' in process1:
        index = process1.index(f'{event.sender_id}')
        last = timer[int(index)]
        present = time.time()
        return await event.answer(f"You have to wait {120-round(present-float(last))} seconds more to start a new process!", alert=True)
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    await drive(event, msg) 
    now = time.time()
    timer.append(f'{now}')
    process1.append(f'{event.sender_id}')
    await event.client.send_message(event.chat_id, 'You can start a new process again after 2 minutes.')
    await asyncio.sleep(120)
    timer.pop(int(timer.index(f'{now}')))
    process1.pop(int(process1.index(f'{event.sender_id}')))
    
@Drone.on(events.callbackquery.CallbackQuery(data="upload"))
async def u(event):
    if f'{event.sender_id}' in process1:
        index = process1.index(f'{event.sender_id}')
        last = timer[int(index)]
        present = time.time()
        return await event.answer(f"You have to wait {120-round(present-float(last))} seconds more to start a new process!", alert=True)
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    ds = await Drone.send_message(event.chat_id, file=down_sticker, reply_to=msg.id)
    edit = await Drone.send_message(event.chat_id, '**DOWNLOADING**', reply_to=msg.id)
    file = None
    try:
        link = get_link(msg.text)
        try:
            x = weburl(link)
            if x is None:
                try:
                    file = ytdl(link)
                except Exception:
                    await ds.delete()
                    return await edit.edit('Link Not supported.')
            else:
                file = x
        except Exception:
            try:
                file = ytdl(link)
            except Exception:
                await ds.delete()
                return await edit.edit('Link Not supported.')
    except Exception as e:
        await ds.delete()
        return await edit.edit(f'An error `[{e}]` occured!\n\nContact [SUPPORT]({SUPPORT_LINK})', link_preview=False) 
    await ds.delete()
    await upload_file(file, event, edit) 
    now = time.time()
    timer.append(f'{now}')
    process1.append(f'{event.sender_id}')
    await event.client.send_message(event.chat_id, 'You can start a new process again after 2 minutes.')
    await asyncio.sleep(120)
    timer.pop(int(timer.index(f'{now}')))
    process1.pop(int(process1.index(f'{event.sender_id}')))
    
                
@Drone.on(events.callbackquery.CallbackQuery(data="m3u8"))
async def u8(event):
    if f'{event.sender_id}' in process1:
        index = process1.index(f'{event.sender_id}')
        last = timer[int(index)]
        present = time.time()
        return await event.answer(f"You have to wait {120-round(present-float(last))} seconds more to start a new process!", alert=True)
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    ds = await Drone.send_message(event.chat_id, file=down_sticker, reply_to=msg.id)
    edit = await Drone.send_message(event.chat_id, '**DOWNLOADING**', reply_to=msg.id)
    file = None
    try:
        link = get_link(msg.text)
        try:
            file = datetime.now().isoformat("_", "seconds") + ".mp4"
            download_m3u8_video(link, file) 
        except Exception as e:
            print(e)
            try:
                x = weburl(link)
                if x is None:
                    try:
                        file = ytdl(link)
                    except Exception:
                        await ds.delete()
                        return await edit.edit('Link Not supported.')
                else:
                    file = x
            except Exception:
                try:
                    file = ytdl(link)
                except Exception:
                    await ds.delete()
                    return await edit.edit('Link Not supported.')
    except Exception as e:
        await edit.edit(f'An error `[{e}]` occured!\n\nContact [SUPPORT]({SUPPORT_LINK})', link_preview=False) 
    await ds.delete()
    await upload_file(file, event, edit) 
    now = time.time()
    timer.append(f'{now}')
    process1.append(f'{event.sender_id}')
    await event.client.send_message(event.chat_id, 'You can start a new process again after 2 minutes.')
    await asyncio.sleep(120)
    timer.pop(int(timer.index(f'{now}')))
    process1.pop(int(process1.index(f'{event.sender_id}')))
    
                
            
                    
                    
        
