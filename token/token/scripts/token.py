#!/usr/bin/python3

from brownie import Token, accounts


def main():
    return Token.deploy("Whiskey", "wkey", 18, 1e21, {'from': accounts[0]})
