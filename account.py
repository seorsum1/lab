class Account:
    """
    A class representing details for a person's account balance
    """
    
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of account with initial balance of zero.
        :param name: Account owner's name.
        """
        self.__account_name = name
        self.__account_balance = 0
        
    def deposit(self, amount: float) -> bool:
        """
        Method to increment person's account balance by amount.
        :param amount: Integer or float to add to account balance, must be positive above zero.
        :return: True if deposit transaction is successful, False otherwise.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
        
    def withdraw(self, amount: float) -> bool:
        """
        Method to decrement person's account balance by amount.
        :param amount: Integer or float to subtract to account balance, must be positive above zero and greater than current balance.
        :return: True if withdraw transaction is successful, False otherwise.
        """
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False
        
    def get_balance(self) -> float:
        """
        Method to get person's account balance.
        :return: Float value of account balance.
        """
        return self.__account_balance
        
    def get_name(self) -> str:
        """
        Method to get person's account name.
        :return: String value of account name.
        """
        return self.__account_name
