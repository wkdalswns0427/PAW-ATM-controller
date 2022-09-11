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
            while self.cnt < 3:
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
    
    def log_in(self):
        if self.verify_user():
            return True
        else:
            sys.exit("Killing Program")
    
    def menu_page(self):
        print("\t0. Logout and Exit")
        print("\t1. View Account Balance")
        print("\t2. Withdraw Cash")
        print("\t3. Deposit Cash")
        print("\t4. Change PIN")
        print("\t5. Return Card")
        self.choice = int(input("Enter number to proceed > "))
        self.proceed_to_next()
    
    def proceed_to_next(self):
        if self.choice == 0:
            self.choose_0()
        elif self.choice == 1:
            self.choose_1()
            self.return_to_main()
        elif self.choice == 2:
            self.return_to_main()
            self.choose_2()
        elif self.choice == 3:
            self.choose_3()
            self.return_to_main()
        elif self.choice == 4:
            self.choose_4()
            self.return_to_main()
        elif self.choice == 5:
            self.choose_5()
            self.return_to_main()

    def select_account(self):
        self.L = len(user_data[self.user]["accounts"])
        for i in range(self.L):
            print("account: ",user_data[self.user]["accounts"][i])
        self.selected = int(input("select account : "))
        self.idx = user_data[self.user]["accounts"].index(self.selected)
        return self.selected, self.idx

    def choose_0(self):
        print("Exiting...")
        time.sleep(1)
        sys.exit("You have been logged out")
    
    def choose_1(self):
        self.account, self.idx = self.select_account()
        print("Hello {user}! your account {account} balance is".format(user=self.user, account=self.account))
        print("${dollars}".format(dollars=user_data[self.user]["balance"][self.idx]))
        print("\n\n")

    def choose_2(self):
        self.account, self.idx = self.select_account()
        print("current balance is ${dollars}".format(dollars=user_data[self.user]["balance"][self.idx]))
        print("wait for cassette to open...")
        time.sleep(1)
        self.input = input("insert cash(type in the amount) : $")
        
        print("\n\n")
    
    def choose_3(self):
        self.account = self.select_account()
        print("\n\n")
    
    def choose_4(self):
        self.account = self.select_account()
        print("\n\n")

    def choose_5(self):
        self.account = self.select_account()
        print("\n\n")

    def return_to_main(self):
        self.next = int(input("Enter 0 if you want to exit 1 if you want to proceed to menu"))
        if self.next==1:
            self.menu_page()
        else:
            sys.exit("program exit")
        