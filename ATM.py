
class atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number


    def cashWithdrawal(self, card_number):
            print("Money has been successfully withdrawaled")
    def balanceEnquiry(self, pin_number):
            print("You have sufficient balance")
    def cashDeposit(self, card_number):
            print("Your cash is safely deposited")

idfcBank = atm(28382929929, 2020)
print(idfcBank.cashWithdrawal(28382929929))