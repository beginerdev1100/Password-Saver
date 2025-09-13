import sys
import csv
import os

def main(accounts):
    print("Z see passwords")
    print("Y add password")
    op = input("X stop: ").lower().strip()

    if op == "z":
        mainn(accounts)
        return None
    elif op == "x":
        save_accounts(accounts)   
        sys.exit()
    elif op == "y":
        i = input("Input Name: ").lower().strip()
        x = input("Input Email: ")
        y = input("Input Password: ")
        return i, x, y
    else:
        print("Invalid option")
        return None

def mainn(accounts):
    i = input("Name to lookup: ").lower().strip()
    if i in accounts:
        print("Email:", accounts[i]["email"])
        print("Password:", accounts[i]["pas"])
    else:
        print("Name not found")

def save_accounts(accounts):
    with open("passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "email", "password"])  # header
        for acc in accounts.values():
            writer.writerow([acc["name"], acc["email"], acc["pas"]])
    print("Accounts saved to passwords.csv")

def load_accounts():
    accounts = {}
    if os.path.exists("passwords.csv"):
        with open("passwords.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts[row["name"]] = {
                    "name": row["name"],
                    "email": row["email"],
                    "pas": row["password"]
                }
    return accounts

def start():
    accounts = load_accounts()   
    while True:
        result = main(accounts)
        if result:
            i, x, y = result
            accounts[i] = dict(name=i, email=x, pas=y)

accounts = start()
if __name__ == "__main__":
    start()