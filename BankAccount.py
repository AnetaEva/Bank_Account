# data attributes: account_num, interest_rate, and balance
class SavingsAccount:
    def __init__(self, account_num, interest_rate, balance):
        self.account_num = account_num
        self.interest_rate = interest_rate
        self.balance = balance

    # methods: get_account_num, check_balance, apply_interest, deposit, and withdraw
    def get_account_num(self):
        return self.account_num

    def get_balance(self):
        return self.balance

    def get_interest_rate(self, int_rate):
        self.balance = self.balance * (1 + int_rate)
        # self.apply_interest = self.balance * self.interest_rate
        return self.balance

    def get_deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        return self.balance

    def get_withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - withdraw_amount
        return self.balance


# Design a CDAccount as a subclass of the SavingAccount class
class CDAccount(SavingsAccount):
    # new attributes: mini_balance
    def __init__(self, account_num, interest_rate, balance, mini_balance):
        SavingsAccount.__init__(self, account_num, interest_rate, balance)
        self.mini_balance = mini_balance

    # new methods: withdraw (this method should ensure the mini_balance in the account,
    # otherwise displays "insufficient balance")
    def get_mini_balance(self, mini_balance):
        if mini_balance > self.balance:
            return 'Insufficient Funds'
        self.balance = self.balance + mini_balance
        return self.balance


# main() function, create an object of SavingAccount and perform deposit, apply interest, and withdraw operations;
# then create an object of CDAccount and perform the same series of operations.

def main():
    print('Enter information for a saving account:')
    acct_num = input('Account number: ')
    int_rate = float(input('Interest rate: '))
    balance = float(input('Initial Balance: '))
    deposit_amount = float(input('Deposit Amount: '))

    savings = SavingsAccount(acct_num, int_rate, balance)
    print('Account', savings.get_account_num(), 'Balance: $', format(savings.get_deposit(deposit_amount), ',.2f'),
          sep='')
    print('Applying Interest')
    print('Account', savings.get_account_num(), 'Balance: $', format(savings.get_interest_rate(int_rate), ',.2f'),
          sep='')
    withdraw_amount = float(input('Withdraw Amount: '))
    print('Account', savings.get_account_num(), 'Balance: $', savings.get_withdraw(withdraw_amount))

    print()

    print('Enter information for CD account:')
    acct_num = input('Account number:')
    int_rate = float(input('Interest rate:'))
    balance = float(input('Initial Balance:'))
    mini_balance = input('Minimum Balance:')
    deposit_amount = float(input('Deposit Amount: '))

    cd = CDAccount(acct_num, int_rate, balance, mini_balance)
    print('Account', cd.get_account_num(), 'Balance: $', format(cd.get_deposit(deposit_amount), ',.2f'), sep='')
    print('Applying Interest')
    print('Account', cd.get_account_num(), 'Balance: $', format(cd.get_interest_rate(int_rate), ',.2f'), sep='')
    withdraw_amount = float(input('Withdraw Amount: '))
    print('Account', cd.get_account_num(), 'Balance: $', cd.get_withdraw(withdraw_amount))


main()
