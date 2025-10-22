from customer import Customer

class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []


    def create_account(self, category, owner, interest_rate):
        if category not in ["account", "credit", "savings"]:
            raise TypeError("Invalid Account type")
        elif not isinstance(owner, Customer):
            raise TypeError("Owner must be a customer")
        
        account = {
            "owner": owner.name,
            "ssn": owner.ssn,
            "category": category,
            "interest": interest_rate
        }
        self.accounts.append(account)

    def find_accounts_by_ssn(self, ssn):
        account_list = []
        for x in self.accounts:
            if x["ssn"] == ssn:
                account_list.append(x)
        return account_list
    
    def find_accounts_by_name(self, name):
        account_list = []
        for x in self.accounts:
            if x["owner"].startswith(name):
                account_list.append(x)
        return account_list




    
        

jack = Customer("Jack", "123")
john = Customer("John", "456")
dave = Customer("Dave", "789")

cibc = Bank("CIBC")
cibc.create_account("account", jack, 7)
rbc = Bank("RBC")
rbc.create_account("credit", john, 11)
td = Bank("TD")
td.create_account("savings", dave, 8)
# print(cibc.accounts, rbc.accounts, td.accounts)
# print(cibc.find_accounts_by_ssn("123"))
print(cibc.find_accounts_by_name("J"))
