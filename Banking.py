import sys, time
import json

def who_are_you():
    with open('users.json') as f:
        user_data = json.load(f)
    user = input("Insert Card (type your user_code since we don't currently have card reader)")
    # if user name is not found in DB update user info
    if user not in user_data:
        print("You are a new user please provide your info")
        PIN = int(input("PIN:"))
        accounts, balance = [], []
        N = input("How many accounts? :")

        for i in range(int(N)):
            acc = int(input("enter account id :"))
            bal = int(input("enter balance :"))
            accounts.append(acc)
            balance.append(bal)

        new_user_data = {
            user:{
                "PIN":PIN,
                "accounts":accounts,
                "balance":balance
            }
        }
        user_data.update(new_user_data)
        with open("users.json", 'w',encoding='utf-8') as f:
            json.dump(user_data, f, indent='\t')
            
    return user

class banking():
    def __init__(self, user):
        with open('users.json') as f:
            self.user_data = json.load(f)
        self.user = user
        print("Welcome {user}! Verify with PIN".format(user=self.user))
        self.PIN = int(input("PIN :"))
    
    def verify_user(self):
        if self.PIN != self.user_data[self.user]["PIN"]:
            self.cnt = 0
            while self.cnt < 3:
                self.PIN = int(input("retry PIN :"))
                if self.PIN == self.user_data[self.user]["PIN"]:
                    break
                self.cnt+=1

            if self.PIN != self.user_data[self.user]["PIN"]:
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
        print("\t2. Deposit Cash")
        print("\t3. Withdraw Cash")
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
            self.choose_2()
            self.return_to_main()
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
        self.L = len(self.user_data[self.user]["accounts"])
        for i in range(self.L):
            print("account: ",self.user_data[self.user]["accounts"][i])
        self.selected = int(input("select account : "))
        self.idx = self.user_data[self.user]["accounts"].index(self.selected)
        return self.selected, self.idx

    # log out done
    def choose_0(self):
        print("Exiting...")
        time.sleep(1)
        sys.exit("You have been logged out")
    
    # balance check done
    def choose_1(self):
        self.account, self.idx = self.select_account()
        print("Hello {user}! your account {account} balance is".format(user=self.user, account=self.account))
        print("${dollars}".format(dollars=self.user_data[self.user]["balance"][self.idx]))
        print("\n")
    
    # deposit done
    def choose_2(self):
        self.account, self.idx = self.select_account()
        print("current balance is ${dollars}".format(dollars=self.user_data[self.user]["balance"][self.idx]))
        print("wait for cassette to open...") # open cassette
        time.sleep(1)
        amount = int(input("insert cash(type in the amount) : $"))
        new_balance = self.user_data[self.user]["balance"][self.idx] + amount
        print("input : {input} , current balance : {new}".format(input=amount, new=new_balance))
        self.user_data[self.user]["balance"][self.idx] = new_balance
        
        with open('users.json','w',encoding='utf-8') as f:
            json.dump(self.user_data, f, indent="\t")
        
        print("\n")
    
    # withdraw done
    def choose_3(self):
        self.account, self.idx = self.select_account()
        print("current balance is ${dollars}".format(dollars=self.user_data[self.user]["balance"][self.idx]))
        amount = int(input("How much will you withdraw? : "))
        if amount > self.user_data[self.user]["balance"][self.idx]:
            print("That exceeds your balance! retry")
            print()
            self.choose_3()
        else:
            new_balance = self.user_data[self.user]["balance"][self.idx] - amount
            self.user_data[self.user]["balance"][self.idx] = new_balance
            print("withdrawal : {input} , current balance : {new}".format(input=amount, new=new_balance))
            with open('users.json','w',encoding='utf-8') as f:
                json.dump(self.user_data, f, indent="\t")
        
        print("\n")
    
    # change PIN ongoing
    def choose_4(self):
        ans=input("Do you really want to change PIN? Y/N > ")
        if ans == "Y" or ans=="y":
            oldpin = self.user_data[self.user]["PIN"]
            newPIN=input("Type in New PIN > ")
            confirm = input("confirm New PIN > ")
            if newPIN == confirm:
                self.user_data[self.user]["PIN"] = int(newPIN)
                with open('users.json','w',encoding='utf-8') as f:
                    json.dump(self.user_data, f, indent="\t")
                print("PIN changed from {old} to {new}".format(old=oldpin, new=newPIN))
            else :
                confirm = input("reconfirm New PIN > ")
                if newPIN == confirm:
                    self.user_data[self.user]["PIN"] = int(newPIN)
                    with open('users.json','w',encoding='utf-8') as f:
                        json.dump(self.user_data, f, indent="\t")
                    print("PIN changed from {old} to {new}".format(old=oldpin, new=newPIN))
                else:
                    print("PIN change cancelled")
        else :
            print("PIN change cancelled")
        print("\n")

    # return card done
    def choose_5(self):
        ans=input("Do you really want to return card? Y/N > ")
        if ans=="Y" or ans=="y":
            print("returning card...")
            time.sleep(1)
            an=input("Will you continue with other card? Y/N > ")
            if an=="N" or an=="n":
                sys.exit("program exit")
            elif an=="Y" or an=="y":
                who_are_you()
        else:
            print("Return card cancelled")
        print("\n")

    def return_to_main(self):
        self.next = input("Do you want to proceed to menu Y/N > ")
        if self.next=="Y" or self.next=="y":
            self.menu_page()
        else:
            sys.exit("program exit")
        