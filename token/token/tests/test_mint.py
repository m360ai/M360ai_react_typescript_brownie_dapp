from itertools import accumulate
from black import assert_equivalent


def test_mint(accounts, token):
    assert token.balanceOf(accounts[0]) == 1e21

def test_name(accounts, token):
    assert token.symbol() == 'wkey'
