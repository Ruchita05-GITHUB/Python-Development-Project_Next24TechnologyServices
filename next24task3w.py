import tkinter
from tkinter import messagebox
import requests

def fetch_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    
    if artist and song:
        try:
            url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
            response = requests.get(url)
            data = response.json()
            lyrics = data.get("lyrics", "Lyrics could not be found.")
            display_lyrics(lyrics)
            status_bar.config(text="Lyrics generated successfully.", fg="blue")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Cannot  fetch lyrics: {str(e)}")
            status_bar.config(text="Error fetching lyrics.", fg="red")
    else:
        messagebox.showwarning("Input Error", "Please enter both artist and song name.")
        status_bar.config(text="Input error.", fg="pink")

def display_lyrics(lyrics):
    lyrics_text.config(state=tkinter.NORMAL)  # Allow editing to update text
    lyrics_text.delete(1.0, tkinter.END)
    lyrics_text.insert(tkinter.END, lyrics)
    lyrics_text.config(state=tkinter.DISABLED)  # Disable editing after updating text

# Create the main window
root = tkinter.Tk()
root.title("Lyrics Extractor")
root.configure(bg='lightgray')

# Artist label and entry
tkinter.Label(root, text="Artist", bg='#f0f0f0', font=('Helvetica', 14)).grid(row=0, column=0, padx=10, pady=10)
artist_entry = tkinter.Entry(root, font=('Helvetica', 12))
artist_entry.grid(row=0, column=1, padx=10, pady=10)

# Song label and entry
tkinter.Label(root, text="Song", bg='#f0f0f0', font=('Helvetica', 14)).grid(row=1, column=0, padx=10, pady=10)
song_entry = tkinter.Entry(root, font=('Helvetica', 12))
song_entry.grid(row=1, column=1, padx=10, pady=10)

# Get Lyrics button
get_lyrics_button = tkinter.Button(root, text="Get Lyrics", command=fetch_lyrics, bg='#C1FFC1', fg='blue', font=('Helvetica', 12, 'bold'))
get_lyrics_button.grid(row=2, column=0, columnspan=2, pady=10)

# Lyrics text box
lyrics_text = tkinter.Text(root, wrap='word', height=15, width=50, bg='#FFB6C1', state=tkinter.DISABLED)  # Read-only text box
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Status bar
status_bar = tkinter.Label(root, text="Enter artist's name  and song name to get lyrics.", bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
status_bar.grid(row=4, column=0, columnspan=2, sticky=tkinter.W+tkinter.E, padx=10, pady=10)

# Run the application
root.mainloop()
