# Security Coding Review

## 1. Vulnerable Code

The vulnerable application stores and compares the password directly in plain text.

### Security Issues
- Password is stored in plain text.
- Hardcoded credentials can be exposed.
- Plain-text password handling is insecure.

## 2. Secure Code

The secure version uses password hashing and hides the password while it is being entered.

### Security Improvements
- Password is converted into a SHA-256 hash.
- The password is not displayed during input.
- Hardcoded plain-text password comparison is avoided.

## 3. Conclusion

The secure version improves password protection by using hashing and secure password input techniques.
## 4. Static Analysis Result

Bandit was used to scan the vulnerable Python application.

### Finding
- Tool: Bandit
- Vulnerability: Hardcoded password
- Severity: Low
- Location: vulnerable_app.py, line 6
- CWE: CWE-259

### Remediation
The hardcoded password should not be stored directly in the source code. Passwords should be securely stored and verified using appropriate hashing and authentication practices.