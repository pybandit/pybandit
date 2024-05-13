<picture align="center">
  <img alt="Pandas Logo" src="https://raw.githubusercontent.com/pybandit/pybandit/main/doc/_static/logo-pybandit.png">
</picture>

-----------------
[![PyPI Downloads](https://img.shields.io/pypi/dm/pybandit.svg?label=PyPI%20downloads)](
https://pypi.org/project/pybandit/)

# PyBandit : powerful multiarmed bandit toolkit

Welcome to PyBandit, an open-source Python library designed to make experimenting with and deploying multi-armed bandit algorithms simple and accessible. Whether you're a researcher, data scientist, or enthusiast, PyBandit offers a robust platform for exploring bandit algorithms, optimizing decision-making processes, and enhancing your applications with the power of reinforcement learning.

## Features

- **Ease of Use**: Simple, clear APIs make it easy to integrate and experiment with different bandit algorithms.
- **Extensive Documentation**: Comprehensive guides and examples to help you get started quickly.
- **Community Driven**: PyBandit is developed and supported by an enthusiastic community of contributors.
- **Flexibility**: From basic to advanced bandit algorithms, PyBandit supports a wide range of use cases.
- **Scalability**: Built to scale from small projects to large-scale deployments.

## Installation

You can install PyBandit using pip:

```bash
pip install pybandit
```

## Quick Start

```python
import numpy as np
np.random.seed(0)
import pybandit as pb
bandit = pb.bandit.BernoulliBandit(0.7)
bandit.pull()
1
[bandit.pull() for _ in range(5)]
[0, 1, 1, 1, 1]
```

## Contributing to PyBandit

Thank you for your interest in contributing to PyBandit! We are thrilled to have you join our community of developers and researchers dedicated to advancing the field of reinforcement learning through accessible multi-armed bandit algorithms. This document provides guidelines for contributing to PyBandit and should be followed to ensure a smooth collaboration process.
Contributions can take various forms, from bug fixes and feature additions to documentation improvements and example tutorials. Here's how you can get started:

### Development Environment

Setting up your development environment is easy:

```bash
git clone https://github.com/your_username/pybandit.git
cd pybandit
conda create -n pybandit-dev -c conda-forge python=3.11
conda activate pybandit-dev
pip install -e . --no-build-isolation
pip install -r requirements_dev.txt
```

### Writing Documentation

Good documentation is crucial for any project. Help us improve and expand our docs. Documentation changes can be proposed in the same way as code changes, through a pull request.

### Asking for Help

If you need help at any point, feel free to ask questions in our community forum or on the GitHub issue tracker. We value your contributions and will do our best to provide support.
