import sys
from typing import Tuple
import numpy as np
from sklearn.metrics import precision_score, recall_score


def read_positive_int(prompt: str = "Enter a positive integer N: ") -> int:
    """Read a positive integer from stdin."""
    while True:
        try:
            raw = input(prompt).strip()
            n = int(raw)
            if n <= 0:
                raise ValueError
            return n
        except ValueError:
            print("Invalid input. Please enter a positive integer (e.g., 5).")


def read_binary_label(prompt: str) -> int:
    """Read a single binary label {0,1} from stdin."""
    while True:
        raw = input(prompt).strip()
        if raw in ("0", "1"):
            return int(raw)
        print("Invalid input. Please enter 0 or 1.")


def read_xy_points(n: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Read N (x, y) points one by one.
    X = ground-truth labels, Y = predicted labels. Both must be {0,1}.
    Returns:
        y_true (np.ndarray), y_pred (np.ndarray)
    """
    # Initialize with NumPy
    y_true = np.empty(n, dtype=np.int64)
    y_pred = np.empty(n, dtype=np.int64)

    print("\nPlease provide N (x, y) label pairs.")
    print("For each pair, enter x first (ground truth), then y (predicted). Both must be 0 or 1.\n")

    for i in range(n):
        x_i = read_binary_label(f"[{i+1}/{n}] Enter x (ground truth, 0 or 1): ")
        y_i = read_binary_label(f"[{i+1}/{n}] Enter y (predicted, 0 or 1): ")
        # Insert into NumPy arrays
        y_true[i] = x_i
        y_pred[i] = y_i

    return y_true, y_pred


def main() -> int:
    print("=== Precision & Recall (scikit-learn) ===")
    n = read_positive_int("Enter N (number of (x, y) pairs): ")
    y_true, y_pred = read_xy_points(n)

    # Compute metrics with scikit-learn
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    # Output
    print("\n--- Results ---")
    print(f"Precision: {precision:.6f}")
    print(f"Recall:    {recall:.6f}")

    # Optional: show class distribution for sanity check
    unique, counts = np.unique(y_true, return_counts=True)
    dist = {int(k): int(v) for k, v in zip(unique, counts)}
    print("\n(Info) Ground-truth class distribution:", dist)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(1)
