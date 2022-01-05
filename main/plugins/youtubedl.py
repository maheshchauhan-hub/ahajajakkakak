import os
from youtube_dl import YoutubeDL

#For youtube videos download
def youtube(url, event):    
    options = {
        "nocheckcertificate": True,
        "geo-bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "format": "best",
        "quiet": True }
    options["postprocessors"] = [{"key": "FFmpegMetadata"}]
    YoutubeDL(options).download([url])
    info = YoutubeDL({}).extract_info(url=url, download=False)
    title = info["title"]
    ext = "." + ytd["outtmpl"].split(".")[-1]
    file = title + ext
    return file
    
