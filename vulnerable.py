import os

password = "hardcoded_secret"  # Hardcoded password (Critical vulnerability)
password = "another_secret"  # New hardcoded secret

def insecure_function():
    os.system("rm -rf /")  # Command Injection (Critical vulnerability)
