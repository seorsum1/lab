import pytest
from account import Account


def test_init():
    account = Account('John')
    assert account.get_name() == 'John'
    assert account.get_balance() == 0


def test_deposit():
    account = Account('John')
    assert account.deposit(100) == True
    assert account.get_balance() == 100


def test_deposit_negative_amount():
    account = Account('John')
    assert account.deposit(-50) == False
    assert account.get_balance() == 0


def test_withdraw():
    account = Account('John')
    account.deposit(100)
    assert account.withdraw(50) == True
    assert account.get_balance() == 50


def test_withdraw_negative_amount():
    account = Account('John')
    account.deposit(100)
    assert account.withdraw(-50) == False
    assert account.get_balance() == 100


def test_withdraw_more_than_balance():
    account = Account('John')
    account.deposit(100)
    assert account.withdraw(150) == False
    assert account.get_balance() == 100
