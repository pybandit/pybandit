import numpy as np


class GaussianBandit:
    """
    A simple Gaussian bandit with a single arm.

    Attributes
    ----------
    mean : float
        The mean reward of the Gaussian distribution.
    std_dev : float
        The standard deviation of the Gaussian distribution.

    Examples
    --------
    >>> np.random.seed(0)
    >>> bandit = GaussianBandit(mu=0, sigma=1)
    >>> bandit.pull()  # Random output, example: 1.764052345967664
    """

    def __init__(self, mean=0.0, std_dev=1.0):
        """
        Parameters
        ----------
        mean : float, optional
            The mean reward of the Gaussian distribution (default is 0.0).
        std_dev : float, optional
            The standard deviation of the Gaussian distribution (default is 1.0).
        """
        self.mean = mean
        self.std_dev = std_dev

    def pull(self):
        """
        Pull the arm of the bandit and get a reward.

        Returns
        -------
        float
            A reward sampled from the Gaussian distribution defined by the mean and std_dev.
        """
        return np.random.normal(self.mean, self.std_dev)
