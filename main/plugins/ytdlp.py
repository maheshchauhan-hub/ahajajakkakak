#tg:MaheshChauhan/DroneBots
#Github.com/Vasusen-code

import yt_dlp
from yt_dlp import YoutubeDL

#for ytdlp supported sites -------------------------------------------------------------------------------------------

#logging
class YTLogger:
    def debug(self, msg):
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        
ydlp_opts={'logger': YTLogger(),
          'outtmpl': '%(title)s.%(ext)s',
          'no_warnings': True, 
          'quiet': True }

def ytdl(url):
    with yt_dlp.YoutubeDL(ydlp_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None) 
        video_ext = info_dict.get('ext', None) 
        return video_title + '.' + video_ext


    
    
        
    
    

