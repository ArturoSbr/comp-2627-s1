import pandas as pd

# Q1. Read all tables by replacing `True` with a function that reads the
# corresponding CSV files from `../data/` (`../data/albums.csv`,
# `../data/songs.csv`, and `../data/song_features.csv`)
albums = pd.read_csv("../data/albums.csv")
print(albums)
songs = pd.read_csv("../data/songs.csv")
print(songs)
features = pd.read_csv("../data/song_features.csv")
print(features)
# Q2. How many songs have a guest appearance? Use table `features` and column
# `featuring` to count the number of non-null entries
guest_appearances = len(features["featuring"])-features["featuring"].isna().sum()
print(guest_appearances)

# Q3. What is the average Metacritic score across all albums? Use table `albums`
# and column `metacritic_score` to compute the mean
mean_metacritic = albums["metacritic_score"].sum()/(len(albums["metacritic_score"])-albums["metacritic_score"].isna().sum())
print(mean_metacritic)

# Q4. How many songs are bonus tracks? Use table `features` and column
# `bonus_track` to sum the number of bonus tracks
bonus_tracks = features["bonus_track"].sum()
print(bonus_tracks)

# Q5. Perform an inner join between `albums` (left) and `songs` (right) on
# `album_name` using `pd.merge()`
albums_songs = pd.merge(albums, songs, on="album_name", how="inner")
print(albums_songs)
# Q6. Perform an inner join between `albums_songs` (left) and `features` (right)
# on `track_name` using `pd.merge()`
df = pd.merge(albums_songs, features, on="track_name", how="inner")
print(df)

# Q7. Group `df` by `album_name` and compute the average (`mean`) `tempo` per
# album as a pandas Series
mean_tempo = df.groupby("album_name")["tempo"].mean()
print(mean_tempo)
# Q8. Group `df` by `album_name` and use `.agg()` with a dictionary to compute:
# - `'track_name': 'count'`
# - `'duration_ms': 'sum'`
# - `'energy': 'mean'`
album_summary = df.groupby("album_name").agg({
    "track_name": "count",
    "duration_ms": "sum",
    "energy": "mean"
})
print(album_summary)