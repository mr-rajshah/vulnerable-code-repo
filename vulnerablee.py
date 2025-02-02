import os
import subprocess

def insecure_function(user_input):
    # This is a critical vulnerability: Command Injection
    return subprocess.run(f"ls {user_input}", shell=True)

user_input = input("Enter a directory name: ")
insecure_function(user_input)
