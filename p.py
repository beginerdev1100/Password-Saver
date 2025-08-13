def main():
    print("Save passwords")
    print("see passwords")
    i = input("")
    if i == "save passwords":
        passwords = ps(passwords)
    elif i == "see passwords":
        pss(passwords)
    return passwords

def ps(passwords):
    while True:
        i = input("Password Input (or type stop): ")
        if i == "stop":
            break
        passwords.append(i)  
    return passwords

def pss(passwords):
    for every 

while True:
    passwords = main(passwords)




