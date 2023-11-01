import os
from yt_dlp import YoutubeDL

def download_audio(video_url, output_folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_title = info_dict.get("title", None)
        sanitized_title = video_title.replace("|", "-").replace("/", "-").replace(":", " -")

        # Ensure the directory exists
        if not os.path.exists(f'{output_folder}/{sanitized_title}'):
            os.makedirs(f'{output_folder}/{sanitized_title}')

        # Update the outtmpl with the folder structure
        ydl_opts['outtmpl'] = f'{output_folder}/{sanitized_title}/{sanitized_title}.%(ext)s'

        with YoutubeDL(ydl_opts) as ydl_download:
            ydl_download.download([video_url])

        # Return both the path to the downloaded file and the sanitized title
        return f'{output_folder}/{sanitized_title}/{sanitized_title}.mp3', sanitized_title
