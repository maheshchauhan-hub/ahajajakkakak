from ethon.pyfunc import bash

#For youtube videos download
async def youtube(url, event):    
    try:
        bash("pip install pyUltroid")
        from pyUltroid.functions.ytdl import download_yt
    except Exception:
        pass
    options = {
        "nocheckcertificate": True,
        "geo-bypass": True,
        "outtmpl": "%(id)s.mp4",
        "format": "best",
        "quiet": True }
    options["postprocessors"] = [{"key": "FFmpegMetadata"}]
    await download_yt(event, url, options) 
    
