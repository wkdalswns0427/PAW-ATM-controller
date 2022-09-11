import sys, time
import json
from Banking import who_are_you, banking

def main():
    user = who_are_you()
    bank_use = banking(user)
    if bank_use.log_in():
        bank_use.menu_page()

if __name__=="__main__":
    main()
