import pandas as pd

# Q1. Read the three CSV files.
albums = pd.read_csv("../data/albums.csv")
songs = pd.read_csv("../data/songs.csv")
features = pd.read_csv("../data/song_features.csv")

# Q2. Count non-null guest appearances.
guest_appearances = features["featuring"].count()

# Q3. Compute the average Metacritic score.
mean_metacritic = albums["metacritic_score"].mean()

# Q4. Count bonus tracks.
bonus_tracks = features["bonus_track"].sum()

# Q5. Join albums and songs by album name.
albums_songs = pd.merge(albums, songs, on="album_name", how="inner")

# Q6. Join the result with song features by track name.
df = pd.merge(albums_songs, features, on="track_name", how="inner")

# Q7. Compute the average tempo per album as a Series.
mean_tempo = df.groupby("album_name")["tempo"].mean()

# Q8. Summarize track count, total duration, and average energy per album.
album_summary = df.groupby("album_name").agg({
    "track_name": "count",
    "duration_ms": "sum",
    "energy": "mean",
})
