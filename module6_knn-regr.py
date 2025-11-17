from __future__ import annotations
import sys
from typing import Tuple
import numpy as np


class XYDataset:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity")
        self._xs = np.empty(capacity, dtype=float)
        self._ys = np.empty(capacity, dtype=float)
        self._size = 0

    def insert(self, x: float, y: float) -> None:
        if self._size >= self._xs.shape[0]:
            raise IndexError("The data is full and cannot be inserted again.")
        self._xs[self._size] = x
        self._ys[self._size] = y
        self._size += 1

    @property
    def xs(self) -> np.ndarray:
        return self._xs[: self._size]

    @property
    def ys(self) -> np.ndarray:
        return self._ys[: self._size]

    @property
    def size(self) -> int:
        return self._size

    def y_variance(self) -> float:
        """Returns the variance of label y (population variance) ddof=0）。"""
        if self._size == 0:
            return float("nan")
        return float(np.var(self.ys, ddof=0))


def knn_regression_predict(X: float, xs: np.ndarray, ys: np.ndarray, k: int) -> float:
    if k <= 0:
        raise ValueError("k Must be a positive integer")
    n = xs.shape[0]
    if k > n:
        raise ValueError(f"k(={k}) Cannot exceed the sample size N(={n})")

    dists = np.abs(xs - X)
    nn_idx = np.argpartition(dists, kth=k-1)[:k]
    y_hat = float(np.mean(ys[nn_idx]))
    return y_hat


def _read_positive_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(prompt).strip())
            if val <= 0:
                print("Please enter a positive integer.")
                continue
            return val
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def _read_two_floats(prompt: str) -> Tuple[float, float]:
    while True:
        line = input(prompt).strip()
        parts = line.replace(",", " ").split()
        if len(parts) != 2:
            print("Please enter only two real numbers, separated by a space (example: 1.2 3.4).")
            continue
        try:
            x = float(parts[0])
            y = float(parts[1])
            return x, y
        except ValueError:
            print("Parsing failed. Please ensure that the input is a real number.")


def _read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input, please enter a real number.")


def main() -> None:
    print(" ")

    N = _read_positive_int("Please enter the number of samples N (positive integer):")
    k = _read_positive_int("Please enter the number of neighbors k (a positive integer):")

    dataset = XYDataset(capacity=N)
    for i in range(N):
        x, y = _read_two_floats(f"Please enter the x and y values ​​(separated by spaces) for the {i+1}/{N}th point:")
        dataset.insert(x, y)

    X = _read_float("Please enter the X (real number) you want to predict:")

    if k > dataset.size:
        print(f"Error: k(={k}) is greater than N(={dataset.size}), k-NN regression cannot be performed.")
        sys.exit(1)

    y_hat = knn_regression_predict(X, dataset.xs, dataset.ys, k)
    print("\n")
    print(f"The variance of the training set label y (ddof=0): {dataset.y_variance():.6f}")
    print(f"When k = {k} and X = {X}, the k-NN regression prediction value Y_hat = {y_hat:.6f}")


if __name__ == "__main__":
    main()
