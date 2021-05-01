# student = 1

# while student <= 3:
#     total = 0
#     for score in range(1, 4):
#         score = int(input("Enter test score: "))
#         total += score
#     average = total / 300
#     print(f"Student:{student}, average: {average}")

#     student += 1

class SavingsAcc:
    def __init__(self, account_no, interest_rate, bal):
        self.account_no = account_no
        self.interest_rate = interest_rate
        self.bal = bal

    def display_data(self):
        print("\n---Savings Account---")
        print(f"Account Number: {self.account_no}")
        print(f"Interest Rate: {str(self.interest_rate)}")
        print(f"Balance: {str(self.bal)}")
        print("\n")


class CertifcateDeposit:

    def __init__(self, account_no, interest_rate, bal, maturity_date):
        self.account_no = account_no
        self.interest_rate = interest_rate
        self.bal = bal
        self.maturity_date = maturity_date

    def display_data(self):
        print("\n---Certificate of Deposit---")
        print(f"Account Number: {self.account_no}")
        print(f"Interest Rate: {str(self.interest_rate)}")
        print(f"Balance: {str(self.bal)}")
        print(f"Maturity Date: {self.maturity_date}")


print("\nEnter the data required for a savings account.")
acc_no = input("Account Number: ")
int_rate = float(input("Interest Rate: "))
balance = float(input("Balance: "))
savAcc = SavingsAcc(acc_no, int_rate, balance)

print("\nEnter the data requried for a Certificate of Deposit.")
acc_no = input("Account Number: ")
int_rate = float(input("Interest Rate: "))
balance = float(input("Balance: "))
maturityDate = input("Maturity Date: ")
certDepo = CertifcateDeposit(
    acc_no, int_rate, balance, maturityDate)

print("Here is the data that you have entered")
savAcc.display_data()
certDepo.display_data()
