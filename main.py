from tkinter import *
import requests  


def fetch_lyrics():
    artist = artist_entry.get().strip()
    song_title = song_title_entry.get().strip()
    
    if artist and song_title:
        try:
            response = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song_title}")
            data = response.json()
            
            
            print(data)
            
            if 'lyrics' in data:
                lyrics_text.config(state=NORMAL)  
                lyrics_text.delete(1.0, END)
                lyrics_text.insert(END, data['lyrics'])
                lyrics_text.config(state=DISABLED)  
            else:
                lyrics_text.config(state=NORMAL)
                lyrics_text.delete(1.0, END)
                lyrics_text.insert(END, "Lyrics not found. Please check the artist and song title.")
                lyrics_text.config(state=DISABLED)
        except Exception as e:
            lyrics_text.config(state=NORMAL)
            lyrics_text.delete(1.0, END)
            lyrics_text.insert(END, f"Error: {str(e)}")
            lyrics_text.config(state=DISABLED)
    else:
        lyrics_text.config(state=NORMAL)
        lyrics_text.delete(1.0, END)
        lyrics_text.insert(END, "Please enter both artist and song title.")
        lyrics_text.config(state=DISABLED)


window = Tk()
window.title("Song Lyrics Extractor")
window.geometry("600x400")  
window.configure(bg="#f2f2f2")


artist_label = Label(window, text="Artist:", font=("Helvetica", 12, "bold"), bg="#f2f2f2")
artist_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

song_title_label = Label(window, text="Song Title:", font=("Helvetica", 12, "bold"), bg="#f2f2f2")
song_title_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)


artist_entry = Entry(window, width=40, font=("Helvetica", 12), bd=2, relief=GROOVE)
artist_entry.grid(row=0, column=1, padx=10, pady=10)

song_title_entry = Entry(window, width=40, font=("Helvetica", 12), bd=2, relief=GROOVE)
song_title_entry.grid(row=1, column=1, padx=10, pady=10)


fetch_button = Button(window, text="Fetch Lyrics", command=fetch_lyrics, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", bd=2, relief=RAISED)
fetch_button.grid(row=2, column=0, columnspan=2, pady=20)


lyrics_text = Text(window, wrap=WORD, height=10, width=60, font=("Helvetica", 12), bg="#ffffff", bd=2, relief=GROOVE)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
lyrics_text.config(state=DISABLED)  

window.mainloop()
