import pandas as pd

# Q1. Read all tables by replacing `True` with a function that reads the
# corresponding CSV files from `../data/` (`../data/albums.csv`,
# `../data/songs.csv`, and `../data/song_features.csv`)
albums = pd.read_csv('../data/albums.csv')
songs = pd.read_csv('../data/songs.csv')
features = pd.read_csv('../data/song_features.csv')

# Q2. How many songs have a guest appearance? Use table `features` and column
# `featuring` to count the number of non-null entries
guest_appearances = features['featuring'].count()

# Q3. What is the average Metacritic score across all albums? Use table `albums`
# and column `metacritic_score` to compute the mean
mean_metacritic = albums['metacritic_score'].mean()

# Q4. How many songs are bonus tracks? Use table `features` and column
# `bonus_track` to sum the number of bonus tracks
bonus_tracks = features['bonus_track'].sum()

# Q5. Perform an inner join between `albums` (left) and `songs` (right) on
# `album_name` using `pd.merge()`
albums_songs = pd.merge(albums,songs, on='album_name', how='inner')

# Q6. Perform an inner join between `albums_songs` (left) and `features` (right)
# on `track_name` using `pd.merge()`
df = pd.merge(albums_songs, features, on='track_name', how='inner')

# Q7. Group `df` by `album_name` and compute the average (`mean`) `tempo` per
# album as a pandas Series
mean_tempo = df.groupby('album_name')['tempo'].mean()

# Q8. Group `df` by `album_name` and use `.agg()` with a dictionary to compute:
# - `'track_name': 'count'`
# - `'duration_ms': 'sum'`
# - `'energy': 'mean'`
album_summary = df.groupby('album_name').agg({
'track_name':'count',
'duration_ms':'sum',
'energy':'mean',
})