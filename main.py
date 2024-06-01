import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from scripts import download_youtube_video, progress_function

# Function to browse and select download directory
def browse_directory():
    download_directory = filedialog.askdirectory(initialdir="/", title="Select Download Directory")
    download_path.set(download_directory)

# Function to update the progress bar
def update_progress(stream, chunk, bytes_remaining):
    percentage_of_completion = progress_function(stream, chunk, bytes_remaining)
    progress_var.set(percentage_of_completion)
    root.update_idletasks()

# Function to start the download
def start_download():
    try:
        download_youtube_video(video_url.get(), download_path.get(), update_progress)
        messagebox.showinfo("Info", "Download successful.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("700x300")
root.resizable(True, True)

# Variables
video_url = tk.StringVar()
download_path = tk.StringVar()
progress_var = tk.DoubleVar()

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

tk.Button(root, text="Download", command=start_download, font=("Arial", 12), bg="green", fg="white").grid(row=2, column=1, pady=20)

# Add the progress bar
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="WE")

# Make the UI responsive
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
