# ATM controller project : Paw Banking System

```
---------------------------------------------------------
               ____  ___ _       __       
      __/|_   / __ \/   | |     / /  __/|_
     |    /  / /_/ / /| | | /| / /  |    /
    /_ __|  / ____/ ___ | |/ |/ /  /_ __| 
     |/    /_/   /_/  |_|__/|__/    |/    
                                          

       ____              __   _            
      / __ )____ _____  / /__(_)___  ____ _
     / __  / __ `/ __ \/ //_/ / __ \/ __ `/
    / /_/ / /_/ / / / / ,< / / / / / /_/ / 
   /_____/\__,_/_/ /_/_/|_/_/_/ /_/\__, /  
                                  /____/   
   _____            __                    
  / ___/__  _______/ /____  ____ ___      
  \__ \/ / / / ___/ __/ _ \/ __ `__ \     
 ___/ / /_/ (__  ) /_/  __/ / / / / /     
/____/\__, /____/\__/\___/_/ /_/ /_/      
     /____/                               

---------------------------------------------------------
 version 1.0.0
---------------------------------------------------------

```
## Features
```
        0. Logout and Exit     
        1. View Account Balance
        2. Deposit Cash        
        3. Withdraw Cash
        4. Change PIN
        5. Return Card
```
---
## Instructions
Clone repository
```
git clone https://github.com/wkdalswns0427/PAW-ATM-controller.git
```
Install all required packages
```
pip3 install -r requirements.txt
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
you shall log in with or without user data in users.json

---
## Actual Use Image
- **Log in with data in DB**

    ![menuimage](https://user-images.githubusercontent.com/68832065/189533662-9c3324a5-3580-4f20-98de-cc5210fe517f.JPG)

- **Log in with data not in DB**

    ![newuser](https://user-images.githubusercontent.com/68832065/189533669-427f498c-fdfa-4943-959a-e6163710f28b.JPG)

- **Logout and Exit**

    ![img0](https://user-images.githubusercontent.com/68832065/189533685-ec58d5da-b722-4c7a-99aa-49e5d9191763.JPG)

- **View Account Balance**

    ![img1](https://user-images.githubusercontent.com/68832065/189533691-36746548-d298-4e3b-b195-08ed9d22fae4.JPG)

- **eposit Cash**

    ![img2](https://user-images.githubusercontent.com/68832065/189533692-49ff2074-3606-4b63-a04f-8363adfd6770.JPG)

- **Withdraw Cash**

    ![img3](https://user-images.githubusercontent.com/68832065/189533693-c89c5432-8d7c-48e3-8564-78895ea076c8.JPG)

- **Change PIN**

    ![img4](https://user-images.githubusercontent.com/68832065/189533720-5175cc34-612d-47ae-a66e-ac5a66938e5b.JPG)

- **Return Card**

    ![img5](https://user-images.githubusercontent.com/68832065/189533721-fea7e7e0-7a06-458c-b812-403c9cacaf9f.JPG)

---
final update 2022-09-11 23:00:00 KST
