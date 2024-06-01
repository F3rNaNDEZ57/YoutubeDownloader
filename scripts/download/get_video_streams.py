from pytube import YouTube


# Function to list available streams
def list_streams(video_url):
    try:
        # Create YouTube object
        yt = YouTube(video_url)
        
        # List all available streams
        for stream in yt.streams.filter(progressive=True):
            print(f'{stream.itag} - {stream.mime_type} - {stream.resolution}')
    
    except Exception as e:
        print(f'An error occurred: {e}')

# URL of the YouTube video
video_url = 'https://www.youtube.com/watch?v=DF3XjEhJ40Y&list=RDMM&index=2'

# List available streams
list_streams(video_url)
