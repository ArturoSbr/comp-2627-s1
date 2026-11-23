import importlib
import os
import sys
import traceback
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Ensure working directory is `assignments/assignment-02/code/` so relative
# paths (`../data/*.csv`) and `import main` work regardless of where
# `grader.py` is called from
CODE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CODE_DIR)
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)


# ------------------------------ Dataset Config -------------------------------

DATA_PATH = os.path.join('..', 'data', 'default.csv')
TARGET_COL = 'default'
FEATURE_COLS = ['student', 'balance', 'income']


def load_data(path=DATA_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f'Dataset not found at `{path}`. Make sure the CSV file is placed '
            f'inside `assignments/assignment-02/data/`.'
        )

    df = pd.read_csv(path)
    y = df[TARGET_COL].to_numpy(dtype=float)

    X_raw = df[FEATURE_COLS].to_numpy(dtype=float)
    # Standardize features so full-batch gradient descent converges smoothly
    X_scaled = (X_raw - X_raw.mean(axis=0)) / X_raw.std(axis=0)
    # Prepend an intercept column of 1s: shape (n, 1 + len(FEATURE_COLS))
    X = np.column_stack([np.ones(len(df)), X_scaled])
    return X, y


# ------------------------------ Expected Values ------------------------------

X_TEST = np.array([
    [1.0, -1.5, 0.5],
    [1.0, -0.5, -1.0],
    [1.0, 0.0, 0.2],
    [1.0, 0.8, 1.2],
    [1.0, 1.7, -0.4],
])
Y_TEST = np.array([0.0, 0.0, 1.0, 1.0, 1.0])
BETA_TEST = np.array([-0.2, 0.7, -0.4])
ALPHA_TEST = 0.1


def _ref_p_hat(X, beta):
    probs = 1.0 / (1.0 + np.exp(-(X @ beta)))
    return np.clip(probs, 1e-15, 1.0 - 1e-15)


def _ref_nabla(X, y, probs):
    return (X.T @ (probs - y)) / len(y)


def _ref_update(beta, gradient, alpha):
    return beta - alpha * gradient


def _ref_gd_steps(X, y, alpha, n_steps):
    beta = np.zeros(X.shape[1], dtype=float)
    for _ in range(n_steps):
        probs = _ref_p_hat(X, beta)
        gradient = _ref_nabla(X, y, probs)
        beta = _ref_update(beta, gradient, alpha)
    return beta


PROBS_EXP = _ref_p_hat(X_TEST, BETA_TEST)
PROBS_ZERO_EXP = np.full(len(X_TEST), 0.5)
GRADIENT_EXP = _ref_nabla(X_TEST, Y_TEST, PROBS_EXP)
BETA_NEXT_EXP = _ref_update(BETA_TEST, GRADIENT_EXP, ALPHA_TEST)
GD_5_STEPS_EXP = _ref_gd_steps(X_TEST, Y_TEST, alpha=0.5, n_steps=5)


# -------------------------------- Assertions ---------------------------------

def get_func(student_module, name):
    assert student_module is not None, (
        '`main.py` failed to import (fix any syntax/import errors first)'
    )
    assert hasattr(student_module, name), (
        f'Function `{name}` was not found in `main.py`'
    )
    fn = getattr(student_module, name)
    assert callable(fn), f'`{name}` must be a function'
    return fn


def check_array(actual, expected, name, atol=1e-8, rtol=1e-5):
    assert not isinstance(actual, bool), (
        f'`{name}` returned a boolean (did you replace `True`?)'
    )
    assert isinstance(actual, np.ndarray), (
        f'`{name}` must return a NumPy array, got {type(actual).__name__}'
    )
    if actual.shape != expected.shape:
        hint = ''
        if actual.ndim == 2 and actual.shape == (expected.shape[0], 1):
            hint = ' (make sure to use a 1D array, e.g. `np.zeros(X.shape[1])`)'
        raise AssertionError(
            f'Expected shape {expected.shape} from `{name}`, '
            f'got {actual.shape}{hint}'
        )
    assert np.all(np.isfinite(actual)), (
        f'`{name}` returned non-finite values (NaN or inf)'
    )
    max_diff = float(np.max(np.abs(actual - expected)))
    assert np.allclose(actual, expected, atol=atol, rtol=rtol), (
        f'Values from `{name}` do not match expected output '
        f'(max abs diff = {max_diff:.6g})'
    )


def grade(student_module=None, data_path=DATA_PATH):
    if student_module is None:
        try:
            print('Importing student code from `main.py`...')
            student_module = importlib.import_module('main')
            print('Import completed successfully.\n')
        except Exception as e:
            print(f'\nImport encountered an error: {e}')
            traceback.print_exc(limit=2)
            print('\nContinuing grading with available definitions...\n')

    score = 0
    total = 5

    # Q1: p_hat
    try:
        fn = get_func(student_module, 'p_hat')
        actual = fn(X_TEST, BETA_TEST)
        check_array(actual, PROBS_EXP, 'p_hat')
        actual_zero = fn(X_TEST, np.zeros(X_TEST.shape[1]))
        check_array(actual_zero, PROBS_ZERO_EXP, 'p_hat')
        print('Q1 (p_hat): CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q1 (p_hat): FAILED ({e})')

    # Q2: nabla
    try:
        fn = get_func(student_module, 'nabla')
        actual = fn(X_TEST, Y_TEST, PROBS_EXP)
        check_array(actual, GRADIENT_EXP, 'nabla')
        print('Q2 (nabla): CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q2 (nabla): FAILED ({e})')

    # Q3: update
    try:
        fn = get_func(student_module, 'update')
        actual = fn(BETA_TEST.copy(), GRADIENT_EXP, ALPHA_TEST)
        check_array(actual, BETA_NEXT_EXP, 'update')
        print('Q3 (update): CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q3 (update): FAILED ({e})')

    # Q4: logistic_regression initialization & loop wiring (5 GD steps)
    try:
        fn = get_func(student_module, 'logistic_regression')
        actual = fn(X_TEST, Y_TEST, alpha=0.5, tol=1e-12, max_iter=5)
        check_array(actual, GD_5_STEPS_EXP, 'logistic_regression')
        print('Q4 (logistic_regression loop): CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q4 (logistic_regression loop): FAILED ({e})')

    # Q5: logistic_regression convergence on dataset vs. statsmodels Logit MLE
    try:
        fn = get_func(student_module, 'logistic_regression')
        X_data, y_data = load_data(data_path)
        beta_mle = sm.Logit(y_data, X_data).fit(disp=False).params
        beta_hat = fn(X_data, y_data)
        check_array(
            beta_hat,
            beta_mle,
            'logistic_regression',
            atol=1e-3,
            rtol=1e-3,
        )
        print('Q5 (logistic_regression on dataset): CORRECT (+1)')
        score += 1
    except Exception as e:
        print(f'Q5 (logistic_regression on dataset): FAILED ({e})')

    print('\n' + '=' * 80)
    print(f'FINAL SCORE: {score} / {total}'.center(80))
    print('=' * 80)

    if score < total:
        sys.exit(1)


if __name__ == '__main__':
    grade()
