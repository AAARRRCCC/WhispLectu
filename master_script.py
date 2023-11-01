import os 
from download_audio import download_audio
from split_audio import split_audio
from transcribe_audio_part import transcribe_audio_part

def run_scripts():
    # Get video URL and download audio
    video_url = input("Enter the YouTube video URL: ")
    output_folder = "C:\\Users\\rbrad_jz8v5xi\\Desktop\\LectureStorage"
    
    # Receive both the audio path and the sanitized title
    downloaded_audio_path, sanitized_title = download_audio(video_url, output_folder)

    # Split the downloaded audio
    split_audio(downloaded_audio_path, output_folder)

    # After splitting, transcribe the first part
    first_part_path = os.path.join(output_folder, sanitized_title, "part000.mp3")
    transcribe_audio_part(first_part_path)
    
    print("Processing completed!")

if __name__ == "__main__":
    run_scripts()
