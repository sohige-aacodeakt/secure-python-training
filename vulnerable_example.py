#!/usr/bin/env python3
"""
VULNERABLE EXAMPLE: Unsafe input handling.

This script accepts a username and age from the user and prints a greeting.
It does NOT validate the input, making it susceptible to injection attacks.
"""

def vulnerable_greeting():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    # No validation – age is used directly in a formatted string
    # This could lead to code injection if age contains malicious input.
    print(f"Hello {name}, you are {age} years old.")

    # Simulate a database query (vulnerable to SQL injection)
    query = f"SELECT * FROM users WHERE name = '{name}' AND age = {age}"
    print(f"[DEBUG] Query: {query}")

if __name__ == "__main__":
    vulnerable_greeting()
