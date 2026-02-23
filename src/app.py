import os

password = "admin123"  # hardcoded password

def login(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query
