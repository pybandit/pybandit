import numpy as np
import pytest

from pybandit.bandit.bernoulli import (
    BernoulliBandit,
)

np.random.seed(0)


def test_initialization():
    """
    Test initialization of the BernoulliBandit with various probabilities.
    """
    # Normal initialization
    bandit = BernoulliBandit(0.3)
    assert bandit.p == 0.3, "Bandit should initialize with the correct probability."

    # Boundary initialization
    bandit_zero = BernoulliBandit(0)
    bandit_one = BernoulliBandit(1)
    assert bandit_zero.p == 0, "Bandit should handle probability of 0."
    assert bandit_one.p == 1, "Bandit should handle probability of 1."

    # Initialization with invalid probabilities
    with pytest.raises(ValueError):
        BernoulliBandit(-0.1)
    with pytest.raises(ValueError):
        BernoulliBandit(1.1)


def test_pull_returns_int():
    """
    Test if the pull method returns an integer.
    """
    bandit = BernoulliBandit(0.5)
    assert isinstance(bandit.pull(), int), "Pull method should return an integer."


def test_pull_valid_outputs():
    """
    Test if the pull method returns only valid outputs (0 or 1).
    """
    bandit = BernoulliBandit(0.5)
    outcomes = set(bandit.pull() for _ in range(1000))
    assert outcomes <= {0, 1}, "Pull method should only return 0 or 1."


def test_zero_probability():
    """
    Test that pulling the arm with zero probability always returns 0.
    """
    bandit = BernoulliBandit(0)
    results = [bandit.pull() for _ in range(100)]
    assert all(result == 0 for result in results), "With p=0, all results should be 0."


def test_one_probability():
    """
    Test that pulling the arm with probability one always returns 1.
    """
    bandit = BernoulliBandit(1)
    results = [bandit.pull() for _ in range(100)]
    assert all(result == 1 for result in results), "With p=1, all results should be 1."


def test_probability_distribution():
    """
    Test the distribution of outcomes to ensure it closely matches the Bernoulli distribution.
    """
    p = 0.75
    trials = 10000
    bandit = BernoulliBandit(p)
    results = [bandit.pull() for _ in range(trials)]
    successes = sum(results)
    proportion = successes / trials
    assert (
            pytest.approx(proportion, 0.02) == p
    ), f"Results should approximate the probability {p} within a reasonable margin."
