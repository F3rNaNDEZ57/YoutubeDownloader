import tkinter as tk
from tkinter import filedialog, messagebox

# Function to browse and select download directory
def browse_directory():
    download_directory = filedialog.askdirectory(initialdir="/", title="Select Download Directory")
    download_path.set(download_directory)

# Function to download the YouTube video (functionality to be added later)
def download_video():
    messagebox.showinfo("Info", "Download functionality will be added later.")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("1000x200")
root.resizable(False, False)

# Variables
video_url = tk.StringVar()
download_path = tk.StringVar()

# Create and place widgets
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=video_url, width=50).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Download Directory:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=download_path, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_directory).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Download", command=download_video, bg="green", fg="white").grid(row=2, column=1, pady=20)

# Start the main event loop
root.mainloop()
