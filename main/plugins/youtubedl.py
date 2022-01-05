from yt_dlp import YoutubeDL
import yt_dlp

#logging-------------------------------------------------------------------------------------------

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
        
#----------------------------------------------------------------------------------------------------------

ydlp_opts={'logger': YTLogger(),
          'format': 'bestaudio/best',
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
