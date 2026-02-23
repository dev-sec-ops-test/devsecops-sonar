import os

def add(a, b):
    return a + b

def insecure_password():
    # Intentional issue for Sonar (hardcoded secret)
    password = "admin123"
    return password

def divide(a, b):
    return a / b
