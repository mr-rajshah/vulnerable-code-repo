import os

password = "hardcoded_secret"  # Hardcoded password (Critical vulnerability)

def insecure_function():
    os.system("rm -rf /")  # Command Injection (Critical vulnerability)
