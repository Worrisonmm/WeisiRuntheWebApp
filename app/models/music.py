from app.db import BaseModel

class Music(BaseModel):

    SHEET_NAME = "musics"

    COLUMNS = ["title", "composer"]

    SEEDS = [
        {"title": "Swan Lake", "composer": "Pyotr Ilyich Tchaikovsky"},
        {"title": "Also sprach Zarathustra", "composer": "Richard Strauss"},
        {"title": "Overture to Fidelio", "composer": "Ludwig van Beethoven"},
        {"title": "Romances for violin and orchestra", "composer": "Ludwig van Beethoven"},
        {"title": "Symphony No. 9", "composer": "Anton Bruckner"},
        {"title": "Piano Concerto No. 1", "composer": "Franz Liszt"},
        {"title": "Symphonie fantastique", "composer": "Hector Berlioz"},
    ]

if __name__ == "__main__":

    musics = Music.all()
    print("FOUND", len(musics), "BOOKS")
    if any(musics):
        for music in musics:
            print(music.title, music.composer)
    else:
        Music.seed()


