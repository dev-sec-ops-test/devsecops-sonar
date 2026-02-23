import os
import hashlib

# Vulnerabilities (for Sonar testing)

ADMIN_PASSWORD = "admin123"  # Hardcoded secret

def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()  # Weak hashing

def login(user_input):
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"  # SQL Injection
    return query

# Add this so tests pass
def add(a, b):
    return a + b
