import pandas as pd

# Q1. Read all tables by replacing `True` with a function that reads the
# corresponding CSV files from `../data/` (`../data/albums.csv`,
# `../data/songs.csv`, and `../data/song_features.csv`)
albums = True
songs = True
features = True

# Q2. How many songs have a guest appearance? Use table `features` and column
# `featuring` to count the number of non-null entries
guest_appearances = True

# Q3. What is the average Metacritic score across all albums? Use table `albums`
# and column `metacritic_score` to compute the mean
mean_metacritic = True

# Q4. How many songs are bonus tracks? Use table `features` and column
# `bonus_track` to sum the number of bonus tracks
bonus_tracks = True

# Q5. Perform an inner join between `albums` (left) and `songs` (right) on
# `album_name` using `pd.merge()`
albums_songs = True

# Q6. Perform an inner join between `albums_songs` (left) and `features` (right)
# on `track_name` using `pd.merge()`
df = True

# Q7. Group `df` by `album_name` and compute the average (`mean`) `tempo` per
# album as a pandas Series
mean_tempo = True

# Q8. Group `df` by `album_name` and use `.agg()` with a dictionary to compute:
# - `'track_name': 'count'`
# - `'duration_ms': 'sum'`
# - `'energy': 'mean'`
album_summary = True
