import pytest


class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount("Not enough available to spend {}".format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount


@pytest.fixture
def my_wallet():
    """Returns a Wallet instance with a zero balance and the best practice here is"""
    return Wallet()
@pytest.mark.parametrize(
    "earned,spent,expected",
    [
        (30, 10, 20),
        (20, 2, 18),
    ],
)
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
