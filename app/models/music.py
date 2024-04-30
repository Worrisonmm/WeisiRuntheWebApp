from app.db import BaseModel

class Music(BaseModel):

    SHEET_NAME = "musics"

    COLUMNS = ["title", "composer"]

    SEEDS = [
        {"title": "Swan Lake", "composer": "Pyotr Ilyich Tchaikovsky"},
         {"title": "Also sprach Zarathustra", "composer": "Richard Strauss"},
       
    ]

if __name__ == "__main__":

    musics = Music.all()
    print("FOUND", len(musics), "BOOKS")
    if any(musics):
        for music in musics:
            print(music.title, music.author, music.year)
    else:
        Music.seed()


