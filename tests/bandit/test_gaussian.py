import numpy as np
import pytest

from pybandit.bandit.gaussian import GaussianBandit

np.random.seed(0)


@pytest.fixture
def default_bandit():
    """Fixture to create a bandit with default parameters."""
    return GaussianBandit()


@pytest.fixture
def custom_bandit():
    """Fixture to create a bandit with custom parameters."""
    return GaussianBandit(mean=10, std_dev=5)


def test_default_initialization(default_bandit):
    """Test the initialization with default parameters."""
    assert default_bandit.mean == 0.0, "Default mean should be 0.0"
    assert default_bandit.std_dev == 1.0, "Default std_dev should be 1.0"


def test_custom_initialization(custom_bandit):
    """Test the initialization with custom parameters."""
    assert custom_bandit.mean == 10, "Custom mean should be 10"
    assert custom_bandit.std_dev == 5, "Custom std_dev should be 5"


@pytest.mark.parametrize("mean, std_dev", [(0, 1), (5, 2), (-3, 0.5)])
def test_pull_distribution_properties(mean, std_dev):
    """
    Test that the majority of the pull method returns values fall within 3 standard deviations
    for various means and standard deviations.
    """
    bandit = GaussianBandit(mean, std_dev)
    rewards = np.array([bandit.pull() for _ in range(9999999)])

    within_1st = np.mean(
        (mean - 1 * std_dev < rewards) & (rewards < mean + 1 * std_dev)
    )

    # At least 68% of rewards should fall within 1 standard deviations of the mean
    assert within_1st >= 0.68

    within_2nd = np.mean(
        (mean - 2 * std_dev < rewards) & (rewards < mean + 2 * std_dev)
    )
    # At least 95% of rewards should fall within 2 standard deviations of the mean
    assert within_2nd >= 0.95

    # At least 99.7% of rewards should fall within 3 standard deviations of the mean
    within_3sd = np.mean(
        (mean - 3 * std_dev < rewards) & (rewards < mean + 3 * std_dev)
    )
    assert within_3sd >= 0.97


def test_pull_returns_float(default_bandit):
    """Test that pulling the bandit's arm returns a float."""
    reward = default_bandit.pull()
    assert isinstance(reward, float), "Reward should be a float"


@pytest.fixture
def bandit(request):
    """General fixture that returns a bandit instance based on input parameters."""
    if request.param == "default":
        return GaussianBandit()
    elif request.param == "custom":
        return GaussianBandit(mean=10, std_dev=5)


@pytest.mark.parametrize("bandit", ["default", "custom"], indirect=True)
def test_pull_statistical_properties(bandit):
    """Statistical test to check if generated rewards are normally distributed (requires scipy)."""
    from scipy import stats

    rewards = [bandit.pull() for _ in range(9999999)]
    k2, p = stats.normaltest(rewards)
    assert (
        p > 0.05
    ), "p-value should be greater than 0.05, indicating normal distribution"
