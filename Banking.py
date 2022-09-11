import sys, time
from users import user_data

def who_are_you():
    user = input("Insert Card (type your user_code since we don't currently have card reader)")
    # if user name is not found in DB update user info
    if user not in user_data:
        print("You are a new user please provide your info")
        PIN = input("PIN:")
        accounts, balance = [], []
        N = input("How many accounts? :")

        for i in range(int(N)):
            acc = input("enter account id :")
            bal = input("enter balance :")
            accounts.append(acc)
            balance.append(bal)

        new_user_data = {
            "PIN":PIN,
            "accounts":accounts,
            "balance":balance
        }

        user_data[user] = new_user_data

    return user


class banking():
    def __init__(self, user):
        self.user = user
        print("Welcome {user}! Verify with PIN".format(user=self.user))
        self.PIN = int(input("PIN :"))
    
    def verify_user(self):
        if self.PIN != user_data[self.user]["PIN"]:
            self.cnt = 0
            while self.cnt < 4:
                self.PIN = int(input("retry PIN :"))
                if self.PIN == user_data[self.user]["PIN"]:
                    break
                self.cnt+=1

            if self.PIN != user_data[self.user]["PIN"]:
                print("wrong PIN user locked...\n Please cnatace maintanence")
                sys.exit("Killing Program")
            else:
                print("user verified")
                return True
        else:
            print("user verified")
            return True
    
    # def log_in(self):
    #     if self.verify_user():
    #         return True
    
    def menu_page(self):
        if self.verify_user():
            print("\t0. Logout and Exit")
            print("\t1. View Account Balance")
            print("\t2. Withdraw Cash")
            print("\t3. Deposit Cash")
            print("\t4. Change PIN")
            print("\t5. Return Card")
            self.choice = int(input("Enter number to proceed > "))
            print("\n\n")
        else:
            sys.exit("Why is this still running? Killing...")
    
    def select_account(self):
        self.L = len(user_data[self.user]["accounts"])
        print()
        for i in range(self.L):
            print("account: ",user_data[self.user]["accounts"][i])
        self.selected = input("select account : ")
        return self.selected

    def choose_0(self):
        print("Exiting...")
        time.sleep(1)
        sys.exit("You have been logged out")
    
    def choose_1(self):
        self.account = self.select_account()
        print("\n\n")


    
    def return_to_main(self):
        self.menu_page()
        

def main():
    user = who_are_you()
    bank_use = banking(user)
    bank_use.menu_page()