import os
import subprocess
import platform
import sys

# Check if the folder path was passed as a command line argument
if len(sys.argv) < 2:
    print("Error: missing folder path argument")
    sys.exit(1)

# Get the folder path from the command line arguments
folder = sys.argv[1]

# Iterate through all files in the folder
for filename in os.listdir(folder):
    # Check if the file is a video file
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov") or filename.endswith(".mkv") or filename.endswith(".yuv") or filename.endswith(".flv"):
        # Split the file name and extension
        file_name, file_ext = os.path.splitext(filename)

        # Compress the video file with HEVC codec
        # Use software-based H265/HEVC encoding
        subprocess.run(["ffmpeg", "-i", filename, "-c:v", "libx265", "-crf", "28", file_name + "_HEVC" + file_ext])

        # Get the size of the original and compressed files
        original_size = os.path.getsize(filename)
        compressed_size = os.path.getsize(file_name + "_HEVC" + file_ext)

        # Delete the smaller file
        if original_size > compressed_size:
            os.remove(filename)
        else:
            os.remove(file_name + "_HEVC" + file_ext)
