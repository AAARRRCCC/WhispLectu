import subprocess
import os

def split_audio(input_file, output_folder, segment_time=900, output_pattern='part%03d.mp3'):
    """
    Splits the audio file into segments of a specified duration.

    Args:
        input_file (str): Path to the input audio file.
        output_folder (str): Path to the folder where split audio parts should be saved.
        segment_time (int, optional): Duration of each segment in seconds. Default is 900 seconds (15 minutes).
        output_pattern (str, optional): Pattern for naming the output files. Default is 'part%03d.mp3'.
    """

    # Extract the lecture's title from its filename
    lecture_title = os.path.basename(input_file).rsplit('.', 1)[0]  # removes the file extension

    # Create a subfolder with the lecture's title inside the output folder
    lecture_subfolder = os.path.join(output_folder, lecture_title)
    if not os.path.exists(lecture_subfolder):
        os.makedirs(lecture_subfolder)

    # Copy the original lecture into its subfolder
    new_lecture_path = os.path.join(lecture_subfolder, os.path.basename(input_file))
    os.replace(input_file, new_lecture_path)

    # Formulate the complete output pattern with the subfolder
    output_path = os.path.join(lecture_subfolder, output_pattern)

    # Command to split the audio file using ffmpeg
    cmd = [
        'ffmpeg',
        '-i', new_lecture_path,  # path to the lecture inside its subfolder
        '-f', 'segment',
        '-segment_time', str(segment_time),
        '-c', 'copy',
        output_path
    ]
    
    subprocess.run(cmd)

if __name__ == "__main__":
    input_path = input("Enter path to the input audio file: ").strip()
    output_folder = "C:\\Users\\rbrad_jz8v5xi\\Desktop\\LectureStorage"
    split_audio(input_path, output_folder)
