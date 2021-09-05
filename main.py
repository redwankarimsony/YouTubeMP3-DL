import os
import youtube_dl
from pydub import AudioSegment
AudioSegment.converter = '/opt/homebrew/bin/ffmpeg'

def get_video_info(video_url=None):
    try:
        print(video_url)
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
        return video_info
    except Exception as e:
        print(e)


def download_video(video_info):
    filename = f"{video_info['title']}.webm"
    options = {
        "format": "bestaudio/best",
        "keepvideo": False,
        "outtmpl": filename,
    }

    try:
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
            print(f"Download complete... {filename}")

            print(f"Converting webm to mp3....")
            convert_webm_mp3(filename)
            print(f"Deleting old {filename} ...")
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print(f"{filename} not found !!!")
    except Exception as e:
        print(f"Exception occurred inside video_download() \n{e}")


def load_links_file(file_path=None):
    try:
        with open(file_path, 'r') as f:
            urls = f.readlines()
            urls_filtered = [url.split("&")[0] for url in urls]
            return urls_filtered
    except Exception as e:
        print(e)
        return None


def convert_webm_mp3(filename):
    song = AudioSegment.from_file(filename, "webm")
    song.export(filename.replace("webm", "mp3"),
                format="mp3", bitrate='320k')


if __name__ == "__main__":
    for video_url in load_links_file(file_path="url_list.txt"):
        video_info = get_video_info(video_url)
        download_video(video_info)

