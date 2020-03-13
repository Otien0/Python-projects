#Download the FFmpeg-python file;

#on the terminal, run this commands:
#FFmpeg -i "name of your video file" -vn output_audio.mp3
        
        #Extracting mp4 vid to ogg
FILE="1.mp4";
ffmpeg -i "${1.mp4}" -vn -acodec libvorbis -y "${1.mp4%.mp4}.ogg"

#In case we want to automatically process (batch process) all .MP4 video files in a folder we can use the following:

for FILE in *.mp4;
do
    echo -e "Processing video '\e[32m$FILE\e[0m'";
    ffmpeg -i "${FILE}" -vn -acodec libvorbis -y "${FILE%.mp4}.ogg";
done
