from bank_accounts import *

John = BankAccount(1000,"John")
Sarah = BankAccount(2000,"Sarah")

John.getBalance()
Sarah.getBalance()

Sarah.deposit(500)

John.withdraw(10000)
John.withdraw(10)

John.transfer(100000,Sarah)
John.transfer(200,Sarah)

Céline = InterestRewardsAcct(1000,"Céline")

Céline.getBalance()
Céline.deposit(100)
Céline.transfer(100,John)

George = SavingsAccount(1000,"George")

George.getBalance()
George.deposit(100)
George.transfer(1000,Sarah)

