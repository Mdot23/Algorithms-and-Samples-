
def retrieve_accounts():
    account_ids = input("Enter commmercial account id: ")
    account_ids = account_ids.split()
    print(account_ids)

    while True:
        for accounts in account_ids:
            if len(accounts) != 12:
                raise ValueError("Account numbers must be 12 characters")
            else:
                print('Account Id: %s'%accounts)
        break

    verify = input(str("Is this correct? "))
    verify = verify.strip() # Remove trailing and leading whitespaces 
    if verify == 'y':
        return account_ids
    if verify == 'n':
        print('terminated')
        return None
    else:
        raise ValueError("Invalid input, choose 'y' or 'n'")

if __name__ == "__main__":
    retrieve_accounts()
