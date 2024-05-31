from pytube import YouTube


def download_youtube_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        # print(yt)
        
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        # print(stream)
        
        stream.download(output_path)
        
        print(f'Video "{yt.title}" has been downloaded successfully and saved to "{output_path}"')
    
    except Exception as e:
        print(f'An error occurred: {e}')


video_url = 'https://www.youtube.com/watch?v=DF3XjEhJ40Y&list=RDMM&index=2'
output_path = 'Downloads/'

download_youtube_video(video_url, output_path)
