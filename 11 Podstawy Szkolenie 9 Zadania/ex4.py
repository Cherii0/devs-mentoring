
class BankAccount:


    def __init__(self, no_acc, owner, status):
        self.__no_acc = no_acc
        self.__owner = owner
        self.__status = status
        self.__commission_pct = 2
        self.__operational_commission_pln = 0

    def change_ownership(self, new_owner):

        if new_owner != self.__owner:
            self.__owner = new_owner
        else:
            print(f"{new_owner} is same as old owner name and last name")

    def deposit(self, amount):

        self.__operational_commission_pln = (amount // 100) * self.__commission_pct
        self.__status = amount - self.__operational_commission_pln

    def withdraw(self, amount):

        # not enough money
        if amount > self.__status:
            print("not enough money")
            return 0

        # enough money
        self.__status -= amount
        print(f"withdraw {amount}, now your status is {self.__status}")
        return amount

    def get_owner(self):
        return self.__owner

    def get_status(self):
        return self.__status

    def display(self):
        print(f"wlascicielem konta o numerze {self.__no_acc} jest {self.__owner}"
              f". Dostepne srodki na koncie wynosza : {self.__status} PLN")

def main():
    account = BankAccount(no_acc=123, owner="Jan Kowalski", status="active")

    account.deposit(244)
    print(account.get_status())
    account.withdraw(95)
    account.withdraw(195)

    account.change_ownership("Grzegorz Glowacki")
    print(f"owner : {account.get_owner()}")

    account.display()

if __name__ == "__main__":
    main()
