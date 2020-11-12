# Curl sample that takes accounts from a file as input and itterates over the account
# to provide as output for run_curl which will curl the url. 

def retrieve_accounts():
    with open('account_test.txt', 'r') as file:
        data = []
        for i, account in enumerate(file):
            accounts = (account[0:12])
            data.append(accounts)
            #print(data)
        return data

def run_curl():
    accounts = retrieve_accounts()
    for account in accounts:
        iam_tool = subprocess.check_output(["mcurl", "https://url-here" + account])
        iam_tool = iam_tool.decode('utf-8')
        print(iam_tool[17:29]) 
        # Create function to store output in a list, possibly seperate file?
    return iam_tool[17:29]

if __name__ == "__main__":
    run_curl()
    


