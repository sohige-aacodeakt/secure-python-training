# Exercise: Email Validator

## Objective
Create a Python script that validates and sanitizes email addresses according to RFC 5322 standards.

## Requirements
1. Accept an email address as user input.
2. Validate the local‑part and domain using a regular expression that follows RFC 5322.
3. Sanitize the input by removing any leading/trailing whitespace and converting the domain part to lowercase.
4. Reject any input that contains potentially dangerous characters (e.g., `;`, `|`, `&`, `$`, `` ` ``, `'`, `"`).
5. Print the sanitized email if valid, otherwise print an error message.

## Bonus Challenge
- Use a parsing library like `email.utils` to further validate the address.
- Extend the validator to check for disposable email domains.

## Submission
Place your solution in a file named `email_validator.py` and include it in the module folder.
