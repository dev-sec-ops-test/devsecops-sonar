import os
import hashlib
import subprocess

# 🔴 Hardcoded credentials (Security issue)
ADMIN_PASSWORD = "admin123"

def weak_hash(password):
    # 🔴 Weak hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()

def login(user_input):
    # 🔴 SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    return query

def run_command(user_input):
    # 🔴 Command Injection vulnerability
    os.system("ls " + user_input)

def dangerous_eval(user_input):
    # 🔴 Arbitrary code execution
    return eval(user_input)

if __name__ == "__main__":
    print("App running...")
