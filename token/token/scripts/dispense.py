from brownie import *


def main():
    for i in range(10):
        spill(i)


def spill(i):
    return Token.deploy("Whiskey", "Wkey", 18, 1e21, {"from": accounts[i]})
