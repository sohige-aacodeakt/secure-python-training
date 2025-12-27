#!/usr/bin/env python3
"""
SECURE SOLUTION: Proper input validation and sanitization.

This script demonstrates safe input handling using whitelisting and parameterized queries.
"""

import re

def safe_greeting():
    # Validate name: allow only letters, spaces, hyphens, and apostrophes
    name_pattern = re.compile(r"^[A-Za-z\s\-\']+$")
    name = input("Enter your name: ").strip()
    
    while not name_pattern.match(name):
        print("Invalid name. Please use only letters, spaces, hyphens, or apostrophes.")
        name = input("Enter your name: ").strip()

    # Validate age: must be a positive integer between 1 and 120
    age = input("Enter your age: ").strip()
    while not age.isdigit() or not (1 <= int(age) <= 120):
        print("Invalid age. Please enter a whole number between 1 and 120.")
        age = input("Enter your age: ").strip()
    age_int = int(age)

    print(f"Hello {name}, you are {age_int} years old.")

    # Use parameterized queries to prevent SQL injection
    # (simulated with a placeholder syntax)
    query = "SELECT * FROM users WHERE name = %s AND age = %s"
    params = (name, age_int)
    print(f"[DEBUG] Safe query: {query} with parameters {params}")

if __name__ == "__main__":
    safe_greeting()
