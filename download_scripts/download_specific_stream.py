from pytube import YouTube


def download_specific_stream(video_url, itag, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_by_itag(itag)
        stream.download(output_path)
        
        print(f'Video "{yt.title}" has been downloaded successfully and saved to "{output_path}"')
    
    except Exception as e:
        print(f'An error occurred: {e}')

# URL of the YouTube video
video_url = 'https://www.youtube.com/watch?v=DF3XjEhJ40Y&list=RDMM&index=2'
itag = 22  # Example itag for 720p mp4
output_path = 'Downloads/'

# Download the video
download_specific_stream(video_url, itag, output_path)
