import pandas as pd

# Q1. Cargar los datos
albums = pd.read_csv("../data/albums.csv")
songs = pd.read_csv("../data/songs.csv")
features = pd.read_csv("../data/song_features.csv")

# Q2 a Q4. Invitados, calificación media y pistas extra
guest_appearances = features["featuring"].count()
mean_metacritic = albums["metacritic_score"].mean()
bonus_tracks = features["bonus_track"].sum()

# Q5 y Q6. Unir las tablas
albums_songs = pd.merge(albums, songs, on="album_name", how="inner")
df = pd.merge(albums_songs, features, on="track_name", how="inner")

# Q7 y Q8. Resumir los datos por álbum
mean_tempo = df.groupby("album_name")["tempo"].mean()
album_summary = df.groupby("album_name").agg({
    "track_name": "count",
    "duration_ms": "sum",
    "energy": "mean",
})
