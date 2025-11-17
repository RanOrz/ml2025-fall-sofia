import sys
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def read_int(prompt):
    while True:
        try:
            v = int(input(prompt).strip())
            return v
        except ValueError:
            print("Please enter an integer.")

def read_float(prompt):
    while True:
        try:
            v = float(input(prompt).strip())
            return v
        except ValueError:
            print("Please enter a real number.")

def main():
    # Read N (positive integer)
    N = read_int("Please enter the number of points N (positive integer):")
    if N <= 0:
        print("Error: N must be a positive integer.")
        sys.exit(1)

    # Read k (a positive integer)
    k = read_int("Please enter the nearest neighbor number k (a positive integer):")
    if k <= 0:
        print("Error: k must be a positive integer.")
        sys.exit(1)

    # Data initialization (pre-allocation) is performed using NumPy, where x is a 1D feature.
    X = np.empty((N, 1), dtype=float)  # The eigenvalue matrix has a shape of (N, 1).
    y = np.empty((N,), dtype=float)    # Label vector, shape (N, )

    # Read N (x, y) points one by one, and use NumPy to perform data "insertion" (fill in each item).
    print(f"Read N (x, y) points one by one, and use NumPy to perform data "insertion" (fill in each item).")
    for i in range(N):
        xi = read_float(f"x at the {i+1}th point:")
        yi = read_float(f"y at the {i+1}th point:")
        X[i, 0] = xi
        y[i] = yi

    # Output the variance of the labels in the training dataset (unbiased sample variance ddof=1).
    # To determine the overall variance, set ddof=0.
    y_variance = np.var(y, ddof=1) if N > 1 else 0.0
    print(f"Sample variance of training set label y (ddof=1): {y_variance}")

    # Verify the relationship between k and N
    if k > N:
        print(f"Error: k({k}) cannot be greater than N({N}).")
        sys.exit(1)

    #Read the query point X (real number).
    X_query = read_float("Please enter the position X (real number) to predict:")
    X_query_arr = np.array([[X_query]], dtype=float)

    # Using scikit-learn for k-NN regression
    # The default metric is Euclidean distance, and the weights are uniform.
    try:
        knn = KNeighborsRegressor(n_neighbors=k, metric='minkowski', p=2, weights='uniform')
        knn.fit(X, y)
        pred = knn.predict(X_query_arr)[0]
        print(f"k-NN regression (k={k}) prediction Y at X={X_query}: {pred}")
    except Exception as e:
        print("An error occurred while running k-NN regression:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
