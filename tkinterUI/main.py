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
root.geometry("700x250")
root.resizable(True, True)

# Variables
video_url = tk.StringVar()
download_path = tk.StringVar()

# Configure grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=1)

# Create and place widgets
tk.Label(root, text="YouTube URL:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="E")
url_entry = tk.Entry(root, textvariable=video_url, font=("Arial", 12), width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky="W")

tk.Label(root, text="Download Directory:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="E")
directory_entry = tk.Entry(root, textvariable=download_path, font=("Arial", 12), width=50)
directory_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")
tk.Button(root, text="Browse", command=browse_directory, font=("Arial", 12)).grid(row=1, column=2, padx=10, pady=10, sticky="W")

tk.Button(root, text="Download", command=download_video, font=("Arial", 12), bg="green", fg="white").grid(row=2, column=1, pady=20)

# Make the UI responsive
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
