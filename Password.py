import sys

def main(accounts):
    print("Z see passwords")
    print("Y Add password")
    op = input("X stop: ").lower().strip()
    if op == "z":
        mainn(accounts)
        return None
    elif op == "x":
        sys.exit()
    i = input("Input Name: ").lower().strip()
    x = input("Input Email: ")
    y = input("Input Password: ")
    return i, x, y

def mainn(accounts):
    i = input("Name to lookup: ")
    if i in accounts:
        print("Email:", accounts[i]["email"])
        print("Password:", accounts[i]["pas"])
    else:
        print("Name not found")

def start():
    accounts = {}
    while True:
        result = main(accounts)
        if result:
            i, x, y = result
            accounts[i] = dict(name=i, email=x, pas=y)

    return accounts

accounts = start()
