"""Shannon entropy calculation for datasets."""

import math
from collections import Counter
from typing import Sequence


def shannon_entropy(data: Sequence) -> float:
    """Calculate the Shannon entropy of a dataset.

    Shannon entropy measures the average amount of information (uncertainty)
    in a dataset. It is defined as:

        H(X) = -sum(p(x) * log2(p(x)))

    where p(x) is the probability of each unique value x in the dataset.

    Args:
        data: A sequence of values (e.g., list, tuple, string).

    Returns:
        The Shannon entropy in bits. Returns 0.0 for an empty dataset
        or a dataset with only one unique value.

    Raises:
        TypeError: If data is not iterable.
    """
    if not data:
        return 0.0

    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        probability = count / total
        entropy -= probability * math.log2(probability)

    return entropy
