class Account:
    accounts = []
    bank_balance = 0
    bank_loan = 0

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transition_history = []
        self.account_number = len(Account.accounts) + 1001
        Account.accounts.append(self)
        self.loan_cnt = 0

    def deposit(self, amount):
        self.balance += amount
        Account.bank_balance += amount
        print(f"\nSuccessfully deposited {amount} taka. Your current balance is {self.balance} taka")
        self.transition_history.append(f"Successfully deposited {amount} taka")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nWithdrawal amount exceeded")
        else:
            self.balance -= amount
            Account.bank_balance -= amount
            print(f"\nWithdraw of {amount} approved. Your current balance is {self.balance} taka")
            self.transition_history.append(f"Successfully withdrawn {amount} taka")

    def available_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transition_history(self):
        print("\n--------------- Transition History ---------------")
        for transition in self.transition_history:
            print(transition)

    def take_loan(self, amount):
        if amount > self.loan_cnt <= 2:
            if amount > 0:
                self.loan_cnt += 1
                self.balance += amount
                Account.bank_balance -= amount
                Account.bank_loan += amount
                print(f"\nSuccessfully taken {amount} for loan!!")
                self.transition_history.append(f"\nSuccessfully {amount} taken as loan!!")
            else:
                print("\nInvalid amount inserted!!")
        else:
            print("\nYou are not allowed to take loans more than two times!!")

    def transfer_money(self, user_account_number, amount):
        flag = False
        for person in self.accounts:
            if user_account_number == person.account_number:
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    person.balance += amount
                    flag = True
                    print(f"\nTransfarred {amount} taka succesfully!!")
                    self.transition_history.append(f"Successfully transfarred {amount} taka")

                else:
                    flag = True
                    print("\nInvalid amount inserted!!")

        if flag is False:
            print(f"\nAccount does not exist")

    def __repr__(self) -> str:
        print(f"Account User Name: {self.name}")
        print(f"User Account Number: {self.account_number}")
        print(f"Account User Address: {self.address}")
        print(f"Account User E-mail ID: {self.email}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance : {self.balance}")
        return ""



class Admin(Account):
    bank_admins = []
    def __init__(self, name, admin_id, password):
        self.name = name
        self.admin_id = admin_id
        self.password = password
        self.admin_accounts = []
        self.loan_approval = True
        Admin.bank_admins.append(self)

    def delete_account(self, acc_number):
        flag = False
        for account in admin.admin_accounts:
            if account.account_number == acc_number:
                flag = True
                Account.bank_balance -= account.balance
                admin.admin_accounts.remove(account)
                Account.accounts.remove(account)

        if flag is True:
            print("\nAccount deleted successfully!!")
        else:
            print("\nThe account you wants to delete, that doesn't exists!!")

admin = None
user = None

while True:
    print("\n------------------ Welcome to our Bank ------------------")
    print("1. ADMIN")
    print("2. USER")
    print("3. EXIT")

    option = int(input("Enter Option: "))

    if option == 1:
        f = True
        while True:
            if admin == None:
                print("--------------- Welcome Admin ---------------")
                choice = input("Registar or Login? (R/L): ")

                if choice == 'R':
                    print("Admin Info --> Name: admin, ID: admin, Password: admin1234")
                    name = input("Enter Name: ")
                    id = input("Enter ID: ")
                    password = input("Enter Password: ")
                    admin = Admin(name, id, password)

                elif choice == 'L':
                    print("Admin Info --> Name: admin, ID: admin, Password: admin1234")
                    name = input("Enter Name: ")
                    id = input("Enter ID: ")
                    password = input("Enter Password: ")
                    
                    for ad in Admin.bank_admins:
                        if ad.name == name and ad.admin_id == id:
                            admin = ad
            
            else:
                print("--------------- Welcome Admin ---------------")
                print("1. Create a user account")
                print("2. Delete a user account")
                print("3. See all users accounts list")
                print("4. Check the total available balance of the bank")
                print("5. Check the total loan amount")
                print("6. Exit")

                op = int(input("Enter option: "))

                if op == 1:
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    acc_type = input("Enter account type: ")
                    new_account = Account(name, email, address, acc_type)
                    admin.admin_accounts.append(new_account)
                    print("\nAccount create Successfull!!")

                elif op == 2:
                    acc_num = int(input("Enter account number you want to delete: "))
                    admin.delete_account(acc_num)

                elif op == 3:
                    print("\n---------------- All accounts in the bank list ----------------")
                    for acc_holder in admin.admin_accounts:
                        print(acc_holder)

                elif op == 4:
                    print(f"Total available bank balance: {admin.bank_balance}")

                elif op == 5:
                    print(f"Total loan amount: {admin.bank_loan}")

                elif op == 6: 
                    admin = None
                    break

    elif option == 2:
        while True:
            if user == None:
                flag = False
                print("\n ---------- Give your information to login ----------")
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                address = input("Enter user address: ")
                acc_type = input("Enter user account type: ")

                for userr in Account.accounts:
                    if userr.name == name or userr.email == email or userr.address == address or userr.account_number == acc_type:
                        user = userr
                        flag = True
                        
                if flag is False:
                    print("\nThere is no account with the given informations!!")

            else:
                print("\n---------- Welcome User ----------")
                print("1. Deposit money in your account")
                print("2. Withdraw money in your account")
                print("3. Available Balance")
                print("4. All Transition")
                print("5. Take Loan")
                print("6. Transfer money to another account")
                print("7. Exit")

                op = int(input("Choose option: "))

                if op == 1:
                    amount = int(input("Enter deposit amount: "))
                    user.deposit(amount)

                elif op == 2:
                    amount = int(input("Enter withdraw amount: "))
                    user.withdraw(amount)

                elif op == 3:
                    user.available_balance()

                elif op == 4:
                    user.check_transition_history()

                elif op == 5:
                    loan_amount = int(input("Enter loan amount: "))
                    if loan_amount > Account.bank_balance:
                        print(f"\nBank doesn't have {loan_amount} to give loan!!")
                    else:
                        user.take_loan(loan_amount)

                elif op == 6:
                    transfer_acc_num = int(input("Enter account number in which you want to send money: "))
                    transfer_amount = int(input("Enter amount: "))
                    user.transfer_money(transfer_acc_num, transfer_amount)

                elif op == 7:
                    user = None
                    break

    elif option == 3:
        print("\nThanks for using our service!!")
        break

    else:
        print("\nInvalid option choosen!!\nTry again!!")


# sayem = Account("sayem", "sayem@gmail.com", "Dhaka", "savings")
# sayem.deposit(1000)
# sayem.deposit(2000)
# sayem.withdraw(500)
# sayem.take_loan(200)

# atik = Account("Shihab", "shihab@gmail.com", "Dhaka", "Current")

# sayem.display_info()
# atik.display_info()

# for transfer in sayem.transition_history:
#     print(transfer)