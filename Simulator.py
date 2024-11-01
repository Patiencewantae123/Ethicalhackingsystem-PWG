import time
import hashlib

def welcome():
    print("\nWelcome to the Ethical Hacking Code Simulator!")
    print("This simulator provides a hands-on, safe environment to learn basic ethical hacking principles.")
    print("\nModules available:")
    print("1. Network Security")
    print("2. Web Application Security")
    print("3. Cryptography Basics")
    print("0. Exit")

def network_security_module():
    print("\nNetwork Security Module: Basic Network Scanning")
    print("Scenario: Simulate a network scan to identify open ports.")
    ports = [22, 80, 443]
    for port in ports:
        print(f"Scanning port {port}... Open")
        time.sleep(0.5)
    print("Port scan complete! Identified open ports: 22, 80, 443")

def web_application_security_module():
    print("\nWeb Application Security Module: SQL Injection Simulation")
    print("Scenario: Simulate a SQL injection vulnerability.")
    print("Try injecting with ' OR '1'='1'")
    user_input = input("Enter SQL query: ")
    if "OR '1'='1'" in user_input or "or '1'='1'" in user_input:
        print("Access Granted! You've simulated a SQL injection vulnerability.")
    else:
        print("Access Denied. Try again with a different input.")

def cryptography_basics_module():
    print("\nCryptography Basics Module: Hash Cracking Simulation")
    print("Scenario: You have a hashed password: '5f4dcc3b5aa765d61d8327deb882cf99' (MD5).")
    print("Try cracking the hash to find the original password.")
    password_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
    user_input = input("Enter password guess: ")
    if hashlib.md5(user_input.encode()).hexdigest() == password_hash:
        print("Password cracked! The original password is 'password'.")
    else:
        print("Incorrect guess. Try again.")

def main():
    while True:
        welcome()
        choice = input("\nEnter the number of the module you want to try: ")
        
        if choice == "1":
            network_security_module()
        elif choice == "2":
            web_application_security_module()
        elif choice == "3":
            cryptography_basics_module()
        elif choice == "0":
            print("Exiting the Ethical Hacking Code Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid module.")

if __name__ == "__main__":
    main()
