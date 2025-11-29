# module9_knn_gridsearchcv.py

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


def read_dataset(name):
    """
    Read dataset from user input.
    Returns:
        X (numpy array): feature column
        y (numpy array): label column
    """
    n = int(input(f"Enter number of samples for {name}: "))
    X_list = []
    y_list = []

    print(f"Provide {n} (x, y) pairs for {name}:")
    for i in range(n):
        x = float(input(f"  x[{i+1}]: "))
        y = int(input(f"  y[{i+1}]: "))
        X_list.append([x])  # feature must be 2D for sklearn
        y_list.append(y)

    return np.array(X_list), np.array(y_list)


def main():
    print("===== kNN Classifier with GridSearchCV =====")

    # Read training set
    X_train, y_train = read_dataset("TRAINING SET")

    # Read test set
    X_test, y_test = read_dataset("TEST SET")

    # Define model and hyperparameter grid
    knn = KNeighborsClassifier()
    param_grid = {"n_neighbors": list(range(1, 11))}  # k = 1..10

    # Grid search with 5-fold cross-validation
    grid = GridSearchCV(knn, param_grid, cv=5)
    grid.fit(X_train, y_train)

    best_k = grid.best_params_["n_neighbors"]
    print("\nBest k from GridSearchCV:", best_k)

    # Evaluate on test set
    y_pred = grid.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    print("Test Accuracy:", test_accuracy)
    print("===========================================")


if __name__ == "__main__":
    main()
