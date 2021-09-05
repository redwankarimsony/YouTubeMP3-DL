# YouTubeMP3-DL
A simple python application for downloading YouTube music into mp3 files. 




# Install Package Requirements
You need to install the following packages to make this code work properly. It uses `youtube_dl` package to download and decode the audio data from YouTube. The package `pydub` is used to convert or encode the `webm` file to `mp3` file for easier use. Package `ffmpeg` is the main encoding engine for conversion. 

## For MacOS
```(Python)
pip install youtube_dl
pip install pydub
brew install ffmpeg
```

## For Linux
```(Python)
pip install youtube_dl
pip install pydub
pip install ffmpeg
```

## Update the encoding engine path
Run the command `where ffmpe` in the terminal to find out the location of the encoding engine of ffmpeg. Then update the path in the `download_mp3.py` file where `AudioSegment.converter` variable is. You should be good to go. 


In order to download the mp3 files of the songs from YouTube, paste the links to each of the video link in the `url_links.txt` file. Once all the files are added in the file, run the `download_mp3.py` file with the following command.

```(Python)
python3 download_mp3.py
```

You should see the `mp3` files in the main directory. 


Thanks !!!





