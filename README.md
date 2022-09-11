# ATM controller project

## Features
---
```
        0. Logout and Exit     
        1. View Account Balance
        2. Deposit Cash        
        3. Withdraw Cash
        4. Change PIN
        5. Return Card
```
## Instructions
---
Clone repository
```
git clone https://github.com/wkdalswns0427/PAW-ATM-controller.git
```
Install all required packages
```
pip install -r requirements.txt
```
If you need to manually add user, please update in **users.json** in format below
```
"name":{
        "PIN" : int,
        "accounts":[int,int,int],
        "balance":[int,int,int]
    },
```
Run the application
```
python3 main.py
```
---
acutal use manual
- log in with data in DB


final update 2022-09-11 23:00:00 KST