from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def widraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Widrawing")
    fund_me.widraw({"from": account})


def main():
    fund()
    widraw()
