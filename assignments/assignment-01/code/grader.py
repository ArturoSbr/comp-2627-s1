import os
import sys
import traceback
import numpy as np
import pandas as pd

# Ensure working directory is `assignments/assignment-01/code/` so `main.py`
# can read `../data/*.csv` regardless of where `grader.py` is called from
CODE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_PATH = os.path.join(CODE_DIR, 'main.py')
os.chdir(CODE_DIR)


# ------------------------------ Expected Values ------------------------------

albums_exp = pd.read_csv('../data/albums.csv')
songs_exp = pd.read_csv('../data/songs.csv')
features_exp = pd.read_csv('../data/song_features.csv')

guest_appearances_exp = features_exp['featuring'].count()
mean_metacritic_exp = albums_exp['metacritic_score'].mean()
bonus_tracks_exp = features_exp['bonus_track'].sum()

albums_songs_exp = pd.merge(albums_exp, songs_exp, on='album_name', how='inner')
df_exp = pd.merge(albums_songs_exp, features_exp, on='track_name', how='inner')

mean_tempo_exp = df_exp.groupby('album_name')['tempo'].mean()
album_summary_exp = df_exp.groupby('album_name').agg({
    'track_name': 'count',
    'duration_ms': 'sum',
    'energy': 'mean',
})


# -------------------------------- Assertions ---------------------------------

def get_var(student_globals, name):
    assert name in student_globals, (
        f'`{name}` was not found (script may have crashed before defining it)'
    )
    return student_globals[name]


def check_scalar(student_globals, expected, name):
    actual = get_var(student_globals, name)
    assert not isinstance(actual, bool), f'`{name}` is still a boolean'
    assert np.isclose(actual, expected), (
        f'Expected `{name}` to be {expected}, got {actual}'
    )


def grade(student_globals=None):
    if student_globals is None:
        student_globals = {}
        try:
            print('Executing student code...')
            with open(MAIN_PATH, 'r', encoding='utf-8') as f:
                student_code = f.read()
            exec(student_code, student_globals)
            print('Execution completed successfully.\n')
        except Exception as e:
            print(f'\nExecution encountered an error: {e}')
            traceback.print_exc(limit=2)
            print('\nContinuing grading with available variables...\n')

    score = 0
    total = 8

    # Q1
    try:
        albums = get_var(student_globals, 'albums')
        songs = get_var(student_globals, 'songs')
        features = get_var(student_globals, 'features')
        assert isinstance(albums, pd.DataFrame), '`albums` must be a DataFrame'
        assert isinstance(songs, pd.DataFrame), '`songs` must be a DataFrame'
        assert isinstance(features, pd.DataFrame), (
            '`features` must be a DataFrame'
        )
        pd.testing.assert_frame_equal(albums, albums_exp)
        pd.testing.assert_frame_equal(songs, songs_exp)
        pd.testing.assert_frame_equal(features, features_exp)
        print('Q1: CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q1: FAILED ({e})')

    # Q2
    try:
        check_scalar(
            student_globals,
            guest_appearances_exp,
            'guest_appearances',
        )
        print('Q2: CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q2: FAILED ({e})')

    # Q3
    try:
        check_scalar(
            student_globals,
            mean_metacritic_exp,
            'mean_metacritic',
        )
        print('Q3: CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q3: FAILED ({e})')

    # Q4
    try:
        check_scalar(student_globals, bonus_tracks_exp, 'bonus_tracks')
        print('Q4: CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q4: FAILED ({e})')

    # Q5
    try:
        albums_songs = get_var(student_globals, 'albums_songs')
        assert isinstance(albums_songs, pd.DataFrame), (
            '`albums_songs` must be a DataFrame'
        )
        pd.testing.assert_frame_equal(albums_songs, albums_songs_exp)
        print('Q5: CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q5: FAILED ({e})')

    # Q6
    try:
        df = get_var(student_globals, 'df')
        assert isinstance(df, pd.DataFrame), '`df` must be a DataFrame'
        pd.testing.assert_frame_equal(df, df_exp)
        print('Q6: CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q6: FAILED ({e})')

    # Q7
    try:
        mean_tempo = get_var(student_globals, 'mean_tempo')
        assert isinstance(mean_tempo, pd.Series), (
            '`mean_tempo` must be a Series'
        )
        pd.testing.assert_series_equal(mean_tempo, mean_tempo_exp)
        print('Q7: CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q7: FAILED ({e})')

    # Q8
    try:
        album_summary = get_var(student_globals, 'album_summary')
        assert isinstance(album_summary, pd.DataFrame), (
            '`album_summary` must be a DataFrame'
        )
        pd.testing.assert_frame_equal(album_summary, album_summary_exp)
        print('Q8: CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q8: FAILED ({e})')

    print('\n' + '=' * 80)
    print(f'FINAL SCORE: {score} / {total}'.center(80))
    print('=' * 80)

    if score < total:
        sys.exit(1)


if __name__ == '__main__':
    grade()
