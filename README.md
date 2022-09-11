# ATM controller project
Features
- Read card
- log in with PIN
- select your account
- See Balance/Deposit/Withdraw/
---

clone the repo
```
git clone https://github.com/wkdalswns0427/PAW-ATM-controller.git
```
if you need to manually add user please update in **users.py** in format below
```
"user":{
        "PIN" : int,
        "accounts":[int,int,int],
        "balance":[int,int,int]
    },
```