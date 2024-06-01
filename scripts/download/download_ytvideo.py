from pytube import YouTube

# Function to download a single YouTube video
def download_youtube_video(video_url, output_path, progress_callback):
    try:
        yt = YouTube(video_url, on_progress_callback=progress_callback)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        
        print(f'Video "{yt.title}" has been downloaded successfully and saved to "{output_path}"')
    
    except Exception as e:
        print(f'An error occurred: {e}')

# Function to track download progress
def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    return percentage_of_completion
