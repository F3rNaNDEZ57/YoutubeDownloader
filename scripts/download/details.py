from pytube import YouTube

def get_thumbnail_url(youtube_url):
    try:
        yt = YouTube(youtube_url)
        return yt.thumbnail_url
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
youtube_url = "https://www.youtube.com/watch?v=HJcGD8Ubv1g"
thumbnail_url = get_thumbnail_url(youtube_url)
print(thumbnail_url)