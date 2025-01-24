import os
import subprocess

def open_notepad(text):
    # Define the path to Notepad.exe (for Windows)
    notepad_path = r"C:\Windows\System32\notepad.exe"

    # Create a new command with the text
    command = f'"{notepad_path}" "{text}"'

    # Use subprocess to execute the command
    subprocess.run(command, shell=True)

# Example usage:
open_notepad('Hello, World!')
