import numpy as np


# Q1. Complete `p_hat(X, beta)` to compute the predicted probabilities:
#     z = X @ beta
#     p_hat = 1 / (1 + exp(-z))
# Replace each `True` with your NumPy code (hint: use `@` for matrix-vector
# multiplication and `np.exp()` for the exponential).
def p_hat(X, beta):
    z = True
    probs = True
    # Clip probabilities strictly inside (0, 1) so extreme linear scores do not
    # round to exact 0.0 or 1.0 in floating-point arithmetic (which would cause
    # log(0) = -inf / NaN if evaluated in the negative log-likelihood J(beta)).
    return np.clip(probs, 1e-15, 1 - 1e-15)


# Q2. Complete `nabla(X, y, probs)` to compute the gradient of J(beta):
#     nabla = (1 / n) * X^T (probs - y)
# Replace `True` with your NumPy code (hint: `X.T` is the transpose of `X`,
# and `@` performs matrix-vector multiplication).
def nabla(X, y, probs):
    n = len(y)
    gradient = True
    return gradient


# Q3. Complete `update(beta, gradient, alpha)` to perform one gradient descent
# step:
#     beta_new = beta - alpha * gradient
# Replace `True` with your NumPy code.
def update(beta, gradient, alpha):
    beta_new = True
    return beta_new


# Q4 & Q5. Complete `logistic_regression` by replacing each `True` placeholder
# using your helper functions (`p_hat`, `nabla`, `update`):
# 1. Initialize `beta` as a 1D array of zeros of length p (hint: `X.shape[1]`
#    gives the number of columns p, and `np.zeros(...)` creates zeros).
# 2. Compute predicted probabilities `probs` using `p_hat()`.
# 3. Compute `gradient` using `nabla()`.
# 4. Update `beta` using `update()`.
# 5. Stop early when the norm of `gradient` is smaller than `tol`
#    (hint: `np.linalg.norm(gradient) < tol`).
def logistic_regression(X, y, alpha=0.5, tol=1e-6, max_iter=20_000):
    # Initialize beta as a 1D array of zeros of length p
    beta = True

    for _ in range(max_iter):
        # Compute predicted probabilities with p_hat()
        probs = True
        # Compute the gradient with nabla()
        gradient = True
        # Update beta with update()
        beta = True

        # Stop early when the gradient norm is smaller than tol
        if True:
            break

    return beta
